// Pip explains matching test: runs pip-window.js's own search functions (pulled out of the file by name) over
// pip/data/explain/ (run tools/build_pip_data.py first), so ranking can be tuned in seconds without a browser.
//   node tools/pip_explain_match.js [tools/pip_explain_questions.json] [--show <slug part>] [--out results.json]
//   node tools/pip_explain_match.js --debug "<question>" <folder slug>      (tokens, candidates, scores)
// Baselines 2026-10-09: tools/pip_explain_questions.json 219/220 get a card; tools/pip_explain_questions_v2.json
// (judged, 392 with targets) 86.9% first card = target, 79/80 no card when none fits.
const fs = require('fs'), path = require('path');
const REPO = path.join(__dirname, '..') + '/';
const src = fs.readFileSync(REPO + 'pip/pip-window.js', 'utf8');
function grab(name) {           // "function name(...) { ... }" with brace matching
  const i = src.indexOf('function ' + name + '(');
  if (i < 0) throw new Error('no function ' + name);
  let j = src.indexOf('{', i), d = 0;
  for (let k = j; k < src.length; k++) { if (src[k] === '{') d++; else if (src[k] === '}') { d--; if (!d) return src.slice(i, k + 1); } }
}
function grabVar(re) { const m = src.match(re); if (!m) throw new Error('no ' + re); return m[0]; }
const stopBlock = src.slice(src.indexOf('var STOP = {};'), src.indexOf('function norm('));
const code = [stopBlock, grabVar(/var CAPS = \{[^}]*\};/), grabVar(/var SYN = \{[^}]*\};/), grabVar(/var CASUAL = \[[\s\S]*?\]\];/), grabVar(/var ROMAN = \{[^}]*\};/), grabVar(/var WANTS = \[[\s\S]*?\]\];/), grabVar(/var KIND = \{[\s\S]*?\};/), grabVar(/var COMPARE = \/.*\/;/),
  ...['norm', 'stem', 'toks', 'casual', 'uniq', 'escRe', 'makeIndex', 'expandFor', 'abFor', 'near', 'spell', 'offGuide', 'rank', 'numbered', 'wants', 'kinds', 'explainHits', 'guideHits', 'guideLine'].map(grab),
  grabVar(/var GENERIC = \{\};[\s\S]*?GENERIC\[w\] = 1; \}\);/)].join('\n');
