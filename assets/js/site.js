// Mobile nav
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
}

// Tabs (Host page: gathering types)
document.querySelectorAll('.tabs').forEach((tabs) => {
  const buttons = tabs.querySelectorAll('[role="tab"]');
  buttons.forEach((btn) => {
    btn.addEventListener('click', () => {
      buttons.forEach((b) => {
        const on = b === btn;
        b.setAttribute('aria-selected', on);
        document.getElementById(b.getAttribute('aria-controls')).hidden = !on;
      });
    });
  });
});

// Tickers: repeat the items until one copy is wider than the screen, then
// double it so the -50% scroll loops with no gap. Speed stays the same
// however long the text is (about 60px a second).
function fillTickers() {
  document.querySelectorAll('.ticker__track').forEach((t) => {
    if (!t.dataset.base) t.dataset.base = t.innerHTML;
    t.innerHTML = t.dataset.base;
    const need = window.innerWidth + 200;
    let guard = 0;
    while (t.scrollWidth < need && guard++ < 50) t.innerHTML += t.dataset.base;
    const half = t.scrollWidth;
    t.innerHTML += t.innerHTML;
    t.style.animationDuration = (half / 60) + 's';
  });
}
fillTickers();
if (document.fonts) document.fonts.ready.then(fillTickers);
let tickerTimer;
window.addEventListener('resize', () => { clearTimeout(tickerTimer); tickerTimer = setTimeout(fillTickers, 200); });
