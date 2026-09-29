#!/usr/bin/env node
/* Unit tests for planner-engine.js against the real academic calendar.
   Run: node tools/test_planner.js   (exits non-zero on any failure) */
const fs = require("fs"), vm = require("vm"), path = require("path");
const ROOT = path.join(__dirname, "..");
const E = require(path.join(ROOT, "planner-engine.js"));
const ctx = { window: {} }; vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, "calendar-data.js"), "utf8"), ctx);
const EV = ctx.window.CalendarData.all;
let fails = 0, n = 0;
function ok(c, msg) { n++; if (!c) { fails++; console.log("FAIL:", msg); } }
function eq(a, b, msg) { ok(JSON.stringify(a) === JSON.stringify(b), msg + "  got " + JSON.stringify(a) + " want " + JSON.stringify(b)); }
const sum = a => a.reduce((x, y) => x + y.minutes, 0);

/* --- coverage parsing --- */
eq(E.parseCoverage("CMS I - EXAM # 2 (Lectures 4-8)"), { lec: [4,5,6,7,8], lab: [] }, "range");
eq(E.parseCoverage("X (Lectures 7-10 and Lab 2)"), { lec: [7,8,9,10], lab: [2] }, "lecs+lab");
eq(E.parseCoverage("X - OSCE"), { lec: [], lab: [] }, "none");
eq(E.parseCoverage("PD II Exam #2 (#5-7)"), { lec: [5,6,7], lab: [] }, "hash range");


/* --- retests: planned only for the ones the student says they have to take --- */
{
  const today = "2026-09-28", none = E.deriveExams(EV, today, E.settingsWith({}));
  ok(none.every(x => !x.retest), "no retest is planned by default");
  const rts = EV.filter(e => (e.k === "retest" || e.k === "remediation") && e.c && e.d >= today);
  ok(rts.length > 3, "the calendar has retests to pick from");
  const one = rts.find(e => /Cardiology Block Exam I$/.test(e.t)), id1 = E.examId(one);
  const picked = E.deriveExams(EV, today, E.settingsWith({ retests: { [id1]: true } }));
  eq(picked.filter(x => x.retest).map(x => x.id), [id1], "exactly the ticked retest is planned");
  eq(picked.filter(x => !x.retest).length, none.length, "regular exams are unchanged");
  const all = E.deriveExams(EV, today, E.settingsWith({ planRetests: true }));
  eq(all.filter(x => x.retest).length, rts.length, "legacy planRetests still plans every retest");
  eq(new Set(rts.map(E.examId)).size, rts.length, "retest ids are unique");
}
/* --- every real exam, several 'today's --- */
const days = ["2026-09-28", "2026-10-06", "2026-10-20", "2026-11-05"];
days.forEach(today => {
  [{}, { planRetests: true }, { startWeeks: 8, hoursPerLecture: 3 }, { rampPower: 3, finalWeekShare: 0.6 }].forEach(over => {
    const cfg = E.settingsWith(over), ex = E.deriveExams(EV, today, cfg);
    const p = E.plan(ex, today, cfg, {}, {}, {}, {}, null, today);
    const exById = {}; ex.forEach(x => exById[x.id] = x);
    Object.keys(p.days).forEach(d => {
      const ts = p.days[d], w = E.windowOf(d, cfg, null, false), cap = E.capOf(w, cfg);
      ok(sum(ts) <= cap + 1, `${today} cap ${d} ${sum(ts)}>${cap}`);
      if (!w) ok(ts.length === 0, `${today} rest day ${d} has tasks`);
      ts.forEach(t => {
        const x = exById[t.exam];
        ok(d < x.d, `${today} task on/after exam ${d} >= ${x.d}`);
        ok(d >= today, `${today} task in the past ${d}`);
        t.units.forEach(u => { const src = x.units.find(v => v.kind === u.kind && v.n === u.n); if (src) ok(d >= src.date, `${today} ${x.t} ${u.kind}${u.n} scheduled ${d} before delivery ${src.date}`); });
        ok(t.start >= w.start && t.end <= w.end + 1, `${today} timeline outside window ${d} ${t.start}-${t.end} vs ${w.start}-${w.end}`);
        ok(t.minutes >= 5, "tiny task");
      });
      // tasks do not overlap
      for (let i = 1; i < ts.length; i++) ok(ts[i].start >= ts[i - 1].end, `overlap ${d}`);
    });
  });
});

