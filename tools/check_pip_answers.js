// Pip answers check: runs pip-window.js's own search functions (pulled out of the file by name, like
// tools/pip_explain_match.js) over pip/data/ (run tools/build_pip_data.py first) and checks which kind of
// answer each question gets, mirroring searchGuides()/show(). No browser, no model.
//   node tools/check_pip_answers.js            (the cases below; exit 1 if any fails)
//   node tools/check_pip_answers.js "<question>" <page exam slug>     (one question, verbose)
// A positive (a failure) looks like: "FAIL junctional rythm? -> none (want card)".
// Jaxon 2026-10-15: "junctional rythm?" dead-ended (misspelling under 6 letters never fixed), "What does
// iatrogenic mean" got a long card, "the one defining feature of each valvular disease" got another topic.
const fs = require('fs'), path = require('path');
const REPO = path.join(__dirname, '..') + '/';
const DATA = REPO + 'pip/data/';
const src = fs.readFileSync(process.env.PIP_SRC || REPO + 'pip/pip-window.js', 'utf8');
function grab(name) {
  const i = src.indexOf('function ' + name + '(');
  if (i < 0) throw new Error('no function ' + name);
  let d = 0;
  for (let k = src.indexOf('{', i); k < src.length; k++) { if (src[k] === '{') d++; else if (src[k] === '}') { d--; if (!d) return src.slice(i, k + 1); } }
}
function grabVar(re) { const m = src.match(re); if (!m) throw new Error('no ' + re); return m[0]; }
const code = [
  src.slice(src.indexOf('var STOP = {};'), src.indexOf('function norm(')),
  grabVar(/var CAPS = \{[^}]*\};/), grabVar(/var SYN = \{[^}]*\};/), grabVar(/var CASUAL = \[[\s\S]*?\]\];/),
  grabVar(/var ROMAN = \{[^}]*\};/), grabVar(/var WANTS = \[[\s\S]*?\]\];/), grabVar(/var KIND = \{[\s\S]*?\};/),
  grabVar(/var GENERIC = \{\};[\s\S]*?GENERIC\[w\] = 1; \}\);/), grabVar(/var COMPARE = [^\n]*/), grabVar(/var STAND = [^\n]*/), grabVar(/var COVER = [^;]*;/),
  grabVar(/var CMPW = \{\};[\s\S]*?CMPW\[w\] = 1; \}\);/), grabVar(/var FILL = \{\};[\s\S]*?FILL\[w\] = 1; \}\);/),
  grabVar(/var DEFQ = [^\n]*/), grabVar(/var SHORT_OF = [^;]*;/), grabVar(/var LOOKUP = [^\n]*/),
  ...['norm', 'stem', 'letterTerms', 'toks', 'casual', 'uniq', 'escRe', 'makeIndex', 'expandFor', 'abFor', 'near', 'spell', 'offGuide', 'rank',
      'numbered', 'wants', 'kinds', 'coverOf', 'explainHits', 'guideHits', 'sidesOf', 'pickBest', 'explainWide', 'wordAt', 'fixSpelling',
      'specific', 'examsFor', 'prepGuide', 'headOf', 'aboutTerm', 'defineTerm', 'ciRe', 'defPatterns', 'sentencesOf', 'findDefinition', 'titleNames',
      'listAsk', 'gatherList', 'wideHits', 'shareIn', 'fullCover', 'passCover', 'hasGuides', 'wantsExplanation', 'needsExplaining'].map(grab),
  grabVar(/var EXPLAIN = [^\n]*/)
].join('\n');
const IX = JSON.parse(fs.readFileSync(DATA + 'index.json', 'utf8'));
const J = {};
function getJSON(p) { return Promise.resolve(J[p] || (J[p] = JSON.parse(fs.readFileSync(DATA + p, 'utf8')))); }
const stubs = {
  IX, getJSON, index: () => Promise.resolve(IX), guideIndex: f => getJSON('guide/' + f.s + '.json'),
  abAll: () => getJSON('ab.json'), examDate: () => Promise.resolve(null), daysUntil: () => 1, PAST: {},
  decodedPath: p => p, location: { pathname: '/x/none.html' },
  words: () => getJSON('words.json').then(d => {
    if (d._W) return d._W;
    const w = d.w.split(' '), at = Object.create(null); w.forEach((x, i) => { at[x] = i; });
    return (d._W = { w, m: d.m.split(' ').map(x => parseInt(x, 16)), at });
  })
};
let M;
function explainOf(f) {
  if (!f || !f.ex) return Promise.resolve(null);
  return getJSON('explain/' + f.s + '.json').then(e => {
    e.cards.forEach(c => { c._f = f; c._m = e.m; });
    if (!e._ix) new Function('e', 'makeIndex', 'numbered', 'toks', 'kinds', grab('explainOf').match(/if \(!e\._ix\) \{([\s\S]*?)\n      \}/)[1])(e, M.makeIndex, M.numbered, M.toks, M.kinds);
    e.cards.forEach(c => { c._ix = e._ix; });
    return e;
  });
}
const names = Object.keys(stubs);
M = new Function(...names, 'explainOf', code + '\nreturn {norm, toks, casual, makeIndex, numbered, kinds, fixSpelling, examsFor, defineTerm, findDefinition, ' +
  'listAsk, gatherList, wideHits, explainWide, guideHits, titleNames, fullCover, passCover, hasGuides, wantsExplanation, SHORT_OF, STAND};')(...names.map(k => stubs[k]), explainOf);

