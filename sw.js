const CACHE_NAME = "pa-quizzes-v1";

/* Precache list, added 2026-07-28. Deliberately tiny: this SW is otherwise
   network-first with runtime caching precisely so there is no big upfront
   list to maintain, and that stays true. The rain recording is the one asset
   that has to be here, because it is the only thing on the site whose whole
   point is working when you are offline and unwinding, and it is fetched
   lazily by relax.html -- so without this it would only be cached AFTER you
   had already played it online at least once, which is exactly backwards. */
const PRECACHE = ["audio/rain-on-window.ogg"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      // addAll() is all-or-nothing; a single failure would reject the whole
      // install. Cached individually and swallowed so a flaky connection
      // during install can never leave the site without a service worker.
      .then((cache) => Promise.all(
        PRECACHE.map((u) => cache.add(u).catch(() => {}))
      ))
      .catch(() => {})
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  /* Audio is cache-FIRST, unlike everything else. These files are immutable
     and large; the default network-first path would re-download 1.2MB from
     the network every time Rain is selected, even though the copy on disk is
     always correct. Falls through to the network if it is not cached yet. */
  if (url.pathname.includes("/audio/")) {
    event.respondWith(
      caches.match(req).then((hit) => hit || fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((c) => c.put(req, copy)).catch(() => {});
        return res;
      }))
    );
    return;
  }

  // Everything else: network-first, falling back to cache when offline. Every
  // successful online fetch refreshes the cache, so previously-visited
  // pages/images stay usable offline without a big upfront precache list.
  event.respondWith(
    fetch(req, { cache: "no-store" })
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(req, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(req))
  );
});
