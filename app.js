/* ===========================
   FEEL GOOD FOODIE v3 — APP.JS
   =========================== */

const API_BASE = 'https://feel-good-foodie.onrender.com/api';

const MOOD_SUBLABELS = {
  happy:'Celebrate & enjoy', sad:'Comfort & warmth', stressed:'Calm & restore',
  energetic:'Power & fuel', romantic:'Love & indulge', tired:'Rest & revive',
  anxious:'Calm your mind', bored:'Fun & exciting', excited:'Celebrate!',
  sick:'Heal & recover', angry:'Cool down', motivated:'Power up!',
  nostalgic:'Classic flavors', lonely:'Warm & cozy'
};

let currentFoods = [];
let activeFilters = { diet: 'all', type: 'all' };

document.addEventListener('DOMContentLoaded', () => {
  loadMoods();
  document.getElementById('backBtn').addEventListener('click', showMoodPicker);
  document.getElementById('searchInput').addEventListener('input', handleSearch);
  detectTimeOfDay();
});

// ── Time of day greeting ──────────────────────────────────────────────────────
function detectTimeOfDay() {
  const hour = new Date().getHours();
  let greeting = '';
  if (hour >= 5 && hour < 12) greeting = '🌅 Good Morning! ';
  else if (hour >= 12 && hour < 17) greeting = '☀️ Good Afternoon! ';
  else if (hour >= 17 && hour < 21) greeting = '🌆 Good Evening! ';
  else greeting = '🌙 Good Night! ';
  const el = document.getElementById('timeGreeting');
  if (el) el.textContent = greeting + 'How are you feeling?';
}