// mirrors searchGuides()/show() in pip-window.js: the kind of answer and whether Claude's general part runs
async function plan(q, slug) {
  const f = IX.folders.find(x => x.s === slug); if (!f) throw new Error('no exam ' + slug);
  const fx = await M.fixSpelling(q), text = fx.text, qx = M.casual(text);
  const D = M.defineTerm(text), L = M.listAsk(text);
  let scope = await M.examsFor(qx, f);
  if (scope.indexOf(f) < 0 && M.hasGuides(f)) scope = scope.slice(0, 3).concat([f]);
  const r = { q, fixed: fx.fixed.map(p => p.join('->')).join(','), scope: scope.map(x => x.s) };
  if (L) { const lst = await M.gatherList(L, scope, f); if (lst) return Object.assign(r, { kind: 'list', n: lst.items.length, from: lst.f.s, first: lst.items[0].name + ': ' + lst.items[0].text.slice(0, 60), general: false }); }
  const sc = scope.filter(M.hasGuides);
  let [out, ex, dd] = await Promise.all([M.wideHits(f, scope, qx, f, text), M.explainWide(f, qx, text), D ? M.findDefinition(D.t, sc, f) : null]);
  if (D && ex.length && !M.titleNames(ex[0], D.t) && (!D.bare || (dd && dd.def))) ex = [];
  if (D && !ex.length && dd && ((dd.def && dd.def.strong) || (!dd.taught && (dd.def || !D.bare))))
    return Object.assign(r, { kind: 'definition', def: dd.def ? (dd.def.strong ? 'strong' : 'weak') + ': ' + (dd.def.gloss || dd.def.s).slice(0, 80) : 'none', mentions: dd.mentions.length, general: !dd.def || !dd.def.strong });
  if (ex.length && !ex.cmp && M.fullCover(ex, text, true) < 0.5) ex = [];
  if (ex.cross) { const xf = ex.map(x => x._f); out = out.filter(o => xf.indexOf(o.f) >= 0); }
  // Claude writes the short answer (mode "answer") unless a comparison has a card per side (its dissection)
  const dissect = !ex.cmp && (ex.length >= 2 || (ex.length && !ex.cross && M.STAND.test(M.norm(text))));
  r.claude = !dissect && !!(ex.length || out.length) && !!(M.wantsExplanation(text) || D);
  if (ex.length) return Object.assign(r, { kind: 'card', card: ex.map(c => c.t).join(' | '), from: ex[0]._f.s, general: M.fullCover(ex, text) < M.SHORT_OF && M.wantsExplanation(text) });
  if (out.length) return Object.assign(r, { kind: 'passages', top: (out[0].b[2] || '') + ': ' + out[0].b[3].slice(0, 60), cov: +M.passCover(out, text).toFixed(2), general: M.passCover(out, text) < M.SHORT_OF && M.wantsExplanation(text) });
  return Object.assign(r, { kind: 'none', general: !!(M.wantsExplanation(text) || D) });
}

