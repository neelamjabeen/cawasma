/* =========================================================
   CAWASMA — Main JavaScript
   ========================================================= */

// ── Navbar scroll effect ─────────────────────────────────── //
const mainNav = document.getElementById('mainNav');
if (mainNav) {
  window.addEventListener('scroll', () => {
    mainNav.style.background = window.scrollY > 30 ? 'rgba(15,13,10,0.98)' : '';
  }, { passive: true });
}

// ── Intersection Observer: fade-up animations ─────────────── //
const fadeEls = document.querySelectorAll(
  '.fade-up, .fade-up-1, .fade-up-2, .fade-up-3, .fade-up-4, .fade-up-5'
);

if (fadeEls.length && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  fadeEls.forEach(el => {
    // Init off-screen state (in case CSS animation is blocked)
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
  });
}

// ── Tooltip initialization ────────────────────────────────── //
document.addEventListener('DOMContentLoaded', () => {
  const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltips.forEach(el => new bootstrap.Tooltip(el));
});

// ── Copy-to-clipboard helper ──────────────────────────────── //
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    // Could trigger a toast here
    console.log('Copied:', text);
  });
}