/* --- availability: content that arrives later cannot be studied earlier --- */
{
  const today = "2026-09-28", cfg = E.settingsWith(), ex = E.deriveExams(EV, today, cfg);
  const pdm3 = ex.find(x => x.c === "pdm-1" && x.num === 3);
  ok(pdm3 && pdm3.units.some(u => u.date > today), "PDM exam 3 has undelivered lectures");
  const p = E.plan(ex, today, cfg, {}, {}, {}, {}, null, today);
  const first = Object.keys(p.days).find(d => p.days[d].some(t => t.exam === pdm3.id));
  const earliest = pdm3.units.map(u => u.date).sort()[0];
  ok(first >= earliest, `PDM3 first study ${first} before first lecture ${earliest}`);
}

/* --- the ramp: one exam, everything delivered, weekly minutes never fall until the taper --- */
{
  const cfg = E.settingsWith({ win: Array(7).fill({ on: true, start: 960, end: 1320 }), dayMax: 480 });
  const x = { id: "T", d: "2026-11-30", t: "T Exam", c: "pharm-1", kind: "exam", name: "T", num: 1, retest: false, practical: false, osce: false,
              units: [1,2,3,4,5,6,7,8].map(n => ({ kind: "lec", n, date: "2026-08-20" })) };
  const p = E.plan([x], "2026-10-05", cfg, {}, {}, {}, {}, null, "2026-10-05");
  const wk = []; for (let w = 0; w < 7; w++) { let t = 0; E.range(E.add("2026-10-05", 7 * w), E.add("2026-10-05", 7 * w + 6)).forEach(d => t += sum(p.days[d] || [])); wk.push(t); }
  ok(wk[0] < wk[wk.length - 1], `ramp: first week ${wk[0]} should be lighter than last ${wk[wk.length - 1]}`);
  ok(wk[wk.length - 1] > wk[Math.floor(wk.length / 2)] * 0.9, "ramp: last week is at least as heavy as middle");
  ok(sum(p.days["2026-11-29"]) <= cfg.taperLastDayMin + 5, "taper: day before is light");
  const total = Object.keys(p.days).reduce((a, d) => a + sum(p.days[d]), 0);
  ok(Math.abs(total - E.examHours(x, cfg) * 60) < 120, `total ${total} ~ ${E.examHours(x, cfg) * 60}`);
}

/* --- start/quit window drives capacity --- */
{
  const a = E.settingsWith({ win: Array(7).fill({ on: true, start: 1080, end: 1260 }) }), b = E.settingsWith({ win: Array(7).fill({ on: true, start: 1080, end: 1380 }) });
  ok(E.capOf(E.windowOf("2026-10-05", b, null, false), b) > E.capOf(E.windowOf("2026-10-05", a, null, false), a), "later quit time = more capacity");
  const w = E.windowOf("2026-10-05", a, 1200, true);
  eq(w, { start: 1200, end: 1260 }, "today's window starts at 'now' when it is inside the window");
  eq(E.windowOf("2026-10-05", a, 1255, true), null, "no window left late in the evening");
  eq(E.windowOf("2026-10-05", a, 900, true), { start: 1080, end: 1260 }, "before the start time the full window is available");
}

/* --- per-exam overrides --- */
{
  const today = "2026-09-28", cfg = E.settingsWith(), ex = E.deriveExams(EV, today, cfg), x = ex.find(e => e.c === "cms-1" && e.num === 4);
  const p1 = E.plan(ex, today, cfg, {}, {}, {}, {}, null, today), p2 = E.plan(ex, today, cfg, { [x.id]: { off: true } }, {}, {}, {}, null, today);
  const tot = (p, id) => Object.keys(p.days).reduce((a, d) => a + sum(p.days[d].filter(t => t.exam === id)), 0);
  ok(tot(p1, x.id) > 0 && tot(p2, x.id) === 0, "exam can be switched off");
  const p3 = E.plan(ex, today, cfg, { [x.id]: { hours: 2 } }, {}, {}, {}, null, today);
  ok(tot(p3, x.id) <= 125, "hours override respected");
  const p4 = E.plan(ex, today, cfg, { [x.id]: { start: "2026-10-08" } }, {}, {}, {}, null, today);
  const firstD = Object.keys(p4.days).find(d => p4.days[d].some(t => t.exam === x.id));
  ok(firstD >= "2026-10-08" || firstD > today, `start override first study ${firstD}`);
}