const PDM3 = 'principles-of-diagnostic-medicine-i-exam-3', CMS4 = 'clinical-medicine-and-surgery-i-exam-4';
// [question, page exam, want kind, a regex the answer must match (card title, list item, definition), want general?]
const CASES = [
  ['junctional rythm?', PDM3, 'card', /junctional/i, false],
  ['What does iatrogenic mean', CMS4, 'definition', /caused by treatment|medical/i, false],
  ['Can you give me the one defining feature of each valvular disease', CMS4, 'list', /Aortic stenosis: harsh systolic/i, false],
  ['what is the defining feature of each valvular disease', PDM3, 'list', /stenosis/i, false],
  ['junctional rhythm', PDM3, 'card', /junctional/i, false],
  ['What is wenckebach', PDM3, 'card', /wenckebach|mobitz|second.degree/i, false],
  ['PVC vs SVT', CMS4, 'card', /premature ventricular|supraventricular/i, false],
  ['What does photosynthesis mean', CMS4, 'definition', /none/, true],
  ['how does primary vs secondary hypertension differ', CMS4, 'card', /hypertension/i, false],
  ['what is takotsubo', CMS4, null, /./, null],
  ['why does aortic stenosis cause syncope during pregnancy', CMS4, 'card', /aortic stenosis/i, true],
  ['iatrogenic', CMS4, 'definition', /caused by treatment/i, false],
  ['where is the murmur chart', CMS4, null, /./, false],
  ['what is selective toxicity', 'microbiology-exam-1', 'definition', /kills harmful microbes/i, false],
  // Jaxon 2026-10-15 (his thumbs-down): one-letter waves were dropped, so "wave" alone found an infarct card
  ["What's the difference between a T and P wave?", CMS4, 'card', /^The J point, ST segment, T wave.*\| The P wave and the PR interval/, false],
  ["What's the difference between a T and P wave?", PDM3, 'card', /^The J point, ST segment, T wave.*\| The P wave and the PR interval/, false],
  ['difference between aortic and mitral stenosis', CMS4, 'card', /^Aortic stenosis.*\| Mitral stenosis/, false],
  ['what is a P wave', CMS4, 'card', /^The P wave and the PR interval$/, false],
];
(async () => {
  if (process.argv[2] === '--rate') {             // how often each kind of answer and the general part come up
    const qs = JSON.parse(fs.readFileSync(process.argv[3] || REPO + 'tools/pip_explain_questions.json', 'utf8')).questions;
    const n = {}; let gen = 0;
    for (const x of qs) { const p = await plan(x.q, x.slug); n[p.kind] = (n[p.kind] || 0) + 1; if (p.general) gen++;
      if (process.argv.includes('--show') && (p.general || p.kind === 'definition' || p.kind === 'list')) console.log('  ' + p.kind + (p.general ? '+general' : '') + ': ' + x.q + ' -> ' + (p.card || p.top || p.def || p.first || '').slice(0, 90)); }
    console.log(qs.length + ' questions:', JSON.stringify(n), '| general part:', gen, '(' + Math.round(100 * gen / qs.length) + '%)');
    return;
  }
  if (process.argv[2]) { console.log(await plan(process.argv[2], process.argv[3] || CMS4)); return; }
  let bad = 0;
  for (const [q, slug, kind, re, gen] of CASES) {
    const p = await plan(q, slug);
    const txt = [p.card, p.first, p.def, p.top].filter(Boolean).join(' ');
    const ok = (!kind || p.kind === kind) && re.test(txt || 'none') && (gen === null || p.general === gen);
    if (!ok) bad++;
    console.log((ok ? 'ok   ' : 'FAIL ') + q + ' -> ' + p.kind + (p.fixed ? ' [' + p.fixed + ']' : '') + ' | ' + (txt || '').slice(0, 110) + (p.general ? ' | +general' : '') +
      (ok ? '' : '  (want ' + kind + ' ' + re + (gen === null ? '' : ' general=' + gen) + ')'));
  }
  console.log(bad ? bad + ' of ' + CASES.length + ' failed' : 'all ' + CASES.length + ' passed');
  process.exit(bad ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
