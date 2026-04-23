/* ===========================
   FEEL GOOD FOODIE — APP.JS
   =========================== */

const API_BASE = 'http://localhost:5000/api';

// Mood sub-labels for the cards
const MOOD_SUBLABELS = {
  happy:    'Celebrate & enjoy',
  sad:      'Comfort & warmth',
  stressed: 'Calm & restore',
  energetic:'Power & fuel',
  romantic: 'Love & indulge',
  tired:    'Rest & revive',
};

// ─── Init ────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  loadMoods();
  document.getElementById('backBtn').addEventListener('click', showMoodPicker);
});

// ─── Load Moods from API ──────────────────────────────────────────────────────
async function loadMoods() {
  try {
    const res = await fetch(`${API_BASE}/moods`);
    const data = await res.json();
    renderMoodGrid(data.moods);
  } catch (err) {
    console.error('Could not load moods:', err);
    // Fallback: render static moods if API is unavailable
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

// ─── Get Recommendations ──────────────────────────────────────────────────────
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
    console.error('Recommendation error:', err);
    showToast('⚠️ Could not connect to server. Check that Flask is running on port 5000.');
  } finally {
    showLoading(false);
  }
}

// ─── Show Results ─────────────────────────────────────────────────────────────
function showResults(data, color) {
  // Hide mood section
  document.getElementById('mood-picker').classList.add('hidden');
  document.getElementById('hero').classList.add('hidden');

  // Update CSS mood color variable
  document.documentElement.style.setProperty('--mood-color', color);

  // Populate header
  document.getElementById('moodBadge').textContent = data.emoji;
  document.getElementById('resultsTitle').textContent = `Perfect picks for your ${data.mood} mood`;
  document.getElementById('resultsTagline').textContent = data.tagline;

  // Build food cards
  const grid = document.getElementById('cardsGrid');
  grid.innerHTML = '';
  data.recommendations.forEach(food => {
    const card = document.createElement('div');
    card.className = 'food-card';
    card.innerHTML = `
      <div class="food-card-hero">${food.emoji}</div>
      <div class="food-card-body">
        <div class="food-card-name">${food.name}</div>
        <div class="food-card-desc">${food.description}</div>
        <div class="food-tags">
          ${food.tags.map(t => `<span class="food-tag">${t}</span>`).join('')}
        </div>
        <div class="food-meta">
          <div class="meta-item"><span>🔥</span><span>${food.calories} cal</span></div>
          <div class="meta-item"><span>⏱️</span><span>${food.prep_time}</span></div>
        </div>
        <button class="try-btn" onclick="handleTry('${food.name}')">
          I'll try this! 🍴
        </button>
      </div>
    `;
    grid.appendChild(card);
  });

  // Show results section
  const section = document.getElementById('resultsSection');
  section.classList.remove('hidden');
  section.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ─── Back to Mood Picker ──────────────────────────────────────────────────────
function showMoodPicker() {
  document.getElementById('resultsSection').classList.add('hidden');
  document.getElementById('mood-picker').classList.remove('hidden');
  document.getElementById('hero').classList.remove('hidden');
  document.getElementById('mood-picker').scrollIntoView({ behavior: 'smooth' });
}

// ─── Try Button Handler ───────────────────────────────────────────────────────
function handleTry(foodName) {
  showToast(`🍴 Great choice! Enjoy your ${foodName}!`);
}

// ─── Loading Overlay ──────────────────────────────────────────────────────────
function showLoading(visible) {
  document.getElementById('loadingOverlay').classList.toggle('hidden', !visible);
}

// ─── Toast Notification ───────────────────────────────────────────────────────
let toastTimer;
function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.remove('hidden');
  // Trigger show
  requestAnimationFrame(() => toast.classList.add('show'));
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.classList.add('hidden'), 300);
  }, 3500);
}