// ── Load Moods ────────────────────────────────────────────────────────────────
async function loadMoods() {
  try {
    const res = await fetch(`${API_BASE}/moods`);
    const data = await res.json();
    renderMoodGrid(data.moods);
  } catch {
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
      <div class="mood-card-sub">${MOOD_SUBLABELS[mood.id] || ''}</div>`;
    card.addEventListener('click', () => getRecommendations(mood.id, mood.color));
    grid.appendChild(card);
  });
}

function renderFallbackMoods() {
  const fallback = [
    {id:'happy',emoji:'😄',label:'Happy',color:'#FFD700'},
    {id:'sad',emoji:'😢',label:'Sad',color:'#6B9BD2'},
    {id:'stressed',emoji:'😤',label:'Stressed',color:'#FF6B6B'},
    {id:'energetic',emoji:'⚡',label:'Energetic',color:'#FF9F1C'},
    {id:'romantic',emoji:'❤️',label:'Romantic',color:'#FF6B9D'},
    {id:'tired',emoji:'😴',label:'Tired',color:'#9B8EC4'},
    {id:'anxious',emoji:'😰',label:'Anxious',color:'#7EC8C8'},
    {id:'bored',emoji:'😑',label:'Bored',color:'#F4A261'},
    {id:'excited',emoji:'🤩',label:'Excited',color:'#FF6B35'},
    {id:'sick',emoji:'🤒',label:'Sick',color:'#90BE6D'},
    {id:'angry',emoji:'😠',label:'Angry',color:'#E63946'},
    {id:'motivated',emoji:'💪',label:'Motivated',color:'#2DC653'},
    {id:'nostalgic',emoji:'🥹',label:'Nostalgic',color:'#E9C46A'},
    {id:'lonely',emoji:'🥺',label:'Lonely',color:'#A8DADC'},
  ];
  renderMoodGrid(fallback);
}

// ── Get Recommendations ───────────────────────────────────────────────────────
async function getRecommendations(moodId, moodColor) {
  showLoading(true);
  try {
    const res = await fetch(`${API_BASE}/recommend`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({mood: moodId}),
    });
    if (!res.ok) throw new Error('API error');
    const data = await res.json();
    currentFoods = data.recommendations;
    activeFilters = {diet: 'all', type: 'all'};
    showResults(data, moodColor);
  } catch {
    showToast('⚠️ Could not connect to server.');
  } finally {
    showLoading(false);
  }
}

// ── Show Results ──────────────────────────────────────────────────────────────
function showResults(data, color) {
  document.getElementById('mood-picker').classList.add('hidden');
  document.getElementById('hero').classList.add('hidden');
  document.documentElement.style.setProperty('--mood-color', color);

  document.getElementById('moodBadge').textContent = data.emoji;
  document.getElementById('resultsTitle').textContent = `Perfect picks for your ${data.mood} mood`;
  document.getElementById('resultsTagline').textContent = data.tagline;
  document.getElementById('searchInput').value = '';

  // Reset filters UI
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  document.querySelector('.filter-btn[data-diet="all"]').classList.add('active');
  document.querySelector('.filter-btn[data-type="all"]').classList.add('active');

  renderCards(currentFoods);

  const section = document.getElementById('resultsSection');
  section.classList.remove('hidden');
  section.scrollIntoView({behavior: 'smooth', block: 'start'});
}

// ── Render Cards ──────────────────────────────────────────────────────────────
function renderCards(foods) {
  const grid = document.getElementById('cardsGrid');
  grid.innerHTML = '';

  if (foods.length === 0) {
    grid.innerHTML = `<div class="no-results">😕 No dishes found. Try a different filter!</div>`;
    return;
  }

  foods.forEach(food => {
    const card = document.createElement('div');
    card.className = 'food-card';
    card.innerHTML = `
      <div class="food-card-hero">${food.emoji}</div>
      <div class="food-card-body">
        <div class="food-card-top">
          <div class="food-card-name">${food.name}</div>
          <div class="food-type-badge ${food.is_veg ? 'veg' : 'nonveg'}">${food.is_veg ? '🟢 Veg' : '🔴 Non-veg'}</div>
        </div>
        <div class="food-stars">${renderStars(food.mood_score)}</div>
        <div class="food-card-desc">${food.description}</div>
        <div class="food-tags">
          ${food.tags.map(t => `<span class="food-tag">${t}</span>`).join('')}
          ${food.diet_type ? food.diet_type.map(d => `<span class="food-tag diet-tag">${d}</span>`).join('') : ''}
        </div>
        <div class="food-meta">
          <div class="meta-item"><span>🔥</span><span>${food.calories} cal</span></div>
          <div class="meta-item"><span>⏱️</span><span>${food.prep_time}</span></div>
          <div class="meta-item"><span>👨‍🍳</span><span>${food.difficulty}</span></div>
          <div class="meta-item"><span>🕐</span><span>${food.best_time}</span></div>
        </div>
        <div class="nutrition-bar">
          <div class="nutrition-item"><span class="n-label">Protein</span><div class="n-bar"><div class="n-fill protein" style="width:${food.nutrition.protein_pct}%"></div></div><span class="n-val">${food.nutrition.protein}g</span></div>
          <div class="nutrition-item"><span class="n-label">Carbs</span><div class="n-bar"><div class="n-fill carbs" style="width:${food.nutrition.carbs_pct}%"></div></div><span class="n-val">${food.nutrition.carbs}g</span></div>
          <div class="nutrition-item"><span class="n-label">Fats</span><div class="n-bar"><div class="n-fill fats" style="width:${food.nutrition.fats_pct}%"></div></div><span class="n-val">${food.nutrition.fats}g</span></div>
        </div>
        <div class="info-section benefits">
          <div class="info-title">💪 Benefits</div>
          <ul class="info-list">${food.benefits.map(b => `<li>${b}</li>`).join('')}</ul>
        </div>
        <div class="info-section avoid">
          <div class="info-title">⚠️ Avoid if</div>
          <ul class="info-list avoid-list">${food.avoid_if.map(a => `<li>${a}</li>`).join('')}</ul>
        </div>
        <button class="try-btn" onclick="handleTry('${food.name}')">I'll try this! 🍴</button>
      </div>`;
    grid.appendChild(card);
  });
}

function renderStars(score) {
  let s = '';
  for (let i = 1; i <= 5; i++) s += `<span class="star ${i <= score ? 'filled' : ''}">★</span>`;
  return s;
}

// ── Search ────────────────────────────────────────────────────────────────────
function handleSearch(e) {
  const q = e.target.value.toLowerCase().trim();
  let filtered = currentFoods;
  if (q) filtered = filtered.filter(f => f.name.toLowerCase().includes(q) || f.description.toLowerCase().includes(q) || f.tags.some(t => t.toLowerCase().includes(q)));
  filtered = applyFilters(filtered);
  renderCards(filtered);
}

// ── Filters ───────────────────────────────────────────────────────────────────
function setFilter(type, value, btn) {
  activeFilters[type] = value;
  document.querySelectorAll(`.filter-btn[data-${type}]`).forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  const q = document.getElementById('searchInput').value.toLowerCase().trim();
  let filtered = currentFoods;
  if (q) filtered = filtered.filter(f => f.name.toLowerCase().includes(q) || f.tags.some(t => t.toLowerCase().includes(q)));
  filtered = applyFilters(filtered);
  renderCards(filtered);
}

function applyFilters(foods) {
  return foods.filter(f => {
    const typeOk = activeFilters.type === 'all' || (activeFilters.type === 'veg' ? f.is_veg : !f.is_veg);
    const dietOk = activeFilters.diet === 'all' || (f.diet_type && f.diet_type.map(d => d.toLowerCase()).includes(activeFilters.diet));
    return typeOk && dietOk;
  });
}

// ── Surprise Me ───────────────────────────────────────────────────────────────
function surpriseMe() {
  const moods = Object.keys(MOOD_SUBLABELS);
  const random = moods[Math.floor(Math.random() * moods.length)];
  const colors = {happy:'#FFD700',sad:'#6B9BD2',stressed:'#FF6B6B',energetic:'#FF9F1C',romantic:'#FF6B9D',tired:'#9B8EC4',anxious:'#7EC8C8',bored:'#F4A261',excited:'#FF6B35',sick:'#90BE6D',angry:'#E63946',motivated:'#2DC653',nostalgic:'#E9C46A',lonely:'#A8DADC'};
  showToast(`🎲 Surprising you with ${random} mood!`);
  getRecommendations(random, colors[random]);
}

// ── Misc ──────────────────────────────────────────────────────────────────────
function showMoodPicker() {
  document.getElementById('resultsSection').classList.add('hidden');
  document.getElementById('mood-picker').classList.remove('hidden');
  document.getElementById('hero').classList.remove('hidden');
  document.getElementById('mood-picker').scrollIntoView({behavior: 'smooth'});
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
