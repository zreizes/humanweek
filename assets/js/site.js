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

// Tickers: duplicate content so the scroll loops seamlessly
document.querySelectorAll('.ticker__track').forEach((t) => { t.innerHTML += t.innerHTML; });
