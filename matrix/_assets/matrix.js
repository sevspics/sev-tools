/* ============================================
   CONTENT MATRIX — SHARED JAVASCRIPT
   Handles view toggle, filtering, copy-to-clipboard
   Each matrix.html defines its own MATRIX_DATA, this file operates on it
   ============================================ */

(function () {
  'use strict';

  // ----- VIEW TOGGLE -----
  const toggleBtns = document.querySelectorAll('.view-toggle button');
  const body = document.body;

  function setView(mode) {
    body.classList.remove('view-client', 'view-internal');
    body.classList.add('view-' + mode);
    toggleBtns.forEach(b => b.classList.toggle('active', b.dataset.view === mode));
    try {
      const client = (window.MATRIX_DATA && window.MATRIX_DATA.client && window.MATRIX_DATA.client.slug) || 'default';
      localStorage.setItem('cm_view_' + client, mode);
    } catch (e) {}
  }

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', () => setView(btn.dataset.view));
  });

  try {
    const client = (window.MATRIX_DATA && window.MATRIX_DATA.client && window.MATRIX_DATA.client.slug) || 'default';
    const saved = localStorage.getItem('cm_view_' + client);
    if (saved) setView(saved);
  } catch (e) {}

  // ----- FILTERS -----
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cells = document.querySelectorAll('.concept-cell');

  const pillarMap = {
    'costs': 1, 'pain points': 2, 'success': 3,
    'comparisons': 4, 'best-of': 5, 'journey': 6
  };

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.textContent.trim().toLowerCase();

      if (filter.startsWith('all')) {
        cells.forEach(c => c.classList.remove('dimmed'));
        return;
      }
      if (filter === 'geo only') {
        cells.forEach(c => {
          const hasGeo = c.querySelector('.geo');
          c.classList.toggle('dimmed', !hasGeo);
        });
        return;
      }

      const targetPillar = pillarMap[filter];
      if (!targetPillar) return;

      cells.forEach(c => {
        const pillar = parseInt(c.dataset.pillar, 10);
        c.classList.toggle('dimmed', pillar !== targetPillar);
      });
    });
  });

  // ----- COPY TO CLIPBOARD -----
  window.copyConceptBrief = function (conceptId) {
    if (!window.MATRIX_DATA) return;
    const concept = window.MATRIX_DATA.concepts.find(c => c.id === conceptId);
    if (!concept) return;

    const pillar = window.MATRIX_DATA.pillars.find(p => p.id === concept.pillar);
    const format = window.MATRIX_DATA.formats.find(f => f.id === concept.format);
    const clientName = window.MATRIX_DATA.client.name;

    const brief = [
      clientName.toUpperCase() + ' \u2014 CONCEPT BRIEF',
      '',
      'Pillar: ' + (pillar ? pillar.name : ''),
      'Format: ' + (format ? format.name : ''),
      'Platform: ' + (concept.platform || ''),
      '',
      'TITLE: ' + concept.title,
      '',
      'HOOK (first 3 seconds):',
      concept.hook,
      '',
      'CORE IDEA:',
      concept.coreIdea,
      '',
      'WHY IT WORKS HERE:',
      concept.whyItWorks,
      '',
      'PRODUCTION NOTES:',
      concept.productionNotes,
      '',
      'GEO TAG: ' + (concept.geoTag || 'N/A')
    ].join('\n');

    navigator.clipboard.writeText(brief).then(() => {
      const toast = document.createElement('div');
      toast.textContent = 'Brief copied';
      toast.style.cssText = 'position:fixed;bottom:24px;right:24px;background:#6ee7b7;color:#0a0a0a;padding:12px 20px;font-family:"IBM Plex Mono",monospace;font-size:11px;text-transform:uppercase;letter-spacing:0.12em;font-weight:600;z-index:999;';
      document.body.appendChild(toast);
      setTimeout(() => toast.remove(), 2000);
    });
  };

  // ----- NOTES PERSISTENCE (INTERNAL ONLY) -----
  document.querySelectorAll('[data-note-key]').forEach(el => {
    const key = 'cm_note_' + el.dataset.noteKey;
    const saved = localStorage.getItem(key);
    if (saved) el.value = saved;
    el.addEventListener('input', () => {
      localStorage.setItem(key, el.value);
    });
  });

})();
