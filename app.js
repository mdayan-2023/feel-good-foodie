/* ===========================
   FEEL GOOD FOODIE v2 — APP.JS
   =========================== */

const API_BASE = 'https://feel-good-foodie.onrender.com/api';

const MOOD_SUBLABELS = {
  happy:    'Celebrate & enjoy',
  sad:      'Comfort & warmth',
  stressed: 'Calm & restore',
  energetic:'Power & fuel',
  romantic: 'Love & indulge',
  tired:    'Rest & revive',
};

document.addEventListener('DOMContentLoaded', () => {
  loadMoods();
  document.getElementById('backBtn').addEventListener('click', showMoodPicker);
});

async function loadMoods() {
  try {
    const res = await fetch(`${API_BASE}/moods`);
    const data = await res.json();
    renderMoodGrid(data.moods);
  } catch (err) {
    renderFallbackMoods();
  }
}

function renderMoodGrid(moods) {
  const grid = document.getElementById('moodGrid');
  grid.innerHTML = '';
  moods.forEach(mood => {
    const card = document.createElement('div');
    card.className = 'mood-card';
    card.style.setProperty('--card-color', mood.color);
    card.innerHTML = `
      <span class="mood-emoji">${mood.emoji}</span>
      <div class="mood-label">${mood.label}</div>
      <div class="mood-card-sub">${MOOD_SUBLABELS[mood.id] || ''}</div>
    `;
    card.addEventListener('click', () => getRecommendations(mood.id, mood.color));
    grid.appendChild(card);
  });
}

function renderFallbackMoods() {
  const fallback = [
    { id: 'happy',    emoji: '😄', label: 'Happy',    color: '#FFD700' },
    { id: 'sad',      emoji: '😢', label: 'Sad',      color: '#6B9BD2' },
    { id: 'stressed', emoji: '😤', label: 'Stressed', color: '#FF6B6B' },
    { id: 'energetic',emoji: '⚡', label: 'Energetic',color: '#FF9F1C' },
    { id: 'romantic', emoji: '❤️', label: 'Romantic', color: '#FF6B9D' },
    { id: 'tired',    emoji: '😴', label: 'Tired',    color: '#9B8EC4' },
  ];
  renderMoodGrid(fallback);
}

async function getRecommendations(moodId, moodColor) {
  showLoading(true);
  try {
    const res = await fetch(`${API_BASE}/recommend`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mood: moodId }),
    });
    if (!res.ok) throw new Error('API error');
    const data = await res.json();
    showResults(data, moodColor);
  } catch (err) {
    showToast('⚠️ Could not connect to server. Check that Flask is running.');
  } finally {
    showLoading(false);
  }
}

function renderStars(score) {
  let stars = '';
  for (let i = 1; i <= 5; i++) {
    stars += `<span class="star ${i <= score ? 'filled' : ''}">★</span>`;
  }
  return stars;
}

function showResults(data, color) {
  document.getElementById('mood-picker').classList.add('hidden');
  document.getElementById('hero').classList.add('hidden');
  document.documentElement.style.setProperty('--mood-color', color);

  document.getElementById('moodBadge').textContent = data.emoji;
  document.getElementById('resultsTitle').textContent = `Perfect picks for your ${data.mood} mood`;
  document.getElementById('resultsTagline').textContent = data.tagline;

  const grid = document.getElementById('cardsGrid');
  grid.innerHTML = '';

  data.recommendations.forEach(food => {
    const card = document.createElement('div');
    card.className = 'food-card';
    card.innerHTML = `
      <div class="food-card-hero">${food.emoji}</div>
      <div class="food-card-body">
        <div class="food-card-name">${food.name}</div>
        <div class="food-stars">${renderStars(food.mood_score)}</div>
        <div class="food-card-desc">${food.description}</div>

        <div class="food-tags">
          ${food.tags.map(t => `<span class="food-tag">${t}</span>`).join('')}
        </div>

        <div class="food-meta">
          <div class="meta-item"><span>🔥</span><span>${food.calories} cal</span></div>
          <div class="meta-item"><span>⏱️</span><span>${food.prep_time}</span></div>
          <div class="meta-item"><span>👨‍🍳</span><span>${food.difficulty}</span></div>
          <div class="meta-item"><span>🕐</span><span>${food.best_time}</span></div>
        </div>

        <div class="info-section benefits">
          <div class="info-title">💪 Benefits</div>
          <ul class="info-list">
            ${food.benefits.map(b => `<li>${b}</li>`).join('')}
          </ul>
        </div>

        <div class="info-section avoid">
          <div class="info-title">⚠️ Avoid if</div>
          <ul class="info-list avoid-list">
            ${food.avoid_if.map(a => `<li>${a}</li>`).join('')}
          </ul>
        </div>

        <button class="try-btn" onclick="handleTry('${food.name}')">
          I'll try this! 🍴
        </button>
      </div>
    `;
    grid.appendChild(card);
  });

  const section = document.getElementById('resultsSection');
  section.classList.remove('hidden');
  section.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function showMoodPicker() {
  document.getElementById('resultsSection').classList.add('hidden');
  document.getElementById('mood-picker').classList.remove('hidden');
  document.getElementById('hero').classList.remove('hidden');
  document.getElementById('mood-picker').scrollIntoView({ behavior: 'smooth' });
}

function handleTry(foodName) {
  showToast(`🍴 Great choice! Enjoy your ${foodName}!`);
}

function showLoading(visible) {
  document.getElementById('loadingOverlay').classList.toggle('hidden', !visible);
}

let toastTimer;
function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.remove('hidden');
  requestAnimationFrame(() => toast.classList.add('show'));
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.classList.add('hidden'), 300);
  }, 3500);
}
