/* First-party click counter. No cookies, no storage, no third-party tracker.
   A tracked click (WhatsApp, phone, text, email, booking link, form submit) loads a tiny
   same-origin page /go/<type>/ in a hidden frame, so Cloudflare Web Analytics
   counts it as a visit to that path (its referrer is the page clicked from). */
(function () {
  'use strict';
  var TYPES = { whatsapp: 1, call: 1, text: 1, email: 1, book: 1, form: 1 };
  var last = {};
  function kind(el) {
    var t = el.getAttribute('data-track');
    if (t && TYPES[t]) return t;
    var h = el.getAttribute('href') || '';
    if (/^tel:/i.test(h)) return 'call';
    if (/^sms:/i.test(h)) return 'text';
    if (/^mailto:/i.test(h)) return 'email';
    if (/^https?:\/\/(wa\.me|wa\.link|api\.whatsapp\.com|(www\.)?whatsapp\.com\/send)/i.test(h)) return 'whatsapp';
    if (/^https?:\/\/book\.seattleconventionstays\.com/i.test(h)) return 'book';
    return null;
  }
  function ping(t, cb) {
    var now = Date.now();
    var done = false;
    function fin() { if (!done) { done = true; if (cb) cb(); } }
    if (!TYPES[t] || (last[t] && now - last[t] < 1500)) { fin(); return; }
    last[t] = now;
    var f = document.createElement('iframe');
    f.src = '/go/' + t + '/';
    f.title = 'analytics';
    f.setAttribute('aria-hidden', 'true');
    f.tabIndex = -1;
    f.style.cssText = 'position:absolute;width:1px;height:1px;border:0;left:-9999px;top:0;visibility:hidden';
    f.onload = function () { setTimeout(fin, 150); };
    setTimeout(fin, 900);
    setTimeout(function () { if (f.parentNode) f.parentNode.removeChild(f); }, 15000);
    (document.body || document.documentElement).appendChild(f);
  }
  window.cwaPing = ping;
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var t = kind(a);
    if (!t) return;
    var h = a.getAttribute('href') || '';
    var newTab = (a.getAttribute('target') || '').toLowerCase() === '_blank';
    var mod = e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey;
    if (newTab || mod || /^(tel|sms|mailto):/i.test(h) || e.defaultPrevented) { ping(t); return; }
    e.preventDefault();
    ping(t, function () { window.location.href = a.href; });
  });
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f || !f.getAttribute) return;
    var t = f.getAttribute('data-track') || 'form';
    if (t !== 'off') ping(t);
  }, true);
})();