const gcache = {};
function guideIndex(f) { return Promise.resolve(gcache[f.s] || (gcache[f.s] = JSON.parse(fs.readFileSync(REPO + 'pip/data/guide/' + f.s + '.json', 'utf8')))); }
function decodedPath(p) { return p; }
const location = { pathname: '/x/none.html' };
const IX = JSON.parse(fs.readFileSync(REPO + 'pip/data/index.json', 'utf8'));
const cache = {};
function explainOf(f) {
  if (cache[f.s]) return Promise.resolve(cache[f.s]);
  const e = JSON.parse(fs.readFileSync(REPO + 'pip/data/explain/' + f.s + '.json', 'utf8'));
  // same preparation as pip-window.js explainOf()
  const prep = grab('explainOf').match(/if \(!e\._ix\) \{([\s\S]*?)\n      \}/)[1];
  new Function('e', 'makeIndex', 'numbered', 'toks', 'kinds', prep)(e, M.makeIndex, M.numbered, M.toks, M.kinds);
  return Promise.resolve(cache[f.s] = e);
}
const M = new Function('IX', 'explainOf', 'guideIndex', 'decodedPath', 'location', code + '\nreturn {norm, toks, casual, makeIndex, numbered, rank, expandFor, explainHits, guideHits, guideLine, kinds, wants};')(IX, explainOf, guideIndex, decodedPath, location);
if (process.argv[2] === '--debug') {
  (async () => {
    const f = IX.folders.find(x => x.s === process.argv[4]); const e = await explainOf(f);
    const q0 = M.casual(process.argv[3]); const q = M.numbered(M.expandFor(q0, e._ix)); const qt = [...new Set(M.toks(q))];
    console.log('query ->', q, '| tokens', qt);
    const r = M.rank(e._ix, e._texts, q, 8);
    console.log('rank (needs', qt.length <= 2 ? qt.length : Math.ceil(qt.length * 0.6), 'hits):'); r.forEach(x => console.log('  ', x[0].toFixed(2), e.cards[x[1]].t, '| names hit:', qt.filter(w => e._names[x[1]][w])));
    // which cards contain each token at all
    qt.forEach(w => console.log('   token', w, 'df', e._ix.df[w] || 0, '| in titles of:', e.cards.filter((c, i) => e._title[i][w]).map(c => c.t).slice(0, 4)));
    console.log('wants', JSON.stringify(M.wants(q0)), '| kinds of top:', r.slice(0, 6).map(x => e.cards[x[1]].id + ' ' + JSON.stringify(M.kinds(e.cards[x[1]].t))).join(' ; '));
    console.log('hits ->', (await M.explainHits(f, q0)).map(c => c.t));
    const g = await guideIndex(f);
    console.log('guide hits ->', (await M.guideHits([f], q0, null)).map(r => r.b[2].slice(0, 40) + ': ' + r.b[3].slice(0, 70)));
    if (g._ix) M.toks(q0).forEach(w => console.log('   guide df', w, g._ix.df[w] || 0));
  })(); return;
}
const Q = JSON.parse(fs.readFileSync(process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(__dirname, 'pip_explain_questions.json'), 'utf8')).questions;
const show = process.argv.includes('--show') ? process.argv[process.argv.indexOf('--show') + 1] : null;
(async () => {
  if (process.argv[2] === '--debug') return;
  let hit = 0;
  const out = [];
  for (const q of Q) {
    const f = IX.folders.find(x => x.s === q.slug);
    const qx = M.casual(q.q);
    const h = await M.explainHits(f, qx);
    if (h.length) hit++;
    const rec = { ...q, got: h.map(c => c.t), gotu: h.map(c => c.u), cards: h.map(c => ({ id: c.id, t: c.t, x: c.x })) };
    if (h.length) { const l = await M.guideLine(f, h[0], h.m, q.q); rec.line = l ? { heading: l.b[2], text: l.b[3] } : null; }
    else rec.guide = (await M.guideHits([f], qx, null)).map(r => ({ heading: r.b[2], text: r.b[3].slice(0, 300) }));
    out.push(rec);
    if (!show || q.slug.includes(show)) console.log(q.slug.slice(0, 12), '|', q.q.slice(0, 58).padEnd(58), '->', (h.map(c => c.t).join(' + ') || '-- none').slice(0, 100), (h[0] && q.u && h[0].u !== q.u) ? '   [unit ' + h[0].u + ' vs expected ' + q.u + ']' : '');
  }
  
  if (Q.length && Q[0].target) {           // a labeled set: score the first card against the judges' target
    let pos = 0, posOk = 0, neg = 0, negOk = 0; const bad = [];
    for (const o of out) {
      if (o.target.length) { pos++; if (o.cards[0] && o.target.includes(o.cards[0].id)) posOk++; else bad.push(o); }
      else { neg++; if (!o.cards.length) negOk++; else bad.push(o); }
    }
    console.log('labeled: first card is the target %d/%d (%s%%); no card when none fits %d/%d', posOk, pos, (100 * posOk / pos).toFixed(1), negOk, neg);
    if (process.argv.includes('--misses')) bad.forEach(o => console.log('   MISS', o.q.slice(0, 60).padEnd(60), '->', (o.cards[0] ? o.cards[0].id : 'none').padEnd(40), 'want', o.target[0] || 'none'));
  }
  if (process.argv.includes('--out')) fs.writeFileSync(process.argv[process.argv.indexOf('--out') + 1], JSON.stringify(out, null, 1));
  console.log('\nexplained', hit, 'of', Q.length, '| top card from the expected unit:', out.filter(o => o.gotu[0] && o.gotu[0] === o.u).length);
})();
