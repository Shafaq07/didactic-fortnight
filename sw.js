// Network first, saved copy when offline
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
e.respondWith(fetch(e.request).then(r=>{if(r.ok){const c=r.clone();caches.open('v1').then(x=>x.put(e.request,c))}return r}).catch(()=>caches.match(e.request)))});
