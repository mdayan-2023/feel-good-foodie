# 🍽️ Feel Good Foodie

> **Eat with your heart** — A mood-based food recommendation web application.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-feel--good--foodie-brightgreen)](https://feel-good-foodie-1.onrender.com)
[![Backend](https://img.shields.io/badge/Backend-Flask%20API-blue)](https://feel-good-foodie.onrender.com/api/health)
[![Made With](https://img.shields.io/badge/Made%20With-HTML%20CSS%20JS%20Python-orange)]()

---

## 🌐 Live Website

👉 **[https://feel-good-foodie-1.onrender.com](https://feel-good-foodie-1.onrender.com)**

---

## 📌 About the Project

**Feel Good Foodie** recommends the perfect food based on how you're feeling right now.

Select your mood → Get 4 curated food recommendations with:
- ⭐ Mood effectiveness star rating
- 🔥 Calories & prep time
- 💪 Health benefits
- ⚠️ Who should avoid it
- 🟢 Veg / 🔴 Non-veg label

---

## 😄 14 Mood Categories

| Mood | Theme | Mood | Theme |
|------|-------|------|-------|
| 😄 Happy | Celebratory foods | 😰 Anxious | Calming foods |
| 😢 Sad | Comfort foods | 😑 Bored | Fun & exciting |
| 😤 Stressed | Stress-relief foods | 🤩 Excited | Festive foods |
| ⚡ Energetic | Power foods | 🤒 Sick | Healing foods |
| ❤️ Romantic | Elegant foods | 😠 Angry | Cooling foods |
| 😴 Tired | Restorative foods | 💪 Motivated | Power foods |
| 🥹 Nostalgic | Classic Indian | 🥺 Lonely | Warm comfort |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3, Flask, Flask-CORS |
| API Style | REST API (JSON) |
| Fonts | Google Fonts (Playfair Display, DM Sans) |
| Deployment | Render.com (Free Tier) |
| Code Hosting | GitHub |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/mdayan-2023/feel-good-foodie.git
cd feel-good-foodie
```

### 2. Install Python dependencies
```bash
pip install flask flask-cors
```

### 3. Start Flask backend (Terminal 1)
```bash
python app.py
```

### 4. Start frontend server (Terminal 2)
```bash
python -m http.server 8080
```

### 5. Open in browser
```
http://localhost:8080
```

---

## 📁 Project Structure

```
feel-good-foodie/
├── app.py            ← Flask backend (REST API)
├── index.html        ← Frontend HTML structure
├── style.css         ← CSS design, animations, dark theme
├── app.js            ← JavaScript logic, API calls
├── requirements.txt  ← Python dependencies
└── Procfile          ← Render.com startup config
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Server health check |
| GET | `/api/moods` | Get all 14 moods |
| POST | `/api/recommend` | Get food recommendations for a mood |

### Example Request
```json
POST /api/recommend
{ "mood": "happy" }
```

### Example Response
```json
{
  "mood": "happy",
  "emoji": "😄",
  "color": "#FFD700",
  "tagline": "Celebrate your joy with vibrant flavors!",
  "recommendations": [...]
}
```

---

## ✨ Features

- 🎭 14 emotional mood categories
- 🍽️ 56 curated food recommendations
- ⭐ Mood effectiveness star rating
- 🔥 Calories, prep time, difficulty, best meal time
- 💪 Health benefits per dish
- ⚠️ Dietary warnings (Avoid If)
- 🟢🔴 Veg / Non-veg labels
- 🔍 Search dishes by name or ingredient
- 🥗 Diet filters (Vegan, High Protein, Low Carb)
- 🎲 Surprise Me button
- 🌙 Dark theme with animated UI
- 📱 Fully responsive (mobile friendly)
- 🌍 Deployed & accessible worldwide

---

## 👨‍💻 Developer

**Md Ayan Hussain**

---

## 📄 License

This project is open source and available for educational purposes.

---

*Made with ❤️ & good taste*
