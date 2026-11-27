"""Offline regression tests for the defects the advisory council found (council/ADDENDUM-01B item 10).

Run from sitehustle/:  python3 -m unittest discover -s tests -v
No network: email, Netlify and Stripe calls are replaced with fakes.
"""
import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "scripts"))
import hustle as h  # noqa: E402

LOCAL = """
business: {name: Test Studio, sender_name: Pat Example, sender_email: pat@studio.test, reply_to: pat@studio.test,
           phone: "(717) 555-0100", owner_digest_email: owner@test.test, postal_address: "PO Box 1, Town, PA 17055"}
offer: {stripe_payment_link: "https://buy.stripe.com/test", terms_url: "https://studio.test/terms"}
outreach: {mode: manual, send_window_hours_local: [0, 24], send_weekends: true}
"""

SAMPLE = json.loads((HERE / "examples" / "sample-lead.json").read_text())


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copy(HERE / "config.yaml", self.tmp / "config.yaml")
        shutil.copytree(HERE / "templates", self.tmp / "templates")
        (self.tmp / "config.local.yaml").write_text(LOCAL)
        self._orig = {k: getattr(h, k) for k in ("ROOT", "DATA", "LEADS", "SUPPRESS", "DIGESTS", "SITES",
                                                  "BUNDLE", "OUTBOX", "FAILED")}
        h.ROOT, h.DATA = self.tmp, self.tmp / "data"
        h.LEADS, h.SUPPRESS, h.DIGESTS = h.DATA / "leads.json", h.DATA / "suppression.txt", h.DATA / "digests.json"
        h.SITES, h.OUTBOX = self.tmp / "sites", self.tmp / "outbox"
        h.BUNDLE, h.FAILED = h.SITES / "_preview_bundle", h.OUTBOX / "failed"
        h.ensure_dirs()
        self.sent = []
        self.fail_to = set()

        def fake_send(c, to, subject, body, headers=None, idempotency_key=None):
            if to in self.fail_to:
                raise h.SendError("422: invalid recipient")
            self.sent.append({"to": to, "subject": subject, "body": body})
            return f"msg-{len(self.sent)}"

        self._send, self._sleep = h.send_email, h.time.sleep
        h.send_email = fake_send
        h.time.sleep = lambda s: None

    def tearDown(self):
        for k, v in self._orig.items():
            setattr(h, k, v)
        h.send_email, h.time.sleep = self._send, self._sleep
        shutil.rmtree(self.tmp)

    # helpers
    def add(self, **over):
        d = copy.deepcopy(SAMPLE)
        d.update(over)
        f = self.tmp / "in.json"
        f.write_text(json.dumps(d))
        h.cmd_upsert(str(f))
        return h.load()[-1]

    def set_status(self, lead_id, status, **extra):
        leads = h.load()
        l = h.find(leads, lead_id)
        l["status"] = status
        l.update(extra)
        h.save(leads)

    def previewed(self, **over):
        l = self.add(**over)
        self.set_status(l["id"], "previewed", preview_url=f"https://previews.test/{l['id']}/")
        return l["id"]

    def digest_and_approve(self, skip=()):
        h.cmd_digest(print_only=True)
        did = max(json.loads(h.DIGESTS.read_text()))
        h.cmd_approve(did, list(skip))
        return did


class TestFailClosed(Base):
    def test_unknown_mode_sends_nothing(self):  # T1
        lid = self.previewed()
        h.cmd_queue()
        self.digest_and_approve()
        (self.tmp / "config.local.yaml").write_text(LOCAL.replace("mode: manual", "mode: auto"))
        with self.assertRaises(SystemExit):
            h.cmd_send()
        self.assertEqual(self.sent, [])

    def test_paused_sends_nothing_and_no_date_switch(self):  # T2
        self.previewed()
        h.cmd_queue()
        self.digest_and_approve()
        (self.tmp / "config.local.yaml").write_text(LOCAL.replace("mode: manual", "mode: paused"))
        h.cmd_send()
        self.assertEqual(self.sent, [])
        self.assertNotIn("trial_ends", (HERE / "config.yaml").read_text())

    def test_unapproved_items_never_send(self):
        self.previewed()
        h.cmd_queue()
        h.cmd_send()
        self.assertEqual(self.sent, [])


class TestApproval(Base):
    def test_approval_is_bound_to_its_digest_and_used_once(self):  # T3
        a = self.previewed()
        h.cmd_queue()
        h.cmd_digest(print_only=True)
        did = max(json.loads(h.DIGESTS.read_text()))
        b = self.previewed(name="Second Place", address="2 Other St, Mechanicsburg, PA")
        h.cmd_queue()  # queued after the digest went out
        h.cmd_approve(did, [])
        with self.assertRaises(SystemExit):
            h.cmd_approve(did, [])  # reuse refused
        h.cmd_send()
        self.assertEqual(len(self.sent), 1)
        self.assertTrue((h.OUTBOX / f"{b}-outreach.json").exists())

    def test_skip_removes_item(self):
        a = self.previewed()
        h.cmd_queue()
        self.digest_and_approve(skip=["SKIP", a])
        h.cmd_send()
        self.assertEqual(self.sent, [])


