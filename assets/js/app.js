/**
 * tools.ai — Client-Side Interactivity (Vanilla JS)
 * Handles live search, multi-select filtering, sorting, dark/light theme, and copy-to-clipboard.
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initCopyButtons();
  initDirectoryFilters();
});

/* Dark/Light Theme Toggle */
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  if (!toggleBtn) return;

  const currentTheme = localStorage.getItem('tools_ai_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
  updateThemeBtnText(toggleBtn, currentTheme);

  toggleBtn.addEventListener('click', () => {
    const activeTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = activeTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('tools_ai_theme', newTheme);
    updateThemeBtnText(toggleBtn, newTheme);
  });
}

function updateThemeBtnText(btn, theme) {
  btn.innerHTML = theme === 'dark'
    ? '<span>☀️</span> Light Mode'
    : '<span>🌙</span> Dark Mode';
}

/* Copy to Clipboard for Prompt & Code Snippets */
function initCopyButtons() {
  document.querySelectorAll('.btn-copy').forEach(btn => {
    btn.addEventListener('click', async () => {
      const targetId = btn.getAttribute('data-target');
      let textToCopy = '';

      if (targetId) {
        const targetEl = document.getElementById(targetId);
        if (targetEl) textToCopy = targetEl.innerText || targetEl.textContent;
      } else {
        const pre = btn.closest('.code-block-wrapper').querySelector('pre');
        if (pre) textToCopy = pre.innerText || pre.textContent;
      }

      if (!textToCopy) return;

      try {
        await navigator.clipboard.writeText(textToCopy);
        const originalText = btn.innerText;
        btn.innerText = 'Copied!';
        btn.style.borderColor = 'var(--accent-green)';
        setTimeout(() => {
          btn.innerText = originalText;
          btn.style.borderColor = '';
        }, 2000);
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
    });
  });
}

/* Dynamic Client-Side Directory Filtering & Search */
function initDirectoryFilters() {
  const searchInput = document.getElementById('search-input');
  const categoryFilter = document.getElementById('filter-category');
  const pricingFilter = document.getElementById('filter-pricing');
  const roleFilter = document.getElementById('filter-role');
  const platformFilter = document.getElementById('filter-platform');
  const sortSelect = document.getElementById('sort-select');
  const clearBtn = document.getElementById('clear-filters');
  const resultsCountEl = document.getElementById('results-count');
  const gridContainer = document.getElementById('tools-grid-container');

  // If there's no tools grid or tools data, exit
  if (!gridContainer || !window.TOOLS_DATA) return;

  const allTools = window.TOOLS_DATA;

  function applyFilters() {
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    const catValue = categoryFilter ? categoryFilter.value : 'all';
    const pricingValue = pricingFilter ? pricingFilter.value : 'all';
    const roleValue = roleFilter ? roleFilter.value : 'all';
    const platformValue = platformFilter ? platformFilter.value : 'all';
    const sortValue = sortSelect ? sortSelect.value : 'relevant';

    let filtered = allTools.filter(tool => {
      // Search Query
      if (query) {
        const matchName = tool.name.toLowerCase().includes(query);
        const matchMaker = tool.maker.toLowerCase().includes(query);
        const matchTagline = tool.tagline.toLowerCase().includes(query);
        const matchDef = (tool.definition || '').toLowerCase().includes(query);
        const matchCat = (tool.category || '').toLowerCase().includes(query);
        const matchFeatures = (tool.key_features || []).some(f => f.toLowerCase().includes(query));
        const matchRoles = (tool.who_uses_it || []).some(r => r.toLowerCase().includes(query));

        if (!matchName && !matchMaker && !matchTagline && !matchDef && !matchCat && !matchFeatures && !matchRoles) {
          return false;
        }
      }

      // Category
      if (catValue !== 'all' && tool.category !== catValue) {
        return false;
      }

      // Pricing
      if (pricingValue !== 'all') {
        if (pricingValue === 'free' && tool.pricing.model !== 'free') return false;
        if (pricingValue === 'freemium' && tool.pricing.model !== 'freemium') return false;
        if (pricingValue === 'paid' && tool.pricing.model !== 'paid' && tool.pricing.model !== 'commercial') return false;
        if (pricingValue === 'has_free_tier' && !tool.pricing.has_free_tier) return false;
      }

      // Role
      if (roleValue !== 'all') {
        const roleMatch = (tool.who_uses_it || []).some(r =>
          r.toLowerCase().replaceAll(' ', '_') === roleValue.toLowerCase() ||
          r.toLowerCase().includes(roleValue.toLowerCase())
        );
        if (!roleMatch) return false;
      }

      // Platform
      if (platformValue !== 'all') {
        const platformMatch = (tool.platform || []).some(p => p.toLowerCase() === platformValue.toLowerCase());
        if (!platformMatch) return false;
      }

      return true;
    });

    // Sorting
    if (sortValue === 'alpha') {
      filtered.sort((a, b) => a.name.localeCompare(b.name));
    } else if (sortValue === 'newest') {
      filtered.sort((a, b) => (parseInt(b.launched) || 0) - (parseInt(a.launched) || 0));
    }

    renderToolsGrid(filtered, gridContainer, resultsCountEl);
  }

  // Attach Event Listeners
  if (searchInput) searchInput.addEventListener('input', applyFilters);
  if (categoryFilter) categoryFilter.addEventListener('change', applyFilters);
  if (pricingFilter) pricingFilter.addEventListener('change', applyFilters);
  if (roleFilter) roleFilter.addEventListener('change', applyFilters);
  if (platformFilter) platformFilter.addEventListener('change', applyFilters);
  if (sortSelect) sortSelect.addEventListener('change', applyFilters);

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      if (searchInput) searchInput.value = '';
      if (categoryFilter) categoryFilter.value = 'all';
      if (pricingFilter) pricingFilter.value = 'all';
      if (roleFilter) roleFilter.value = 'all';
      if (platformFilter) platformFilter.value = 'all';
      if (sortSelect) sortSelect.value = 'relevant';
      applyFilters();
    });
  }

  // Initial render
  applyFilters();
}