/* --- done work reduces what remains; missed work comes back as catch-up --- */
{
  const today = "2026-10-06", cfg = E.settingsWith(), ex = E.deriveExams(EV, today, cfg), x = ex.find(e => e.c === "pharm-1");
  const tot = p => Object.keys(p.days).reduce((a, d) => a + sum(p.days[d].filter(t => t.exam === x.id)), 0);
  const p0 = E.plan(ex, today, cfg, {}, {}, {}, {}, null, "2026-09-01"), p1 = E.plan(ex, today, cfg, {}, { [x.id]: 300 }, {}, {}, null, "2026-09-01");
  ok(tot(p1) < tot(p0), "completed minutes shrink the remaining plan");
  ok(p0.info[x.id].behindMin >= 0, "info present");
}

/* --- streak replay --- */
{
  const T = (done, custom) => ({ done, minutes: 30, custom: !!custom });
  const mk = spec => { const o = {}; Object.keys(spec).forEach(d => o[d] = spec[d]); return o; };
  // 5 finished days -> a freeze; a miss spends it; the streak survives
  let d = {}; ["01","02","03","04","05"].forEach(x => d["2026-10-" + x] = { tasks: [T(true)] });
  d["2026-10-06"] = { tasks: [T(false)] }; d["2026-10-07"] = { tasks: [T(true)] };
  let s = E.replayStreak(d, "2026-10-08");
  eq([s.streak, s.freezes, s.frozen.length, s.best], [6, 0, 1, 6], "freeze earned after 5, spent on a miss");
  // miss with no freeze breaks it
  d = { "2026-10-01": { tasks: [T(true)] }, "2026-10-02": { tasks: [T(false)] }, "2026-10-03": { tasks: [T(true)] } };
  s = E.replayStreak(d, "2026-10-04"); eq([s.streak, s.best, s.broken.length], [1, 1, 1], "miss without a freeze resets");
  // rest days and days off are neutral
  d = { "2026-10-01": { tasks: [T(true)] }, "2026-10-02": { tasks: [] }, "2026-10-03": { off: true, tasks: [T(false)] }, "2026-10-04": { tasks: [T(true)] } };
  s = E.replayStreak(d, "2026-10-05"); eq(s.streak, 2, "rest and off days neutral");
  // today unfinished does not break or freeze
  d = { "2026-10-01": { tasks: [T(true)] }, "2026-10-02": { tasks: [T(false)] } };
  s = E.replayStreak(d, "2026-10-02"); eq([s.streak, s.todayPlanned, s.todayDone], [1, true, false], "today in progress");
  // custom tasks never count
  d = { "2026-10-01": { tasks: [T(false, true)] } }; s = E.replayStreak(d, "2026-10-02"); eq(s.streak, 0, "custom tasks are not planned work");
  // freezes cap at 2
  d = {}; for (let i = 1; i <= 12; i++) d["2026-10-" + (i < 10 ? "0" : "") + i] = { tasks: [T(true)] };
  s = E.replayStreak(d, "2026-10-13"); eq([s.streak, s.freezes], [12, 2], "freezes capped at 2");
  // deterministic
  eq(E.replayStreak(d, "2026-10-13"), s, "replay is deterministic");
}

/* --- crunch detection --- */
{
  const ex = E.deriveExams(EV, "2026-09-28", E.settingsWith()), cr = E.crunches(ex, 5, 3);
  ok(cr.length >= 1 && cr[0].count >= 3, "crunch detected in early October");
}

console.log(`${n - fails}/${n} checks passed`);
process.exit(fails ? 1 : 0);