class TestDuplicates(Base):
    def test_reupsert_never_regresses_or_repitches(self):  # T4
        lid = self.previewed()
        h.cmd_queue()
        self.digest_and_approve()
        h.cmd_send()
        self.assertEqual(len(self.sent), 1)
        self.add(status="researched")  # the agent re-upserts its research file
        self.assertEqual(h.find(h.load(), lid)["status"], "contacted")
        self.set_status(lid, "previewed")  # even if forced back, no second first-touch email
        h.cmd_queue()
        self.assertFalse((h.OUTBOX / f"{lid}-outreach.json").exists())

    def test_unknown_id_rejected(self):  # T5
        d = copy.deepcopy(SAMPLE)
        d["id"] = "L9999"
        f = self.tmp / "x.json"
        f.write_text(json.dumps(d))
        h.cmd_upsert(str(f))
        self.assertEqual(h.load(), [])

    def test_same_name_gets_unique_slug(self):  # T6
        a = self.add(address="1 A St")
        b = self.add(address="9 Z St")
        self.assertNotEqual(a["slug"], b["slug"])


class TestSending(Base):
    def test_one_bad_address_does_not_block_queue(self):  # T7
        a = self.previewed(email="bad@x.test")
        b = self.previewed(name="Good Place", address="5 B St", email="good@y.test")
        self.fail_to = {"bad@x.test"}
        h.cmd_queue()
        self.digest_and_approve()
        h.cmd_send()
        self.assertEqual([s["to"] for s in self.sent], ["good@y.test"])
        self.assertTrue(list(h.FAILED.glob("*.json")))
        self.assertIn("FAILED SENDS", h.status_line(h.cfg(), h.load()))

    def test_hold_stops_followup(self):  # T8
        lid = self.previewed()
        h.cmd_queue()
        self.digest_and_approve()
        h.cmd_send()
        leads = h.load()
        l = h.find(leads, lid)
        l["emails"][0]["at"] = "2026-01-01T09:00:00-05:00"
        h.save(leads)
        h.cmd_mark(lid, "hold", "angry reply")
        h.cmd_followups()
        self.assertFalse((h.OUTBOX / f"{lid}-followup.json").exists())

    def test_lost_is_suppressed(self):
        lid = self.add()["id"]
        h.cmd_mark(lid, "lost", "said no")
        self.assertTrue(h.suppressed(SAMPLE["email"]))

    def test_replied_lead_gets_no_cold_email(self):
        lid = self.previewed()
        h.cmd_queue()
        self.digest_and_approve()
        self.set_status(lid, "replied")
        h.cmd_send()
        self.assertEqual(self.sent, [])


class TestPaymentsAndLaunch(Base):
    def fake_stripe(self, amount, ref):
        class R:
            status_code = 200
            def raise_for_status(self): pass
            def json(self):
                return {"data": [{"id": "cs_1", "client_reference_id": ref, "payment_status": "paid",
                                  "amount_total": amount, "currency": "usd",
                                  "customer_details": {"email": "someone@else.test"}}], "has_more": False}
        return lambda *a, **k: R()

    def test_wrong_amount_goes_to_hold(self):  # T10
        lid = self.add()["id"]
        orig = h.requests.get
        h.requests.get = self.fake_stripe(100, lid)
        try:
            h.cmd_payments()
        finally:
            h.requests.get = orig
        l = h.find(h.load(), lid)
        self.assertEqual(l["status"], "hold")
        self.assertNotIn("paid_at", l)

    def test_payment_alone_cannot_launch_and_is_reported(self):  # T9 + third-party payment
        lid = self.add()["id"]
        orig = h.requests.get
        h.requests.get = self.fake_stripe(50000, lid)
        try:
            h.cmd_payments()
        finally:
            h.requests.get = orig
        self.assertEqual(h.find(h.load(), lid)["status"], "paid")
        with self.assertRaises(SystemExit):
            h.cmd_launch(lid)  # no written confirmation from the restaurant
        self.assertIn("PAID BUT NOT LAUNCHED", h.status_line(h.cfg(), h.load()))


class TestHonestContent(Base):
    def test_outreach_copy(self):
        lid = self.previewed()
        subject, body = h.render_email(h.cfg(), h.find(h.load(), lid), "outreach")
        self.assertNotIn("live nearby", body)
        self.assertNotIn("my family", body.lower())
        self.assertNotIn("one-time note", body)
        self.assertIn("This is a sales email", body)
        self.assertNotIn("buy.stripe.com", body)
        self.assertIn("Pat Example", body)

    def test_no_website_lead_is_not_told_we_saw_its_website(self):
        lid = self.previewed(site_type="none", website=None, pitch={"presence": "a Facebook page"})
        _, body = h.render_email(h.cfg(), h.find(h.load(), lid), "outreach")
        self.assertNotIn("website and noticed", body)
        self.assertIn("couldn't find a website", body)

    def test_unsourced_observation_dropped(self):
        lid = self.previewed(pitch={"observation": "My family loves your food."})
        _, body = h.render_email(h.cfg(), h.find(h.load(), lid), "outreach")
        self.assertNotIn("loves your food", body)

    def test_preview_page(self):
        lid = self.add(tagline=None, menu_intro=None, hero_image="https://x.test/a.jpg",
                       reviews=[{"text": "great", "author": "someone"}])["id"]
        h.cmd_build(lid)
        html = next(h.SITES.glob("*/preview/index.html")).read_text()
        for bad in ("buy.stripe.com", "Make it yours", "Made fresh, every day", "made-from-scratch",
                    "&copy;", "x.test/a.jpg", "What guests say", "application/ld+json"):
            self.assertNotIn(bad, html)
        self.assertIn("noindex", html)
        self.assertIn("Not affiliated", html)

    def test_build_refuses_without_researched_content(self):
        lid = self.add(menu=None, hours=None)["id"]
        with self.assertRaises(SystemExit):
            h.cmd_build(lid)


if __name__ == "__main__":
    unittest.main()
