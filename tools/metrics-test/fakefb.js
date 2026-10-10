// A fake Firebase compat SDK for the metrics tests: app/auth/firestore with real merge + increment
// semantics, batches, every read and write logged by path, and switchable "rules not published".
// The store and log live in sessionStorage under __fake* keys so they survive navigation in one tab
// (one context = one device); __CLOUD_SEED seeds the server side once.
(function () {
  var LS = window.sessionStorage, get = Storage.prototype.getItem, setI = Storage.prototype.setItem;
  function load(k, d) { try { return JSON.parse(get.call(LS, k)) || d; } catch (e) { return d; } }
  var F = window.__FAKE = { store: load('__fakestore', null), ops: load('__fakeops', []), anon: +get.call(LS, '__fakeanon') || 0 };
  if (!F.store) { F.store = JSON.parse(JSON.stringify(window.__CLOUD_SEED || {})); }
  function persist() { setI.call(LS, '__fakestore', JSON.stringify(F.store)); setI.call(LS, '__fakeops', JSON.stringify(F.ops)); setI.call(LS, '__fakeanon', String(F.anon)); }
  persist();
  function denied(path) { var f = window.__FAIL_COLLS || load('__failcolls', []); return f.some(function (c) { return path.indexOf(c + '/') === 0; }); }
  function op(kind, path, n) { F.ops.push({ k: kind, p: path, n: n == null ? 1 : n, page: location.pathname.split('/').pop() }); persist(); }
  function INC(n) { this.n = n; }
  function applyData(path, d, merge) {
    var cur = merge ? JSON.parse(JSON.stringify(F.store[path] || {})) : {};
    Object.keys(d || {}).forEach(function (k) {
      var v = d[k];
      if (v instanceof INC) cur[k] = (typeof cur[k] === 'number' ? cur[k] : 0) + v.n;
      else cur[k] = v;
    });
    F.store[path] = cur;
  }
  function err() { var e = new Error('Missing or insufficient permissions.'); e.code = 'permission-denied'; return e; }
  function snapDoc(path) {
    var id = path.split('/').pop(), d = F.store[path];
    return { id: id, exists: d !== undefined, data: function () { return d === undefined ? undefined : JSON.parse(JSON.stringify(d)); }, ref: new DocRef(path) };
  }
  function children(path) {
    var pre = path + '/';
    return Object.keys(F.store).filter(function (p) { return p.indexOf(pre) === 0 && p.slice(pre.length).indexOf('/') < 0; });
  }
  function Query(path, filters) { this.path = path; this.filters = filters || []; }
  Query.prototype.where = function (f, o, v) { return new Query(this.path, this.filters.concat([[f, o, v]])); };
  Query.prototype.orderBy = function () { return this; };
  Query.prototype.limit = function () { return this; };
  Query.prototype.get = function () {
    var self = this;
    var docs = children(this.path).filter(function (p) {
      return self.filters.every(function (fl) {
        var v = (F.store[p] || {})[fl[0]];
        if (fl[1] === '>') return v > fl[2]; if (fl[1] === '>=') return v >= fl[2]; if (fl[1] === '==') return v === fl[2];
        return true;
      });
    }).map(snapDoc);
    op('read', this.path, Math.max(1, docs.length));
    return Promise.resolve({ docs: docs, size: docs.length, empty: !docs.length, forEach: function (cb) { docs.forEach(cb); } });
  };
  Query.prototype.onSnapshot = function (cb) { var self = this; setTimeout(function () { self.get().then(cb); }, 0); return function () {}; };
  function CollRef(path) { Query.call(this, path, []); }
  CollRef.prototype = Object.create(Query.prototype);
  CollRef.prototype.doc = function (id) { return new DocRef(this.path + '/' + (id || ('auto' + Math.random().toString(36).slice(2)))); };
  CollRef.prototype.add = function (d) { var r = this.doc(); return r.set(d).then(function () { return r; }); };
  function DocRef(path) { this.path = path; this.id = path.split('/').pop(); }
  DocRef.prototype.collection = function (n) { return new CollRef(this.path + '/' + n); };
  DocRef.prototype.set = function (d, o) {
    if (denied(this.path)) { op('denied', this.path); return Promise.reject(err()); }
    applyData(this.path, d, o && o.merge); op('write', this.path); return Promise.resolve();
  };
  DocRef.prototype.update = function (d) { return this.set(d, { merge: true }); };
  DocRef.prototype.delete = function () { delete F.store[this.path]; op('write', this.path); return Promise.resolve(); };
  DocRef.prototype.get = function () { op('read', this.path); return Promise.resolve(snapDoc(this.path)); };
  DocRef.prototype.onSnapshot = function (cb) { var self = this; setTimeout(function () { self.get().then(cb); }, 0); return function () {}; };
  var db = { collection: function (n) { return new CollRef(n); }, doc: function (p) { return new DocRef(p); },
    batch: function () {
      var items = [];
      return { set: function (r, d, o) { items.push([r, d, o]); return this; },
               update: function (r, d) { items.push([r, d, { merge: true }]); return this; },
               delete: function (r) { items.push([r, null, 'del']); return this; },
               commit: function () {
                 // all or nothing, like a real batch
                 if (items.some(function (it) { return denied(it[0].path); })) { items.forEach(function (it) { op('denied', it[0].path); }); return Promise.reject(err()); }
                 items.forEach(function (it) { if (it[2] === 'del') delete F.store[it[0].path]; else applyData(it[0].path, it[1], it[2] && it[2].merge); op('write', it[0].path); });
                 return Promise.resolve();
               } };
    },
    runTransaction: function (fn) { return fn({ get: function (r) { return r.get(); }, set: function (r, d) { r.set(d); }, update: function (r, d) { r.update(d); } }); },
    enablePersistence: function () { return Promise.resolve(); }, settings: function () {} };
  var listeners = [], user = window.__FAKE_USER || load('__fakeuser', null);
  function setUser(u) { user = u; setI.call(LS, '__fakeuser', JSON.stringify(u)); listeners.forEach(function (cb) { cb(user); }); }
  var auth = {
    get currentUser() { return user; },
    setPersistence: function () { return Promise.resolve(); },
    onAuthStateChanged: function (cb) { listeners.push(cb); setTimeout(function () { cb(user); }, 30); return function () {}; },
    signInWithPopup: function () { return Promise.resolve({ user: user }); },
    signInAnonymously: function () { F.anon++; persist(); if (!user) setUser({ uid: 'anon' + F.anon, isAnonymous: true }); return Promise.resolve({ user: user }); },
    signOut: function () { setUser(null); return Promise.resolve(); }
  };
  var fs = function () { return db; };
  fs.FieldValue = { serverTimestamp: function () { return Date.now(); }, increment: function (n) { return new INC(n); }, delete: function () { return null; },
                    arrayUnion: function () { return []; }, arrayRemove: function () { return []; } };
  fs.Timestamp = { now: function () { return { toMillis: function () { return Date.now(); } }; } };
  var au = function () { return auth; };
  au.Auth = { Persistence: { LOCAL: 'local', SESSION: 'session', NONE: 'none' } };
  au.GoogleAuthProvider = function () {};
  window.firebase = { apps: [], initializeApp: function (c) { this.apps.push(c); return {}; }, app: function () { return {}; }, auth: au, firestore: fs };
})();
