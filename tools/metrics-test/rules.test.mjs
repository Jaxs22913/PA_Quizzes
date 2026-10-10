// Rules tests against the Firestore emulator: every block of firestore.rules still behaves, and the
// metrics blocks accept only signed-in, listed-field, small-positive-increment writes and no reads.
import { initializeTestEnvironment, assertSucceeds, assertFails } from "@firebase/rules-unit-testing";
import { doc, setDoc, getDoc, deleteDoc, increment, collection, addDoc } from "firebase/firestore";
import fs from "fs";
const RULES = process.argv[2];
const env = await initializeTestEnvironment({ projectId: "demo-pa", firestore: { rules: fs.readFileSync(RULES, "utf8"), host: "127.0.0.1", port: 8085 } });
const anon = env.authenticatedContext("anon1", { firebase: { sign_in_provider: "anonymous" } }).firestore();
const google = env.authenticatedContext("g1", { email: "x@example.com", firebase: { sign_in_provider: "google.com" } }).firestore();
const nobody = env.unauthenticatedContext().firestore();
const pad = n => (n < 10 ? "0" : "") + n;
const day = (off = 0) => { const d = new Date(Date.now() + off * 864e5); return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); };
let pass = 0, fail = 0;
async function t(name, p, want) {
  try { await (want ? assertSucceeds(p) : assertFails(p)); pass++; }
  catch (e) { fail++; console.log("FAIL:", name, "-", String(e.message || e).slice(0, 160)); }
}
const M = "metrics_daily", T = day();
await t("anon creates today", setDoc(doc(anon, M, T), { q_answered: increment(30), quiz_done: increment(1), active_d: increment(1), active_w: increment(1), active_m: increment(1) }, { merge: true }), true);
await t("anon adds to today", setDoc(doc(anon, M, T), { q_answered: increment(5), active_d: increment(1), guide_open: increment(3) }, { merge: true }), true);
await t("google user adds", setDoc(doc(google, M, T), { cram_open: increment(2), arcade_session: increment(1), review_drill: increment(1), planner_day: increment(1), ref_open: increment(1) }, { merge: true }), true);
await t("signed-out write refused", setDoc(doc(nobody, M, T), { q_answered: increment(1) }, { merge: true }), false);
await t("unknown field refused", setDoc(doc(anon, M, T), { foo: increment(1) }, { merge: true }), false);
await t("text field refused", setDoc(doc(anon, M, T), { note: "hello" }, { merge: true }), false);
await t("q_answered +1001 refused", setDoc(doc(anon, M, T), { q_answered: increment(1001) }, { merge: true }), false);
await t("q_answered +1000 ok", setDoc(doc(anon, M, T), { q_answered: increment(1000) }, { merge: true }), true);
await t("active_d +2 refused", setDoc(doc(anon, M, T), { active_d: increment(2) }, { merge: true }), false);
await t("decrement refused", setDoc(doc(anon, M, T), { quiz_done: increment(-1) }, { merge: true }), false);
await t("zero-or-lower absolute refused", setDoc(doc(anon, M, T), { q_answered: 3 }, { merge: true }), false);
await t("string value refused", setDoc(doc(anon, M, T), { quiz_done: "9" }, { merge: true }), false);
await t("float increment refused", setDoc(doc(anon, M, T), { quiz_done: increment(0.5) }, { merge: true }), false);
await t("non-merge overwrite refused", setDoc(doc(anon, M, T), { q_answered: 2000 }), false);
await t("client read refused", getDoc(doc(anon, M, T)), false);
await t("signed-out read refused", getDoc(doc(nobody, M, T)), false);
await t("delete refused", deleteDoc(doc(anon, M, T)), false);
await t("30 days back ok", setDoc(doc(anon, M, day(-30)), { q_answered: increment(1) }, { merge: true }), true);
await t("40 days back refused", setDoc(doc(anon, M, day(-40)), { q_answered: increment(1) }, { merge: true }), false);
await t("tomorrow ok (time zones)", setDoc(doc(anon, M, day(1)), { q_answered: increment(1) }, { merge: true }), true);
await t("3 days ahead refused", setDoc(doc(anon, M, day(3)), { q_answered: increment(1) }, { merge: true }), false);
await t("garbage day id refused", setDoc(doc(anon, M, "hello"), { q_answered: increment(1) }, { merge: true }), false);
await t("month 13 refused", setDoc(doc(anon, M, "2026-13-01"), { q_answered: increment(1) }, { merge: true }), false);
await t("other collection name refused", setDoc(doc(anon, "metrics_weekly", T), { q_answered: increment(1) }, { merge: true }), false);
// the blocks that were already there still behave
await t("stats/global open write still ok", setDoc(doc(nobody, "stats", "global"), { questionsCompleted: increment(10) }, { merge: true }), true);
await t("stats/global open read still ok", getDoc(doc(nobody, "stats", "global")), true);
await t("stats_events create refused (retired)", addDoc(collection(nobody, "stats_events"), { n: 10, kind: "quiz-complete", path: "/x.html", session: "abc", at: new Date() }), false);
await t("stats_events read refused (retired)", getDoc(doc(nobody, "stats_events", "any")), false);
await t("answer_picks create still ok", setDoc(doc(nobody, "answer_picks", "q1"), { total: 1, opts: 4, c0: 1 }), true);
await t("own kv still ok", setDoc(doc(google, "users", "g1", "kv", "k"), { value: "v", updatedAt: 1 }), true);
await t("other kv refused", setDoc(doc(google, "users", "g2", "kv", "k"), { value: "v", updatedAt: 1 }), false);
await env.cleanup();
console.log(`${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