function renderToolsGrid(tools, container, countEl) {
  if (countEl) {
    countEl.innerText = `${tools.length} tool${tools.length === 1 ? '' : 's'} found`;
  }

  if (tools.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <h3>No matching tools found</h3>
        <p>Try adjusting your search query or filters to find what you're looking for.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = tools.map(tool => renderToolCardHTML(tool)).join('');
}

function renderToolCardHTML(tool) {
  const initial = tool.name.charAt(0).toUpperCase();
  const pricingModel = tool.pricing ? tool.pricing.model : 'freemium';
  const pricingClass = pricingModel.toLowerCase();

  const categoryName = (window.CATEGORIES_MAP && window.CATEGORIES_MAP[tool.category])
    ? window.CATEGORIES_MAP[tool.category].name
    : tool.category.replace(/_/g, ' ');

  const categoryIcon = (window.CATEGORIES_MAP && window.CATEGORIES_MAP[tool.category])
    ? window.CATEGORIES_MAP[tool.category].icon
    : '⚡';

  const features = (tool.key_features || []).slice(0, 3).map(f => `<li>${f}</li>`).join('');
  const roles = (tool.who_uses_it || []).slice(0, 3).map(r => `<span class="role-pill">${r}</span>`).join('');

  return `
    <article class="tool-card">
      <div class="tool-card-header">
        <div class="tool-identity">
          <div class="tool-icon-fallback">${initial}</div>
          <div class="tool-title-group">
            <h3><a href="/tools/${tool.id}.html">${tool.name}</a></h3>
            <span class="tool-maker">by ${tool.maker}</span>
          </div>
        </div>
        <span class="pricing-badge ${pricingClass}">${pricingModel}</span>
      </div>

      <a href="/categories/${tool.category}.html" class="category-tag">
        <span>${categoryIcon}</span> ${categoryName}
      </a>

      <p class="tool-tagline">${tool.tagline}</p>

      <ul class="tool-features-preview">
        ${features}
      </ul>

      <div class="tool-card-footer">
        <div class="tool-roles-list">
          ${roles}
        </div>
        <a href="${tool.official_url}" target="_blank" rel="noopener noreferrer" class="btn-visit">
          Visit ↗
        </a>
      </div>
    </article>
  `;
}
