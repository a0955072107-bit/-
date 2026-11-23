// Polyglot Pages 後台：可以安裝成 App、離線也能開。先抓最新的，沒網路時用上次存的。
const CACHE = 'pp-admin-v1'
const SHELL = ['./', 'index.html', 'style.css', 'app.js', 'schedule.json', 'manifest.webmanifest', 'icon-192.png', 'icon-512.png', 'avatar-96.png']
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).catch(() => {}).then(() => self.skipWaiting()))
})
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim())
  )
})
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return
  e.respondWith(
    fetch(e.request)
      .then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(e.request, copy)) }
        return res
      })
      .catch(() => caches.match(e.request, { ignoreSearch: true }))
  )
})
