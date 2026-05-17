from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOOD_FOODS = {
  "happy": {
    "emoji": "😄",
    "color": "#FFD700",
    "tagline": "Celebrate your joy with vibrant Indian flavors!",
    "foods": [
      {
        "name": "Mango Lassi",
        "description": "Thick yogurt blended with Alphonso mango and cardamom.",
        "emoji": "🥭",
        "tags": [
          "Sweet",
          "Creamy"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 32,
          "fats": 3,
          "protein_pct": 25,
          "carbs_pct": 70,
          "fats_pct": 15
        },
        "benefits": [
          "Probiotics improve gut",
          "Mango rich Vitamin A",
          "Cooling in summer",
          "Calcium for bones"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Pani Puri",
        "description": "Crispy puris filled with tangy tamarind water and chickpeas.",
        "emoji": "🫙",
        "tags": [
          "Tangy",
          "Fun"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 150,
        "prep_time": "15 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 28,
          "fats": 3,
          "protein_pct": 20,
          "carbs_pct": 80,
          "fats_pct": 15
        },
        "benefits": [
          "Chickpeas give protein",
          "Tamarind aids digestion",
          "Mint cooling",
          "Low calorie"
        ],
        "avoid_if": [
          "Acid reflux",
          "Stomach infection"
        ]
      },
      {
        "name": "Chole Bhature",
        "description": "Fluffy fried bread with spicy Punjabi chickpea curry.",
        "emoji": "🫓",
        "tags": [
          "Spicy",
          "Festive"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 520,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 14,
          "carbs": 70,
          "fats": 18,
          "protein_pct": 35,
          "carbs_pct": 88,
          "fats_pct": 50
        },
        "benefits": [
          "Chickpeas rich protein",
          "Iron from chole",
          "Energy-boosting carbs",
          "Mood-lifting"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High BP"
        ]
      },
      {
        "name": "Gulab Jamun",
        "description": "Soft milk-solid dumplings soaked in rose cardamom syrup.",
        "emoji": "🍮",
        "tags": [
          "Sweet",
          "Soft"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 350,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 58,
          "fats": 12,
          "protein_pct": 15,
          "carbs_pct": 90,
          "fats_pct": 38
        },
        "benefits": [
          "Serotonin from sweetness",
          "Rose water calming",
          "Calcium from milk",
          "Instant mood lifter"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Vada Pav",
        "description": "Mumbai soul food - potato vada in pav with garlic chutney.",
        "emoji": "🍔",
        "tags": [
          "Spicy",
          "Street Food"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 290,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 48,
          "fats": 10,
          "protein_pct": 15,
          "carbs_pct": 85,
          "fats_pct": 30
        },
        "benefits": [
          "Quick energy",
          "Spices boost immunity",
          "Street food happiness",
          "Satisfying"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High BP"
        ]
      },
      {
        "name": "Samosa",
        "description": "Crispy triangular pastry filled with spiced potatoes and peas.",
        "emoji": "🔺",
        "tags": [
          "Crispy",
          "Spicy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 250,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 35,
          "fats": 12,
          "protein_pct": 14,
          "carbs_pct": 78,
          "fats_pct": 38
        },
        "benefits": [
          "Peas provide protein",
          "Spices aid digestion",
          "Comfort food happiness",
          "Satisfying"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Jalebi",
        "description": "Crispy spiral sweets soaked in saffron sugar syrup.",
        "emoji": "🌀",
        "tags": [
          "Sweet",
          "Crispy"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 55,
          "fats": 8,
          "protein_pct": 8,
          "carbs_pct": 92,
          "fats_pct": 25
        },
        "benefits": [
          "Instant energy boost",
          "Saffron improves mood",
          "Nostalgic happiness",
          "Quick sugar boost"
        ],
        "avoid_if": [
          "Diabetic",
          "Diet conscious"
        ]
      },
      {
        "name": "Bhel Puri",
        "description": "Puffed rice with vegetables, chutneys and sev.",
        "emoji": "🍿",
        "tags": [
          "Tangy",
          "Crunchy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 160,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 30,
          "fats": 4,
          "protein_pct": 14,
          "carbs_pct": 72,
          "fats_pct": 14
        },
        "benefits": [
          "Low calorie",
          "High fiber",
          "Mood-lifting taste",
          "Quick energy"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Acid reflux"
        ]
      },
      {
        "name": "Aloo Tikki",
        "description": "Crispy potato patties with chutneys and chaat masala.",
        "emoji": "🥔",
        "tags": [
          "Crispy",
          "Chatpata"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 220,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 38,
          "fats": 8,
          "protein_pct": 12,
          "carbs_pct": 75,
          "fats_pct": 28
        },
        "benefits": [
          "Quick energy",
          "Iron from spices",
          "Filling snack",
          "Mood-lifting"
        ],
        "avoid_if": [
          "Diabetic",
          "High cholesterol"
        ]
      },
      {
        "name": "Kulfi",
        "description": "Dense creamy ice cream with pistachio and saffron.",
        "emoji": "🍦",
        "tags": [
          "Sweet",
          "Creamy"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 200,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 30,
          "fats": 8,
          "protein_pct": 16,
          "carbs_pct": 68,
          "fats_pct": 25
        },
        "benefits": [
          "Calcium from milk",
          "Saffron mood-lifting",
          "Cooling",
          "Happiness"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Papdi Chaat",
        "description": "Crispy papdis with chickpeas, yogurt and chutneys.",
        "emoji": "🥗",
        "tags": [
          "Chatpata",
          "Crunchy"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 230,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 38,
          "fats": 7,
          "protein_pct": 24,
          "carbs_pct": 76,
          "fats_pct": 24
        },
        "benefits": [
          "Chickpeas protein",
          "Probiotics from yogurt",
          "Digestive aid",
          "Satisfying"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Rajma Chawal",
        "description": "Red kidney bean curry with steamed rice.",
        "emoji": "🍛",
        "tags": [
          "Hearty",
          "Comfort"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 420,
        "prep_time": "40 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 65,
          "fats": 6,
          "protein_pct": 45,
          "carbs_pct": 88,
          "fats_pct": 20
        },
        "benefits": [
          "High plant protein",
          "Iron-rich",
          "Fiber for digestion",
          "Sustained energy"
        ],
        "avoid_if": [
          "Kidney disease",
          "IBS"
        ]
      },
      {
        "name": "Masala Chai",
        "description": "Spiced Indian tea with ginger, cardamom and milk.",
        "emoji": "☕",
        "tags": [
          "Warm",
          "Spiced"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 80,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 3,
          "carbs": 12,
          "fats": 3,
          "protein_pct": 10,
          "carbs_pct": 42,
          "fats_pct": 12
        },
        "benefits": [
          "Ginger boosts immunity",
          "Antioxidants",
          "Mood-lifting ritual",
          "Digestive"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Paneer Tikka",
        "description": "Marinated cottage cheese grilled with spices.",
        "emoji": "🍢",
        "tags": [
          "Spicy",
          "Grilled"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 300,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Starter",
        "mood_score": 4,
        "nutrition": {
          "protein": 20,
          "carbs": 12,
          "fats": 18,
          "protein_pct": 55,
          "carbs_pct": 28,
          "fats_pct": 55
        },
        "benefits": [
          "Very high protein",
          "Calcium",
          "Low carb",
          "Satisfying"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Low-fat diet"
        ]
      },
      {
        "name": "Dahi Puri",
        "description": "Crispy puris topped with yogurt, sev and chutneys.",
        "emoji": "🍥",
        "tags": [
          "Tangy",
          "Cool"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 32,
          "fats": 6,
          "protein_pct": 22,
          "carbs_pct": 70,
          "fats_pct": 22
        },
        "benefits": [
          "Probiotics from dahi",
          "Cooling",
          "Light",
          "Mood-lifting"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Acid reflux"
        ]
      },
      {
        "name": "Poha",
        "description": "Flattened rice with mustard, onions and curry leaves.",
        "emoji": "🍚",
        "tags": [
          "Light",
          "Quick"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 38,
          "fats": 4,
          "protein_pct": 15,
          "carbs_pct": 82,
          "fats_pct": 14
        },
        "benefits": [
          "Iron-fortified",
          "Light on stomach",
          "Quick energy",
          "Digestible"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Kadai Paneer",
        "description": "Paneer with bell peppers in spicy masala gravy.",
        "emoji": "🧀",
        "tags": [
          "Spicy",
          "Rich"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 18,
          "carbs": 20,
          "fats": 22,
          "protein_pct": 48,
          "carbs_pct": 38,
          "fats_pct": 65
        },
        "benefits": [
          "High protein",
          "Bell peppers Vitamin C",
          "Calcium",
          "Satisfying"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Low-fat"
        ]
      },
      {
        "name": "Chana Chaat",
        "description": "Chickpeas with onions, tomatoes, lemon and chaat masala.",
        "emoji": "🥗",
        "tags": [
          "Healthy",
          "Chatpata"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 32,
          "fats": 3,
          "protein_pct": 38,
          "carbs_pct": 72,
          "fats_pct": 10
        },
        "benefits": [
          "Very high protein",
          "High fiber",
          "Iron-rich",
          "Low fat"
        ],
        "avoid_if": [
          "IBS",
          "Kidney disease"
        ]
      },
      {
        "name": "Sweet Lassi",
        "description": "Thick chilled yogurt drink with sugar and rose water.",
        "emoji": "🥛",
        "tags": [
          "Sweet",
          "Cooling"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Afternoon",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 32,
          "fats": 4,
          "protein_pct": 25,
          "carbs_pct": 72,
          "fats_pct": 14
        },
        "benefits": [
          "Probiotics for gut",
          "Cooling",
          "Calcium",
          "Protein-rich"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Kachori",
        "description": "Deep-fried pastry filled with spiced lentils.",
        "emoji": "🫔",
        "tags": [
          "Crispy",
          "Spicy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 280,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 38,
          "fats": 12,
          "protein_pct": 20,
          "carbs_pct": 78,
          "fats_pct": 38
        },
        "benefits": [
          "Lentils protein",
          "Spices immunity",
          "Filling",
          "Energy-boosting"
        ],
        "avoid_if": [
          "High cholesterol",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Masala Dosa",
        "description": "Crispy fermented rice crepe with spiced potato masala.",
        "emoji": "🥞",
        "tags": [
          "Crispy",
          "South Indian"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 350,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 58,
          "fats": 10,
          "protein_pct": 20,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Fermented good for gut",
          "Iron from potatoes",
          "Gluten-free",
          "Light yet filling"
        ],
        "avoid_if": [
          "Rice allergy"
        ]
      }
    ]
  },
  "sad": {
    "emoji": "😢",
    "color": "#6B9BD2",
    "tagline": "Warm Indian comfort food to wrap your soul in a hug.",
    "foods": [
      {
        "name": "Khichdi",
        "description": "Rice and moong dal porridge with ghee and turmeric.",
        "emoji": "🍲",
        "tags": [
          "Warm",
          "Comfort"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 52,
          "fats": 8,
          "protein_pct": 35,
          "carbs_pct": 80,
          "fats_pct": 28
        },
        "benefits": [
          "Easy to digest",
          "Turmeric anti-inflammatory",
          "Ghee brain health",
          "Complete protein"
        ],
        "avoid_if": [
          "Very low carb"
        ]
      },
      {
        "name": "Dal Chawal with Ghee",
        "description": "Yellow dal over steaming rice with generous ghee.",
        "emoji": "🍛",
        "tags": [
          "Homely",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 14,
          "carbs": 58,
          "fats": 8,
          "protein_pct": 40,
          "carbs_pct": 88,
          "fats_pct": 25
        },
        "benefits": [
          "Tryptophan boosts serotonin",
          "Complete amino acids",
          "Ghee gut health",
          "Ultimate Indian comfort"
        ],
        "avoid_if": [
          "Legume intolerance"
        ]
      },
      {
        "name": "Aloo Paratha with Butter",
        "description": "Crispy potato flatbread with white butter and pickle.",
        "emoji": "🫓",
        "tags": [
          "Crispy",
          "Homestyle"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 420,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 62,
          "fats": 16,
          "protein_pct": 22,
          "carbs_pct": 90,
          "fats_pct": 48
        },
        "benefits": [
          "Comfort food effect",
          "Ghee vitamins",
          "Potato quick energy",
          "Nostalgic happiness"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Suji Halwa",
        "description": "Golden semolina dessert with ghee, sugar and dry fruits.",
        "emoji": "🍮",
        "tags": [
          "Sweet",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 380,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 65,
          "fats": 12,
          "protein_pct": 15,
          "carbs_pct": 92,
          "fats_pct": 35
        },
        "benefits": [
          "Serotonin from sweetness",
          "Dry fruits mood boost",
          "Ghee warms body",
          "Nostalgic comfort"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Maggi Noodles",
        "description": "The iconic 2-minute noodles - India comfort food.",
        "emoji": "🍜",
        "tags": [
          "Quick",
          "Nostalgic"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 10,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 32
        },
        "benefits": [
          "Instant mood lifter",
          "Nostalgia effect",
          "Iron-fortified",
          "Quick energy"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Low-sodium"
        ]
      },
      {
        "name": "Gajar Halwa",
        "description": "Slow-cooked carrot dessert with milk, ghee and cardamom.",
        "emoji": "🥕",
        "tags": [
          "Sweet",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 55,
          "fats": 12,
          "protein_pct": 14,
          "carbs_pct": 90,
          "fats_pct": 35
        },
        "benefits": [
          "Beta-carotene for eyes",
          "Sweetness boosts serotonin",
          "Warm comfort",
          "Vitamin A"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Kadhi Chawal",
        "description": "Tangy yogurt gravy with pakoras over steamed rice.",
        "emoji": "🍲",
        "tags": [
          "Tangy",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 360,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 58,
          "fats": 10,
          "protein_pct": 28,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Probiotics from yogurt",
          "Turmeric anti-inflammatory",
          "Comfort effect",
          "Warm soothing"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Idli Sambhar",
        "description": "Soft steamed rice cakes with hot lentil soup.",
        "emoji": "🫓",
        "tags": [
          "Soft",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 48,
          "fats": 4,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 12
        },
        "benefits": [
          "Fermented probiotic",
          "Light digestible",
          "Protein from lentils",
          "Soothing warm meal"
        ],
        "avoid_if": [
          "Rice allergy"
        ]
      },
      {
        "name": "Moong Dal Soup",
        "description": "Light yellow lentil soup with ginger, garlic and jeera.",
        "emoji": "🍵",
        "tags": [
          "Warm",
          "Light"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 30,
          "fats": 3,
          "protein_pct": 42,
          "carbs_pct": 65,
          "fats_pct": 10
        },
        "benefits": [
          "High protein",
          "Easy to digest",
          "Warming soothing",
          "Detoxifying"
        ],
        "avoid_if": [
          "Legume allergy"
        ]
      },
      {
        "name": "Pav Bhaji",
        "description": "Buttery mashed vegetable curry with toasted pav buns.",
        "emoji": "🍞",
        "tags": [
          "Buttery",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 450,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 68,
          "fats": 16,
          "protein_pct": 22,
          "carbs_pct": 88,
          "fats_pct": 48
        },
        "benefits": [
          "Vegetables give vitamins",
          "Butter boosts mood",
          "Comfort meal",
          "Iron from vegetables"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Kheer",
        "description": "Creamy rice pudding with saffron and cardamom.",
        "emoji": "🍚",
        "tags": [
          "Sweet",
          "Creamy"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "40 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 55,
          "fats": 10,
          "protein_pct": 20,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Saffron lifts mood",
          "Calcium from milk",
          "Sweetness serotonin",
          "Nostalgic comfort"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Tomato Soup",
        "description": "Velvety tomato soup with Indian spices and cream.",
        "emoji": "🍅",
        "tags": [
          "Warm",
          "Soothing"
        ],
        "is_veg": True,
        "diet_type": [
          "Low Carb"
        ],
        "calories": 180,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 22,
          "fats": 8,
          "protein_pct": 14,
          "carbs_pct": 55,
          "fats_pct": 28
        },
        "benefits": [
          "Lycopene for heart",
          "Vitamin C boost",
          "Warm soothing",
          "Low calorie"
        ],
        "avoid_if": [
          "Acid reflux",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Sabudana Khichdi",
        "description": "Sago pearls with peanuts, potatoes and green chilli.",
        "emoji": "🫙",
        "tags": [
          "Light",
          "Comfort"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 360,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 62,
          "fats": 10,
          "protein_pct": 18,
          "carbs_pct": 90,
          "fats_pct": 28
        },
        "benefits": [
          "Quick energy",
          "Peanuts protein",
          "Gluten-free",
          "Easy on stomach"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      },
      {
        "name": "Roti Sabzi",
        "description": "Soft wheat rotis with home-cooked vegetable curry.",
        "emoji": "🫓",
        "tags": [
          "Simple",
          "Homestyle"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 350,
        "prep_time": "30 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 58,
          "fats": 8,
          "protein_pct": 28,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Whole wheat fiber",
          "Vegetables vitamins",
          "Home comfort",
          "Balanced meal"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Badam Milk",
        "description": "Warm almond milk with saffron, cardamom and sugar.",
        "emoji": "🥛",
        "tags": [
          "Warm",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 25,
          "fats": 10,
          "protein_pct": 25,
          "carbs_pct": 55,
          "fats_pct": 32
        },
        "benefits": [
          "Almonds boost serotonin",
          "Saffron lifts mood",
          "Calcium for bones",
          "Warm comforting"
        ],
        "avoid_if": [
          "Nut allergy",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Curd Rice",
        "description": "Soft cooked rice mixed with yogurt and tempering.",
        "emoji": "🍚",
        "tags": [
          "Cooling",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 290,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 48,
          "fats": 5,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 16
        },
        "benefits": [
          "Probiotics calm gut-brain",
          "Cooling for mind",
          "Carbs boost serotonin",
          "Protein keeps calm"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Egg Bhurji",
        "description": "Scrambled eggs with onions, tomatoes and spices.",
        "emoji": "🍳",
        "tags": [
          "Protein-rich",
          "Quick"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 250,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 18,
          "carbs": 10,
          "fats": 16,
          "protein_pct": 52,
          "carbs_pct": 20,
          "fats_pct": 50
        },
        "benefits": [
          "Complete protein",
          "Choline for brain",
          "Quick mood boost",
          "Filling"
        ],
        "avoid_if": [
          "Egg allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Besan Chilla",
        "description": "Crispy gram flour pancakes with onions and coriander.",
        "emoji": "🥞",
        "tags": [
          "Healthy",
          "Crispy"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Vegan"
        ],
        "calories": 220,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 32,
          "fats": 6,
          "protein_pct": 35,
          "carbs_pct": 72,
          "fats_pct": 20
        },
        "benefits": [
          "Chickpea flour protein",
          "Gluten-free",
          "Iron-rich",
          "Filling"
        ],
        "avoid_if": [
          "Chickpea allergy"
        ]
      },
      {
        "name": "Palak Soup",
        "description": "Smooth spinach soup with garlic and black pepper.",
        "emoji": "🥬",
        "tags": [
          "Iron-rich",
          "Smooth"
        ],
        "is_veg": True,
        "diet_type": [
          "Low Carb"
        ],
        "calories": 160,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 6,
          "carbs": 16,
          "fats": 8,
          "protein_pct": 18,
          "carbs_pct": 42,
          "fats_pct": 28
        },
        "benefits": [
          "Folate reduces depression",
          "Magnesium calms muscles",
          "Iron prevents anxiety",
          "Warm comforting"
        ],
        "avoid_if": [
          "Kidney stones",
          "Blood thinners"
        ]
      },
      {
        "name": "Rajma Chawal Sunday Special",
        "description": "Classic red kidney bean curry - every Punjabi Sunday meal.",
        "emoji": "🍛",
        "tags": [
          "Sunday Special",
          "Classic"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 440,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Sunday Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 70,
          "fats": 6,
          "protein_pct": 42,
          "carbs_pct": 90,
          "fats_pct": 18
        },
        "benefits": [
          "Sunday nostalgia reduces sadness",
          "High plant protein",
          "Complex carbs for serotonin",
          "Iron-rich"
        ],
        "avoid_if": [
          "Kidney disease",
          "IBS"
        ]
      },
      {
        "name": "Upma",
        "description": "Semolina cooked with vegetables and curry leaves.",
        "emoji": "🍚",
        "tags": [
          "Light",
          "South Indian"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 240,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 3,
        "nutrition": {
          "protein": 6,
          "carbs": 42,
          "fats": 7,
          "protein_pct": 16,
          "carbs_pct": 80,
          "fats_pct": 22
        },
        "benefits": [
          "Quick energy",
          "Vegetables add vitamins",
          "Light on stomach",
          "Easy to make"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      }
    ]
  },
  "stressed": {
    "emoji": "😤",
    "color": "#FF6B6B",
    "tagline": "Calming Indian foods to melt your tension away.",
    "foods": [
      {
        "name": "Haldi Doodh",
        "description": "Warm milk with turmeric, ginger, black pepper and honey.",
        "emoji": "🥛",
        "tags": [
          "Healing",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 140,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 18,
          "fats": 5,
          "protein_pct": 20,
          "carbs_pct": 45,
          "fats_pct": 18
        },
        "benefits": [
          "Curcumin reduces anxiety",
          "Tryptophan promotes calm",
          "Ginger lowers cortisol",
          "Ayurvedic remedy"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Blood thinners"
        ]
      },
      {
        "name": "Tulsi Green Tea",
        "description": "Green tea brewed with holy basil leaves and honey.",
        "emoji": "🍵",
        "tags": [
          "Calming",
          "Herbal"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 15,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 3,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 10,
          "fats_pct": 2
        },
        "benefits": [
          "Tulsi proven adaptogen",
          "Reduces cortisol",
          "L-theanine promotes calm",
          "Sacred plant comfort"
        ],
        "avoid_if": [
          "Blood thinners",
          "Pregnant women"
        ]
      },
      {
        "name": "Moong Dal Khichdi",
        "description": "Soft moong dal and rice with ghee - Ayurveda stress food.",
        "emoji": "🍲",
        "tags": [
          "Light",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 45,
          "fats": 6,
          "protein_pct": 35,
          "carbs_pct": 80,
          "fats_pct": 20
        },
        "benefits": [
          "Tryptophan boosts serotonin",
          "Easy on nervous stomach",
          "Ghee calms nervous system",
          "Sattvic food"
        ],
        "avoid_if": [
          "Legume intolerance"
        ]
      },
      {
        "name": "Dark Chocolate Barfi",
        "description": "Indian milk fudge made with dark chocolate and cardamom.",
        "emoji": "🍫",
        "tags": [
          "Sweet",
          "Rich"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 200,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 4,
          "carbs": 25,
          "fats": 12,
          "protein_pct": 12,
          "carbs_pct": 55,
          "fats_pct": 38
        },
        "benefits": [
          "Magnesium reduces stress",
          "Serotonin from chocolate",
          "Endorphin release",
          "Cardamom calms mind"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Diabetic"
        ]
      },
      {
        "name": "Banana with Peanut Butter",
        "description": "Ripe banana with natural peanut butter - simple grounding.",
        "emoji": "🍌",
        "tags": [
          "Quick",
          "Grounding"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 38,
          "fats": 12,
          "protein_pct": 28,
          "carbs_pct": 75,
          "fats_pct": 38
        },
        "benefits": [
          "Banana serotonin precursor",
          "Peanut butter magnesium",
          "Stable blood sugar",
          "Potassium prevents tension"
        ],
        "avoid_if": [
          "Peanut allergy",
          "Latex-fruit syndrome"
        ]
      },
      {
        "name": "Kadha Immunity Drink",
        "description": "Traditional decoction with tulsi, ginger, cloves and honey.",
        "emoji": "🫖",
        "tags": [
          "Herbal",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 30,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 7,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 20,
          "fats_pct": 2
        },
        "benefits": [
          "Tulsi reduces stress",
          "Ginger calms nerves",
          "Cloves anti-anxiety",
          "Ayurvedic tradition"
        ],
        "avoid_if": [
          "Blood pressure medication",
          "Pregnant women"
        ]
      },
      {
        "name": "Oats Upma",
        "description": "Rolled oats cooked with mustard and vegetables.",
        "emoji": "🌾",
        "tags": [
          "Healthy",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 260,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 42,
          "fats": 6,
          "protein_pct": 22,
          "carbs_pct": 80,
          "fats_pct": 20
        },
        "benefits": [
          "Oats contain tryptophan",
          "Slow carbs prevent anxiety",
          "Fiber for gut-brain axis",
          "Magnesium calms"
        ],
        "avoid_if": [
          "Oat/gluten sensitivity"
        ]
      },
      {
        "name": "Walnut and Dates Mix",
        "description": "A handful of walnuts and Medjool dates.",
        "emoji": "🥜",
        "tags": [
          "Natural",
          "Stress-busting"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 220,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 28,
          "fats": 12,
          "protein_pct": 15,
          "carbs_pct": 60,
          "fats_pct": 38
        },
        "benefits": [
          "Walnuts omega-3 reduces cortisol",
          "Magnesium calms nervous system",
          "Dates natural energy",
          "Proven stress-busters"
        ],
        "avoid_if": [
          "Nut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Curd Rice",
        "description": "Soft rice with yogurt and mild tempering.",
        "emoji": "🍚",
        "tags": [
          "Cooling",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 290,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 48,
          "fats": 5,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 16
        },
        "benefits": [
          "Probiotics proven anxiety reducers",
          "Cooling for anxious mind",
          "Carbs boost serotonin",
          "Traditional calming"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Makhana Roasted",
        "description": "Lightly roasted lotus seeds with ghee and rock salt.",
        "emoji": "🌸",
        "tags": [
          "Light",
          "Crunchy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 160,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 9,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 28,
          "carbs_pct": 65,
          "fats_pct": 6
        },
        "benefits": [
          "Magnesium reduces anxiety",
          "Low calorie calming snack",
          "Ayurvedic nerve tonic",
          "Anti-inflammatory"
        ],
        "avoid_if": [
          "Rarely contraindicated"
        ]
      },
      {
        "name": "Ashwagandha Milk",
        "description": "Warm milk with ashwagandha powder, honey and nutmeg.",
        "emoji": "🥛",
        "tags": [
          "Adaptogen",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 180,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 22,
          "fats": 6,
          "protein_pct": 18,
          "carbs_pct": 52,
          "fats_pct": 18
        },
        "benefits": [
          "Ashwagandha proven anxiety reducer",
          "Reduces cortisol up to 30%",
          "Tryptophan for calm",
          "Nutmeg sedative"
        ],
        "avoid_if": [
          "Pregnant women",
          "Thyroid medication",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Palak Paneer",
        "description": "Iron-rich spinach with high protein cottage cheese.",
        "emoji": "🥬",
        "tags": [
          "Protein-rich",
          "Iron-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 340,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 16,
          "carbs": 18,
          "fats": 20,
          "protein_pct": 44,
          "carbs_pct": 35,
          "fats_pct": 60
        },
        "benefits": [
          "Iron from spinach fights fatigue",
          "Folate reduces depression",
          "Calcium from paneer",
          "Magnesium calms"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Kidney stones"
        ]
      },
      {
        "name": "Coconut Water Chia",
        "description": "Fresh coconut water with soaked chia seeds and lime.",
        "emoji": "🥥",
        "tags": [
          "Hydrating",
          "Cooling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 110,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 2,
          "carbs": 18,
          "fats": 3,
          "protein_pct": 8,
          "carbs_pct": 45,
          "fats_pct": 12
        },
        "benefits": [
          "Electrolytes calm nerves",
          "Coconut water stress buster",
          "Omega-3 in chia seeds",
          "Hydration reduces irritability"
        ],
        "avoid_if": [
          "High potassium",
          "Coconut allergy"
        ]
      },
      {
        "name": "Sattu Drink",
        "description": "Roasted gram flour drink with lemon, salt and mint.",
        "emoji": "🥤",
        "tags": [
          "Cooling",
          "Protein-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 150,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 22,
          "fats": 3,
          "protein_pct": 32,
          "carbs_pct": 58,
          "fats_pct": 10
        },
        "benefits": [
          "High protein keeps calm",
          "Cooling for body",
          "Iron and fiber rich",
          "Stabilizes blood sugar"
        ],
        "avoid_if": [
          "Chickpea allergy"
        ]
      },
      {
        "name": "Vegetable Daliya",
        "description": "Broken wheat porridge with vegetables and mild spices.",
        "emoji": "🌾",
        "tags": [
          "Wholesome",
          "Grounding"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 260,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 3,
        "nutrition": {
          "protein": 8,
          "carbs": 48,
          "fats": 4,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 14
        },
        "benefits": [
          "Whole grain steady energy",
          "Fiber stabilizes blood sugar",
          "Tryptophan boosts serotonin",
          "Grounding comfort"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Sprouts Salad",
        "description": "Mixed moong and chana sprouts with lemon and chaat masala.",
        "emoji": "🥗",
        "tags": [
          "Healthy",
          "Light"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 3,
        "nutrition": {
          "protein": 12,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 38,
          "carbs_pct": 65,
          "fats_pct": 6
        },
        "benefits": [
          "Very high protein",
          "B vitamins for nervous system",
          "Fiber stabilizes blood sugar",
          "Zinc for mood"
        ],
        "avoid_if": [
          "IBS",
          "Kidney disease"
        ]
      },
      {
        "name": "Raita Cucumber",
        "description": "Chilled yogurt with grated cucumber, cumin and coriander.",
        "emoji": "🥒",
        "tags": [
          "Cooling",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 100,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "With Meals",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 10,
          "fats": 3,
          "protein_pct": 20,
          "carbs_pct": 35,
          "fats_pct": 12
        },
        "benefits": [
          "Probiotics calm gut-brain",
          "Cucumber natural coolant",
          "Magnesium calms",
          "Refreshing"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Lemon Grass Tea",
        "description": "Refreshing lemon grass and ginger tea with honey.",
        "emoji": "🍵",
        "tags": [
          "Herbal",
          "Fresh"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 20,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 4,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 12,
          "fats_pct": 2
        },
        "benefits": [
          "Lemon grass reduces anxiety",
          "Citral calms nervous system",
          "Caffeine-free",
          "Digestive aid"
        ],
        "avoid_if": [
          "Pregnant women",
          "Low blood pressure"
        ]
      },
      {
        "name": "Anjeer and Milk",
        "description": "Soaked dried figs in warm milk with saffron.",
        "emoji": "🌰",
        "tags": [
          "Natural",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "8 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 6,
          "carbs": 35,
          "fats": 4,
          "protein_pct": 18,
          "carbs_pct": 75,
          "fats_pct": 14
        },
        "benefits": [
          "Figs high in magnesium",
          "Tryptophan promotes sleep",
          "Natural sugar for mood",
          "Ayurvedic remedy"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Buttermilk Chaach",
        "description": "Thin spiced yogurt drink with jeera and rock salt.",
        "emoji": "🥛",
        "tags": [
          "Cooling",
          "Probiotic"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Afternoon",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 6,
          "fats": 1,
          "protein_pct": 28,
          "carbs_pct": 30,
          "fats_pct": 8
        },
        "benefits": [
          "Probiotics reduce gut anxiety",
          "Digestive aid reduces bloating",
          "Cooling for tense mind",
          "Very low calorie"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Alsi Ladoo",
        "description": "Roasted flaxseed ladoos with jaggery - omega-3 powerhouse.",
        "emoji": "🟤",
        "tags": [
          "Omega-3",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 25,
          "fats": 9,
          "protein_pct": 14,
          "carbs_pct": 62,
          "fats_pct": 28
        },
        "benefits": [
          "Flaxseed highest plant omega-3",
          "Reduces anxiety inflammation",
          "Lignans balance hormones",
          "Traditional remedy"
        ],
        "avoid_if": [
          "Blood thinners",
          "Hormone-sensitive conditions"
        ]
      }
    ]
  },
  "energetic": {
    "emoji": "⚡",
    "color": "#FF9F1C",
    "tagline": "Power-packed Indian foods to fuel your energy!",
    "foods": [
      {
        "name": "Egg White Omelette",
        "description": "Fluffy egg white omelette with vegetables.",
        "emoji": "🍳",
        "tags": [
          "Protein",
          "Power"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 200,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 22,
          "carbs": 6,
          "fats": 4,
          "protein_pct": 65,
          "carbs_pct": 14,
          "fats_pct": 12
        },
        "benefits": [
          "Purest protein source",
          "Choline for focus",
          "Zero fat",
          "B12 for energy"
        ],
        "avoid_if": [
          "Egg allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Chana Masala",
        "description": "Spicy North Indian chickpea curry - protein powerhouse.",
        "emoji": "🫘",
        "tags": [
          "High Protein",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 58,
          "fats": 8,
          "protein_pct": 45,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Highest plant protein",
          "Iron prevents energy crashes",
          "Complex carbs for stamina",
          "Zinc"
        ],
        "avoid_if": [
          "IBS",
          "Kidney disease"
        ]
      },
      {
        "name": "Grilled Chicken Tikka",
        "description": "Tandoor-grilled marinated chicken - lean protein.",
        "emoji": "🍗",
        "tags": [
          "High Protein",
          "Grilled"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 280,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 35,
          "carbs": 8,
          "fats": 12,
          "protein_pct": 88,
          "carbs_pct": 18,
          "fats_pct": 38
        },
        "benefits": [
          "Very high protein",
          "Low fat grilled",
          "B12 for energy",
          "Iron for oxygen"
        ],
        "avoid_if": [
          "Vegetarians",
          "Low-sodium"
        ]
      },
      {
        "name": "Sattu Paratha",
        "description": "High-protein roasted gram stuffed flatbread.",
        "emoji": "🫓",
        "tags": [
          "High Protein",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 350,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 16,
          "carbs": 52,
          "fats": 8,
          "protein_pct": 42,
          "carbs_pct": 84,
          "fats_pct": 24
        },
        "benefits": [
          "Sattu highest plant protein",
          "Iron-rich",
          "Cooling energy food",
          "Sustained power"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Chickpea allergy"
        ]
      },
      {
        "name": "Banana Shake",
        "description": "Thick banana blended with milk, honey and almonds.",
        "emoji": "🍌",
        "tags": [
          "Sweet",
          "Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Pre-workout",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 58,
          "fats": 10,
          "protein_pct": 32,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Quick energy from natural sugars",
          "Potassium prevents cramps",
          "Protein from milk",
          "Dopamine boost"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Latex-fruit syndrome"
        ]
      },
      {
        "name": "Poha with Peanuts",
        "description": "Flattened rice with roasted peanuts, curry leaves and turmeric.",
        "emoji": "🍚",
        "tags": [
          "Light",
          "Iron-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 260,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 42,
          "fats": 8,
          "protein_pct": 22,
          "carbs_pct": 78,
          "fats_pct": 24
        },
        "benefits": [
          "Iron-fortified for energy",
          "Peanuts protein",
          "Quick to digest",
          "B1 for energy metabolism"
        ],
        "avoid_if": [
          "Peanut allergy"
        ]
      },
      {
        "name": "Sprouted Moong Salad",
        "description": "Germinated moong sprouts with lemon and vegetables.",
        "emoji": "🌱",
        "tags": [
          "Raw",
          "Protein-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 150,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 22,
          "fats": 1,
          "protein_pct": 32,
          "carbs_pct": 60,
          "fats_pct": 4
        },
        "benefits": [
          "Highest protein when sprouted",
          "Vitamin C increases",
          "Enzymes aid digestion",
          "Iron for oxygen"
        ],
        "avoid_if": [
          "IBS sufferers"
        ]
      },
      {
        "name": "Masala Oats",
        "description": "Savory oats cooked with vegetables and mustard seeds.",
        "emoji": "🌾",
        "tags": [
          "Filling",
          "Slow Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 280,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 9,
          "carbs": 48,
          "fats": 6,
          "protein_pct": 24,
          "carbs_pct": 82,
          "fats_pct": 20
        },
        "benefits": [
          "Slow-release carbs for stamina",
          "Beta-glucan sustained energy",
          "Iron and B vitamins",
          "Fiber for fuel"
        ],
        "avoid_if": [
          "Gluten/oat sensitivity"
        ]
      },
      {
        "name": "Rajma Chawal",
        "description": "Protein-rich kidney bean curry with rice.",
        "emoji": "🍛",
        "tags": [
          "Complete Protein",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 440,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 18,
          "carbs": 70,
          "fats": 6,
          "protein_pct": 42,
          "carbs_pct": 90,
          "fats_pct": 18
        },
        "benefits": [
          "Iron + plant protein combo",
          "Complex carbs for energy",
          "Fiber slows energy release",
          "Zinc for recovery"
        ],
        "avoid_if": [
          "Kidney disease",
          "IBS"
        ]
      },
      {
        "name": "Dry Fruit Ladoo",
        "description": "Energy balls with dates, almonds, cashews - no sugar added.",
        "emoji": "🍬",
        "tags": [
          "Natural Energy",
          "No Sugar"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Pre-workout",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 28,
          "fats": 8,
          "protein_pct": 18,
          "carbs_pct": 65,
          "fats_pct": 25
        },
        "benefits": [
          "Natural sugar quick energy",
          "Healthy fats for stamina",
          "Iron from dates",
          "No artificial sugar"
        ],
        "avoid_if": [
          "Nut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Paneer Bhurji",
        "description": "Crumbled cottage cheese scrambled with onions and spices.",
        "emoji": "🧀",
        "tags": [
          "High Protein",
          "Quick"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 320,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 22,
          "carbs": 12,
          "fats": 20,
          "protein_pct": 60,
          "carbs_pct": 26,
          "fats_pct": 60
        },
        "benefits": [
          "Very high protein",
          "Calcium for bones",
          "B vitamins for energy",
          "Quick to make"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Ragi Mudde",
        "description": "Finger millet balls - Karnataka superfood for energy.",
        "emoji": "🟤",
        "tags": [
          "Superfood",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 320,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 65,
          "fats": 4,
          "protein_pct": 25,
          "carbs_pct": 90,
          "fats_pct": 12
        },
        "benefits": [
          "Highest calcium grain",
          "Iron for energy",
          "Slow-release energy",
          "Gluten-free"
        ],
        "avoid_if": [
          "Kidney stones"
        ]
      },
      {
        "name": "Peanut Chikki",
        "description": "Crunchy peanut and jaggery brittle - India original energy bar.",
        "emoji": "🍬",
        "tags": [
          "Natural Energy",
          "Crunchy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Pre-workout",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 28,
          "fats": 10,
          "protein_pct": 24,
          "carbs_pct": 65,
          "fats_pct": 30
        },
        "benefits": [
          "Jaggery iron for energy",
          "Protein from peanuts",
          "Natural energy boost",
          "Better than candy bars"
        ],
        "avoid_if": [
          "Peanut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Dhokla",
        "description": "Steamed fermented gram flour cake with mustard tempering.",
        "emoji": "🟡",
        "tags": [
          "Light",
          "Protein-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 220,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 38,
          "fats": 4,
          "protein_pct": 28,
          "carbs_pct": 78,
          "fats_pct": 12
        },
        "benefits": [
          "Fermented probiotic",
          "High protein from besan",
          "Low fat steamed",
          "Iron for energy"
        ],
        "avoid_if": [
          "Chickpea allergy"
        ]
      },
      {
        "name": "Mutton Keema",
        "description": "Minced lamb cooked with onions, tomatoes and whole spices.",
        "emoji": "🍖",
        "tags": [
          "High Protein",
          "Iron-rich"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 380,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 35,
          "carbs": 10,
          "fats": 22,
          "protein_pct": 88,
          "carbs_pct": 22,
          "fats_pct": 65
        },
        "benefits": [
          "Highest iron content",
          "Zinc boosts testosterone",
          "B12 for energy",
          "Complete protein"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol"
        ]
      },
      {
        "name": "Quinoa Khichdi",
        "description": "Quinoa cooked with dal and vegetables - modern protein powerhouse.",
        "emoji": "🌾",
        "tags": [
          "Complete Protein",
          "Modern"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 52,
          "fats": 6,
          "protein_pct": 38,
          "carbs_pct": 85,
          "fats_pct": 18
        },
        "benefits": [
          "Quinoa has all 9 amino acids",
          "Complete plant protein",
          "Iron prevents energy crashes",
          "Fiber for fuel"
        ],
        "avoid_if": [
          "Quinoa intolerance"
        ]
      },
      {
        "name": "Lassi Salted",
        "description": "Thick salted yogurt drink with roasted cumin and mint.",
        "emoji": "🥛",
        "tags": [
          "Electrolytes",
          "Cooling"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 150,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Post-workout",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 16,
          "fats": 5,
          "protein_pct": 28,
          "carbs_pct": 48,
          "fats_pct": 18
        },
        "benefits": [
          "Electrolytes replenish minerals",
          "Probiotics for gut",
          "Protein for recovery",
          "Cooling after exercise"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Boiled Egg Curry",
        "description": "Hard-boiled eggs in spicy onion-tomato masala.",
        "emoji": "🥚",
        "tags": [
          "High Protein",
          "Power"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 300,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 20,
          "carbs": 14,
          "fats": 18,
          "protein_pct": 55,
          "carbs_pct": 30,
          "fats_pct": 55
        },
        "benefits": [
          "Complete protein egg",
          "Choline for brain",
          "Iron from masala",
          "Most economical protein"
        ],
        "avoid_if": [
          "Egg allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Soya Keema",
        "description": "Textured soya protein cooked like minced meat.",
        "emoji": "🟤",
        "tags": [
          "Plant Protein",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 22,
          "carbs": 22,
          "fats": 8,
          "protein_pct": 62,
          "carbs_pct": 48,
          "fats_pct": 24
        },
        "benefits": [
          "Highest plant protein",
          "Isoflavones for balance",
          "Iron from soya",
          "Complete amino acids"
        ],
        "avoid_if": [
          "Soy allergy",
          "Hypothyroidism"
        ]
      },
      {
        "name": "Dalia with Milk",
        "description": "Creamy broken wheat porridge with milk, nuts and honey.",
        "emoji": "🍚",
        "tags": [
          "Wholesome",
          "Sustained Energy"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 55,
          "fats": 7,
          "protein_pct": 26,
          "carbs_pct": 85,
          "fats_pct": 22
        },
        "benefits": [
          "Whole grain for stamina",
          "Milk protein for energy",
          "Nuts healthy fats",
          "Steady energy release"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Matar Paneer",
        "description": "Green peas and cottage cheese in spiced tomato gravy.",
        "emoji": "🟢",
        "tags": [
          "Protein",
          "Iron-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 360,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 18,
          "carbs": 28,
          "fats": 18,
          "protein_pct": 45,
          "carbs_pct": 55,
          "fats_pct": 55
        },
        "benefits": [
          "Peas and paneer double protein",
          "Iron from peas",
          "Calcium from paneer",
          "Filling meal"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      }
    ]
  },
  "tired": {
    "emoji": "😴",
    "color": "#9B8EC4",
    "tagline": "Quick restorative Indian foods to revive your energy.",
    "foods": [
      {
        "name": "Banana with Honey",
        "description": "Ripe banana drizzled with raw honey and cinnamon.",
        "emoji": "🍌",
        "tags": [
          "Quick",
          "Natural Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 2,
          "carbs": 42,
          "fats": 0,
          "protein_pct": 6,
          "carbs_pct": 88,
          "fats_pct": 2
        },
        "benefits": [
          "Instant glucose for energy",
          "Potassium prevents fatigue",
          "Honey sustained fuel",
          "Cinnamon stabilizes blood sugar"
        ],
        "avoid_if": [
          "Diabetic",
          "Latex-fruit syndrome"
        ]
      },
      {
        "name": "Haldi Doodh",
        "description": "Warm milk with turmeric, ginger and black pepper.",
        "emoji": "🥛",
        "tags": [
          "Healing",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 160,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 16,
          "fats": 8,
          "protein_pct": 18,
          "carbs_pct": 42,
          "fats_pct": 28
        },
        "benefits": [
          "Curcumin fights fatigue",
          "Tryptophan induces sleep",
          "Ginger boosts circulation",
          "Black pepper absorption"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Blood thinners"
        ]
      },
      {
        "name": "Dates and Nuts Mix",
        "description": "Medjool dates with almonds, cashews and raisins.",
        "emoji": "🌰",
        "tags": [
          "Instant Energy",
          "Iron-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 220,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 38,
          "fats": 8,
          "protein_pct": 14,
          "carbs_pct": 78,
          "fats_pct": 24
        },
        "benefits": [
          "Iron in dates combats tiredness",
          "Natural sugar for energy",
          "Magnesium reduces fatigue",
          "B vitamins"
        ],
        "avoid_if": [
          "Nut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Chana Dal",
        "description": "Simple chana dal with turmeric and mustard tempering.",
        "emoji": "🟡",
        "tags": [
          "Protein-rich",
          "Iron-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 15,
          "carbs": 42,
          "fats": 4,
          "protein_pct": 42,
          "carbs_pct": 80,
          "fats_pct": 12
        },
        "benefits": [
          "Iron fights fatigue and anemia",
          "Folate for red blood cells",
          "Protein for recovery",
          "B vitamins"
        ],
        "avoid_if": [
          "Legume intolerance",
          "IBS"
        ]
      },
      {
        "name": "Moong Dal Soup",
        "description": "Thin yellow lentil broth with ginger, garlic and jeera.",
        "emoji": "🍵",
        "tags": [
          "Light",
          "Restorative"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 38,
          "carbs_pct": 68,
          "fats_pct": 6
        },
        "benefits": [
          "Easily digestible when tired",
          "High protein for recovery",
          "Detoxifying",
          "Warm soothing"
        ],
        "avoid_if": [
          "Legume allergy"
        ]
      },
      {
        "name": "Coconut Water",
        "description": "Fresh tender coconut water - nature electrolyte drink.",
        "emoji": "🥥",
        "tags": [
          "Hydrating",
          "Electrolytes"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 1,
          "carbs": 14,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 42,
          "fats_pct": 2
        },
        "benefits": [
          "Electrolytes fight fatigue instantly",
          "Natural rehydration",
          "Potassium for muscle recovery",
          "Better than energy drinks"
        ],
        "avoid_if": [
          "High potassium",
          "Kidney disease"
        ]
      },
      {
        "name": "Sabudana Khichdi",
        "description": "Sago pearls with peanuts, potato and green chilli.",
        "emoji": "⚪",
        "tags": [
          "Quick Energy",
          "Gluten-free"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 380,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 68,
          "fats": 10,
          "protein_pct": 18,
          "carbs_pct": 92,
          "fats_pct": 28
        },
        "benefits": [
          "Quick carbs for instant energy",
          "Peanuts provide protein",
          "Gluten-free and easy",
          "Satisfying light meal"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      },
      {
        "name": "Amla Juice",
        "description": "Fresh Indian gooseberry juice with honey and ginger.",
        "emoji": "🟢",
        "tags": [
          "Vitamin C",
          "Energizing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 12,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 38,
          "fats_pct": 2
        },
        "benefits": [
          "20x more Vitamin C than oranges",
          "Antioxidants fight fatigue",
          "Iron absorption booster",
          "Ayurvedic tonic"
        ],
        "avoid_if": [
          "Severe acid reflux",
          "Blood thinners"
        ]
      },
      {
        "name": "Curd with Jaggery",
        "description": "Fresh homemade curd topped with grated jaggery.",
        "emoji": "🥛",
        "tags": [
          "Probiotic",
          "Natural Sweet"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Afternoon",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 28,
          "fats": 4,
          "protein_pct": 24,
          "carbs_pct": 68,
          "fats_pct": 12
        },
        "benefits": [
          "Probiotics restore gut energy",
          "Jaggery iron fights tiredness",
          "Natural sugar for fuel",
          "Calcium"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Peanut Butter Toast",
        "description": "Multigrain bread with natural peanut butter and banana.",
        "emoji": "🍞",
        "tags": [
          "Protein",
          "Quick"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 42,
          "fats": 14,
          "protein_pct": 32,
          "carbs_pct": 75,
          "fats_pct": 42
        },
        "benefits": [
          "Protein for recovery",
          "Banana potassium prevents fatigue",
          "Slow and fast energy combined",
          "Magnesium"
        ],
        "avoid_if": [
          "Peanut allergy",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Palak Dal",
        "description": "Iron-rich spinach with red lentils and curry leaves.",
        "emoji": "🥬",
        "tags": [
          "Iron-rich",
          "Restorative"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 260,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 38,
          "fats": 4,
          "protein_pct": 40,
          "carbs_pct": 75,
          "fats_pct": 14
        },
        "benefits": [
          "Highest iron combination food",
          "Folate for red blood cells",
          "Protein for energy recovery",
          "B vitamins"
        ],
        "avoid_if": [
          "Kidney stones",
          "Blood thinners"
        ]
      },
      {
        "name": "Rajgira Ladoo",
        "description": "Puffed amaranth ladoos with jaggery - ancient superfood.",
        "emoji": "🟤",
        "tags": [
          "Superfood",
          "Iron-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 170,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 30,
          "fats": 4,
          "protein_pct": 14,
          "carbs_pct": 75,
          "fats_pct": 12
        },
        "benefits": [
          "Iron fights anemia and fatigue",
          "Calcium for energy",
          "Complete protein grain",
          "Jaggery for fuel"
        ],
        "avoid_if": [
          "Rarely contraindicated"
        ]
      },
      {
        "name": "Til Ladoo",
        "description": "Sesame seed and jaggery ladoos - winter energy balls.",
        "emoji": "⚫",
        "tags": [
          "Iron-rich",
          "Calcium-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 28,
          "fats": 10,
          "protein_pct": 14,
          "carbs_pct": 65,
          "fats_pct": 30
        },
        "benefits": [
          "Sesame highest calcium food",
          "Iron from jaggery for energy",
          "B vitamins",
          "Warming"
        ],
        "avoid_if": [
          "Sesame allergy"
        ]
      },
      {
        "name": "Aam Ras",
        "description": "Fresh mango pulp with cardamom - seasonal energy boost.",
        "emoji": "🥭",
        "tags": [
          "Sweet",
          "Natural Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 160,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Summer",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 38,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 88,
          "fats_pct": 2
        },
        "benefits": [
          "Natural sugar for energy",
          "Vitamin C boost",
          "Vitamin A for eyes",
          "Mood-lifting"
        ],
        "avoid_if": [
          "Diabetic",
          "Mango allergy"
        ]
      },
      {
        "name": "Besan Ladoo",
        "description": "Roasted gram flour ladoos with ghee and sugar.",
        "emoji": "🟡",
        "tags": [
          "Traditional",
          "Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 6,
          "carbs": 30,
          "fats": 8,
          "protein_pct": 18,
          "carbs_pct": 72,
          "fats_pct": 24
        },
        "benefits": [
          "Chickpea flour protein",
          "Ghee for absorption",
          "Iron-rich",
          "Traditional energy food"
        ],
        "avoid_if": [
          "Diabetic",
          "Chickpea allergy"
        ]
      },
      {
        "name": "Makhana Kheer",
        "description": "Fox nut pudding with milk, saffron and cardamom.",
        "emoji": "🌸",
        "tags": [
          "Light",
          "Nutritious"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 240,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 38,
          "fats": 6,
          "protein_pct": 22,
          "carbs_pct": 78,
          "fats_pct": 18
        },
        "benefits": [
          "Makhana high in magnesium",
          "Milk tryptophan for sleep",
          "Saffron mood-lifting",
          "Nourishing"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Chicken Soup",
        "description": "Light chicken broth with ginger, garlic, turmeric and vegetables.",
        "emoji": "🍜",
        "tags": [
          "Healing",
          "Protein-rich"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 200,
        "prep_time": "40 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 20,
          "carbs": 12,
          "fats": 6,
          "protein_pct": 60,
          "carbs_pct": 30,
          "fats_pct": 18
        },
        "benefits": [
          "Proven to reduce fatigue",
          "Steam opens nasal passages",
          "Protein for recovery",
          "Electrolytes"
        ],
        "avoid_if": [
          "Vegetarians",
          "Chicken allergy"
        ]
      },
      {
        "name": "Sooji Halwa",
        "description": "Quick semolina dessert with dry fruits and ghee.",
        "emoji": "🟡",
        "tags": [
          "Quick",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 55,
          "fats": 10,
          "protein_pct": 12,
          "carbs_pct": 90,
          "fats_pct": 30
        },
        "benefits": [
          "Quick energy from carbs",
          "Dry fruits add nutrition",
          "Ghee for absorption",
          "Instant comfort"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Nachni Ladoo",
        "description": "Finger millet ladoos with jaggery, ghee and nuts.",
        "emoji": "🟤",
        "tags": [
          "Superfood",
          "Natural Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 30,
          "fats": 6,
          "protein_pct": 14,
          "carbs_pct": 72,
          "fats_pct": 20
        },
        "benefits": [
          "Calcium powerhouse grain",
          "Iron for energy",
          "Jaggery for fuel",
          "Gluten-free"
        ],
        "avoid_if": [
          "Kidney stones"
        ]
      },
      {
        "name": "Peanut Chikki",
        "description": "Crunchy peanut and jaggery brittle - instant energy.",
        "emoji": "🍬",
        "tags": [
          "Natural Energy",
          "Crunchy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 28,
          "fats": 10,
          "protein_pct": 24,
          "carbs_pct": 65,
          "fats_pct": 30
        },
        "benefits": [
          "Iron from jaggery combats tiredness",
          "Protein from peanuts",
          "Natural energy boost",
          "Magnesium"
        ],
        "avoid_if": [
          "Peanut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Kanji Rice Gruel",
        "description": "Thin rice gruel with jeera water - gentlest food when tired.",
        "emoji": "🍚",
        "tags": [
          "Ultra-gentle",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 120,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 26,
          "fats": 0,
          "protein_pct": 8,
          "carbs_pct": 72,
          "fats_pct": 2
        },
        "benefits": [
          "Most digestible food",
          "Electrolytes from jeera",
          "Prevents dehydration",
          "Traditional tired-day food"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      }
    ]
  },
  "romantic": {
    "emoji": "❤️",
    "color": "#FF6B9D",
    "tagline": "Special Indian flavors crafted for love and togetherness.",
    "foods": [
      {
        "name": "Shahi Paneer",
        "description": "Paneer in rich saffron-cream cashew gravy - the most royal dish.",
        "emoji": "🧀",
        "tags": [
          "Rich",
          "Royal",
          "Romantic"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 420,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 22,
          "fats": 28,
          "protein_pct": 42,
          "carbs_pct": 38,
          "fats_pct": 75
        },
        "benefits": [
          "Saffron proven aphrodisiac",
          "High protein from paneer",
          "Cashews for mood",
          "Calcium"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Nut allergy"
        ]
      },
      {
        "name": "Mutton Biryani",
        "description": "Slow-cooked dum biryani with aged basmati and saffron.",
        "emoji": "🍛",
        "tags": [
          "Royal",
          "Aromatic",
          "Special"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 580,
        "prep_time": "90 mins",
        "difficulty": "Hard",
        "best_time": "Dinner (Special)",
        "mood_score": 5,
        "nutrition": {
          "protein": 32,
          "carbs": 68,
          "fats": 18,
          "protein_pct": 78,
          "carbs_pct": 90,
          "fats_pct": 55
        },
        "benefits": [
          "Saffron lifts mood",
          "Whole spices aphrodisiac",
          "High protein",
          "Aromatic experience"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol"
        ]
      },
      {
        "name": "Gulab Jamun with Rabri",
        "description": "Soft gulab jamuns topped with thickened milk and rose petals.",
        "emoji": "🍮",
        "tags": [
          "Romantic",
          "Sweet",
          "Special"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 480,
        "prep_time": "40 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 72,
          "fats": 18,
          "protein_pct": 18,
          "carbs_pct": 95,
          "fats_pct": 55
        },
        "benefits": [
          "Rose water romantic",
          "Serotonin from sweetness",
          "Milk calcium",
          "Special occasion"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Prawn Masala",
        "description": "Juicy prawns in spicy coastal masala.",
        "emoji": "🍤",
        "tags": [
          "Spicy",
          "Coastal",
          "Special"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 320,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 5,
        "nutrition": {
          "protein": 28,
          "carbs": 10,
          "fats": 16,
          "protein_pct": 75,
          "carbs_pct": 22,
          "fats_pct": 50
        },
        "benefits": [
          "Zinc in prawns boosts libido",
          "Omega-3 for heart",
          "High protein",
          "Iodine for thyroid"
        ],
        "avoid_if": [
          "Shellfish allergy",
          "High cholesterol"
        ]
      },
      {
        "name": "Phirni",
        "description": "Set ground rice pudding in earthen pots with saffron and rose.",
        "emoji": "🍯",
        "tags": [
          "Romantic",
          "Fragrant"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 300,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 8,
          "protein_pct": 18,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Saffron natural antidepressant",
          "Rose water promotes romance",
          "Calcium",
          "Mood-lifting"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Dal Makhani",
        "description": "Slow-cooked black dal simmered overnight with butter and cream.",
        "emoji": "🫕",
        "tags": [
          "Rich",
          "Creamy",
          "Romantic"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 420,
        "prep_time": "8 hours",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 16,
          "carbs": 52,
          "fats": 18,
          "protein_pct": 38,
          "carbs_pct": 80,
          "fats_pct": 55
        },
        "benefits": [
          "Protein from black lentils",
          "Iron-rich",
          "Butter boosts mood",
          "Slow-cooked complexity"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Tandoori Chicken",
        "description": "Whole chicken marinated in yogurt spices grilled in tandoor.",
        "emoji": "🍗",
        "tags": [
          "Grilled",
          "Special",
          "High Protein"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 350,
        "prep_time": "3 hours",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 38,
          "carbs": 8,
          "fats": 16,
          "protein_pct": 92,
          "carbs_pct": 18,
          "fats_pct": 48
        },
        "benefits": [
          "High protein for stamina",
          "Spices aphrodisiac",
          "Low fat method",
          "Dramatic presentation"
        ],
        "avoid_if": [
          "Vegetarians",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Kesar Peda",
        "description": "Saffron-flavored milk fudge with pistachios - traditional gift.",
        "emoji": "🟡",
        "tags": [
          "Saffron",
          "Sweet",
          "Gift"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 200,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 32,
          "fats": 8,
          "protein_pct": 14,
          "carbs_pct": 78,
          "fats_pct": 24
        },
        "benefits": [
          "Saffron mood-enhancer",
          "Milk calcium",
          "Pistachios vitamin E",
          "Symbol of affection"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Kerala Fish Curry",
        "description": "Tangy coconut-based fish curry with raw mango.",
        "emoji": "🐟",
        "tags": [
          "Coastal",
          "Romantic",
          "Aromatic"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 340,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 30,
          "carbs": 12,
          "fats": 18,
          "protein_pct": 78,
          "carbs_pct": 25,
          "fats_pct": 55
        },
        "benefits": [
          "Omega-3 for heart and mood",
          "Coconut medium chain fats",
          "Iodine for thyroid",
          "Coastal cuisine"
        ],
        "avoid_if": [
          "Fish allergy",
          "Pregnant women"
        ]
      },
      {
        "name": "Ras Malai",
        "description": "Soft cottage cheese dumplings in saffron cardamom cream.",
        "emoji": "🫙",
        "tags": [
          "Delicate",
          "Sweet",
          "Romantic"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 280,
        "prep_time": "45 mins",
        "difficulty": "Hard",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 9,
          "carbs": 42,
          "fats": 10,
          "protein_pct": 22,
          "carbs_pct": 82,
          "fats_pct": 30
        },
        "benefits": [
          "Saffron antidepressant",
          "Protein from paneer",
          "Rose water calming",
          "Special occasion"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Chicken Malai Tikka",
        "description": "Cream-marinated chicken tikka - silky, mild and elegant.",
        "emoji": "🍢",
        "tags": [
          "Mild",
          "Creamy",
          "Elegant"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 300,
        "prep_time": "3 hours",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 35,
          "carbs": 6,
          "fats": 14,
          "protein_pct": 88,
          "carbs_pct": 14,
          "fats_pct": 42
        },
        "benefits": [
          "High protein",
          "Cream adds richness",
          "Elegant presentation",
          "Low carb"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Vegetarians"
        ]
      },
      {
        "name": "Thandai",
        "description": "Chilled spiced milk with rose petals, almonds and saffron.",
        "emoji": "🥛",
        "tags": [
          "Festive",
          "Fragrant",
          "Romantic"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 38,
          "fats": 12,
          "protein_pct": 22,
          "carbs_pct": 78,
          "fats_pct": 38
        },
        "benefits": [
          "Rose water symbol of love",
          "Saffron antidepressant",
          "Almonds mood-booster",
          "Traditional romantic drink"
        ],
        "avoid_if": [
          "Nut allergy",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Seekh Kebab",
        "description": "Minced lamb kebabs with aromatic spices on skewers.",
        "emoji": "🥩",
        "tags": [
          "Smoky",
          "Aromatic",
          "High Protein"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 340,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 30,
          "carbs": 8,
          "fats": 20,
          "protein_pct": 78,
          "carbs_pct": 18,
          "fats_pct": 62
        },
        "benefits": [
          "High protein",
          "Spices aphrodisiac",
          "Zinc from lamb",
          "Smoky aroma"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol"
        ]
      },
      {
        "name": "Mango Shrikhand",
        "description": "Strained yogurt dessert with Alphonso mango and cardamom.",
        "emoji": "🥭",
        "tags": [
          "Sweet",
          "Creamy",
          "Seasonal"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 42,
          "fats": 6,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 18
        },
        "benefits": [
          "Mango Vitamin C",
          "Probiotics from yogurt",
          "Protein from strained curd",
          "Summer romance"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Paneer Tikka Masala",
        "description": "Grilled paneer in rich tomato-cream masala.",
        "emoji": "🧀",
        "tags": [
          "Restaurant-style",
          "Rich",
          "Special"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 460,
        "prep_time": "40 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 22,
          "carbs": 28,
          "fats": 28,
          "protein_pct": 52,
          "carbs_pct": 48,
          "fats_pct": 78
        },
        "benefits": [
          "High protein from paneer",
          "Lycopene from tomatoes",
          "Calcium",
          "Special occasion"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Falooda",
        "description": "Rose milk with basil seeds, vermicelli, ice cream and jelly.",
        "emoji": "🍧",
        "tags": [
          "Sweet",
          "Unique",
          "Special Drink"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 380,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 62,
          "fats": 12,
          "protein_pct": 14,
          "carbs_pct": 90,
          "fats_pct": 35
        },
        "benefits": [
          "Rose syrup calming and romantic",
          "Basil seeds cooling",
          "Visual appeal",
          "Unique Indian experience"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Reshmi Kebab",
        "description": "Silky minced chicken kebabs with cream cheese and saffron.",
        "emoji": "🍢",
        "tags": [
          "Silky",
          "Romantic",
          "Rich"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 320,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 32,
          "carbs": 8,
          "fats": 18,
          "protein_pct": 82,
          "carbs_pct": 18,
          "fats_pct": 55
        },
        "benefits": [
          "High protein",
          "Cream adds richness",
          "Saffron mood-enhancing",
          "Elegant presentation"
        ],
        "avoid_if": [
          "Vegetarians",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Lauki Halwa",
        "description": "Bottle gourd slow-cooked with milk, sugar and dry fruits.",
        "emoji": "🥗",
        "tags": [
          "Light",
          "Sweet",
          "Healthy Dessert"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 280,
        "prep_time": "40 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 3,
        "nutrition": {
          "protein": 6,
          "carbs": 48,
          "fats": 8,
          "protein_pct": 16,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Lauki cooling and calming",
          "Milk calcium",
          "Lower calorie dessert",
          "Digestive"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Coconut Barfi",
        "description": "Delicate coconut sweet with cardamom and silver leaf.",
        "emoji": "🤍",
        "tags": [
          "Sweet",
          "Delicate",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 250,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 38,
          "fats": 12,
          "protein_pct": 8,
          "carbs_pct": 82,
          "fats_pct": 38
        },
        "benefits": [
          "Coconut mood-boosting",
          "Sweet gesture of love",
          "Energy from medium chain fats",
          "Traditional romantic gift"
        ],
        "avoid_if": [
          "Diabetic",
          "Coconut allergy"
        ]
      },
      {
        "name": "Doodh Peda",
        "description": "Soft milk fudge sweets with cardamom - traditional mithai.",
        "emoji": "🟡",
        "tags": [
          "Traditional Mithai",
          "Sweet",
          "Gift"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 200,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 32,
          "fats": 8,
          "protein_pct": 14,
          "carbs_pct": 78,
          "fats_pct": 24
        },
        "benefits": [
          "Traditional mithai nostalgia",
          "Milk calcium",
          "Cardamom digestive",
          "Gifting memories"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Modak",
        "description": "Sweet steamed dumplings with coconut and jaggery filling.",
        "emoji": "🍡",
        "tags": [
          "Sweet",
          "Special",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 38,
          "fats": 6,
          "protein_pct": 8,
          "carbs_pct": 85,
          "fats_pct": 18
        },
        "benefits": [
          "Jaggery iron",
          "Coconut mood-lifting",
          "Gluten-free steamed",
          "Traditional love offering"
        ],
        "avoid_if": [
          "Coconut allergy",
          "Diabetic"
        ]
      }
    ]
  },
  "anxious": {
    "emoji": "😰",
    "color": "#7EC8C8",
    "tagline": "Gentle Indian foods to quiet your mind and calm your nerves.",
    "foods": [
      {
        "name": "Haldi Doodh",
        "description": "Warm milk with turmeric, ginger and honey - India anxiety remedy.",
        "emoji": "🥛",
        "tags": [
          "Calming",
          "Traditional",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 140,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 18,
          "fats": 5,
          "protein_pct": 20,
          "carbs_pct": 45,
          "fats_pct": 18
        },
        "benefits": [
          "Curcumin reduces anxiety proven",
          "Tryptophan promotes calm",
          "Ginger reduces cortisol",
          "Ancient Ayurvedic remedy"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Blood thinners"
        ]
      },
      {
        "name": "Moong Dal Khichdi",
        "description": "Soft moong dal and rice with ghee - the most gentle Indian meal.",
        "emoji": "🍲",
        "tags": [
          "Gentle",
          "Easy Digest",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 45,
          "fats": 6,
          "protein_pct": 35,
          "carbs_pct": 80,
          "fats_pct": 20
        },
        "benefits": [
          "Tryptophan boosts serotonin",
          "Easy on nervous stomach",
          "Ghee feeds nervous system",
          "Ayurvedic sattvic food"
        ],
        "avoid_if": [
          "Legume intolerance"
        ]
      },
      {
        "name": "Tulsi Kadha",
        "description": "Holy basil decoction with ginger, cloves and honey.",
        "emoji": "🍵",
        "tags": [
          "Herbal",
          "Sacred",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 25,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 5,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 15,
          "fats_pct": 2
        },
        "benefits": [
          "Tulsi proven adaptogen",
          "Reduces cortisol significantly",
          "Ginger calms nerves",
          "Sacred plant comfort"
        ],
        "avoid_if": [
          "Blood thinners",
          "Pregnant women"
        ]
      },
      {
        "name": "Ashwagandha Milk",
        "description": "Warm milk with ashwagandha powder, honey and nutmeg.",
        "emoji": "🥛",
        "tags": [
          "Adaptogen",
          "Anxiety-reducing"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 180,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 22,
          "fats": 6,
          "protein_pct": 18,
          "carbs_pct": 52,
          "fats_pct": 18
        },
        "benefits": [
          "Ashwagandha proven anxiety reducer",
          "Reduces cortisol up to 30%",
          "Tryptophan for calm",
          "Nutmeg sedative"
        ],
        "avoid_if": [
          "Pregnant women",
          "Thyroid medication",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Curd Rice",
        "description": "Soft rice with yogurt and mild tempering.",
        "emoji": "🍚",
        "tags": [
          "Cooling",
          "Probiotic",
          "Gentle"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 290,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 48,
          "fats": 5,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 16
        },
        "benefits": [
          "Gut-brain axis probiotics reduce anxiety",
          "Cooling for anxious mind",
          "Carbs boost serotonin",
          "Traditional calming food"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Banana Walnut Smoothie",
        "description": "Blended banana with walnuts, milk and honey.",
        "emoji": "🍌",
        "tags": [
          "Soothing",
          "Omega-3",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 48,
          "fats": 14,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 42
        },
        "benefits": [
          "Banana serotonin precursor",
          "Walnuts omega-3 reduce anxiety",
          "Magnesium calms nervous system",
          "B6 for GABA"
        ],
        "avoid_if": [
          "Nut allergy",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Makhana Roasted",
        "description": "Lightly roasted lotus seeds with ghee and rock salt.",
        "emoji": "🌸",
        "tags": [
          "Light",
          "Crunchy",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 160,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 9,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 28,
          "carbs_pct": 65,
          "fats_pct": 6
        },
        "benefits": [
          "Magnesium reduces anxiety",
          "Low calorie calming snack",
          "Kavalactones calm nerves",
          "Ayurvedic nerve tonic"
        ],
        "avoid_if": [
          "Rarely contraindicated"
        ]
      },
      {
        "name": "Oats with Banana",
        "description": "Warm oats topped with banana slices and drizzled honey.",
        "emoji": "🌾",
        "tags": [
          "Grounding",
          "Warm",
          "Steady Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 280,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 52,
          "fats": 4,
          "protein_pct": 22,
          "carbs_pct": 88,
          "fats_pct": 12
        },
        "benefits": [
          "Oats contain tryptophan",
          "Slow carbs prevent blood sugar anxiety",
          "Banana magnesium calms",
          "Grounding breakfast"
        ],
        "avoid_if": [
          "Oat/gluten sensitivity"
        ]
      },
      {
        "name": "Vegetable Khichdi",
        "description": "Mixed vegetable rice and dal porridge - sattvic and grounding.",
        "emoji": "🫕",
        "tags": [
          "Sattvic",
          "Grounding",
          "Gentle"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 52,
          "fats": 6,
          "protein_pct": 32,
          "carbs_pct": 82,
          "fats_pct": 18
        },
        "benefits": [
          "Sattvic food calms mind",
          "Vegetables add B vitamins",
          "Ghee nourishes nervous system",
          "Easy on anxious stomach"
        ],
        "avoid_if": [
          "Legume intolerance"
        ]
      },
      {
        "name": "Pomegranate Juice",
        "description": "Fresh pomegranate juice - antioxidant powerhouse.",
        "emoji": "🔴",
        "tags": [
          "Antioxidant",
          "Fresh",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 120,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 2,
          "carbs": 26,
          "fats": 1,
          "protein_pct": 6,
          "carbs_pct": 68,
          "fats_pct": 4
        },
        "benefits": [
          "Reduces oxidative stress",
          "Lowers blood pressure and anxiety",
          "Vitamin C reduces cortisol",
          "Punicalagins powerful antioxidants"
        ],
        "avoid_if": [
          "Blood pressure medication",
          "Kidney disease"
        ]
      },
      {
        "name": "Ragi Porridge",
        "description": "Finger millet porridge with milk, jaggery and cardamom.",
        "emoji": "🟤",
        "tags": [
          "Calcium-rich",
          "Calming",
          "Grounding"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 260,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 48,
          "fats": 4,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 12
        },
        "benefits": [
          "Highest calcium grain calms nervous system",
          "Tryptophan for serotonin",
          "Magnesium muscle relaxant",
          "Gluten-free"
        ],
        "avoid_if": [
          "Kidney stones"
        ]
      },
      {
        "name": "Coconut Ladoo",
        "description": "Simple coconut and condensed milk ladoos with cardamom.",
        "emoji": "🤍",
        "tags": [
          "Sweet",
          "Simple",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 180,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 28,
          "fats": 8,
          "protein_pct": 8,
          "carbs_pct": 72,
          "fats_pct": 24
        },
        "benefits": [
          "Coconut medium chain fats for brain",
          "Sweetness triggers serotonin",
          "Cardamom reduces anxiety",
          "Simple comfort food"
        ],
        "avoid_if": [
          "Diabetic",
          "Coconut allergy"
        ]
      },
      {
        "name": "Dahi Plain",
        "description": "Fresh homemade yogurt with a drizzle of honey.",
        "emoji": "🥣",
        "tags": [
          "Probiotic",
          "Simple",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 140,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 14,
          "fats": 4,
          "protein_pct": 32,
          "carbs_pct": 40,
          "fats_pct": 14
        },
        "benefits": [
          "Probiotics proven anxiety reducers",
          "GABA production from fermentation",
          "Protein for stable mood",
          "Simple and calming"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Lauki Soup",
        "description": "Light bottle gourd soup with jeera and coriander.",
        "emoji": "🟢",
        "tags": [
          "Ultra-light",
          "Sattvic",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 80,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 2,
          "carbs": 12,
          "fats": 3,
          "protein_pct": 8,
          "carbs_pct": 38,
          "fats_pct": 10
        },
        "benefits": [
          "Lauki most cooling in Ayurveda",
          "Reduces body heat and anxiety",
          "Light on nervous stomach",
          "Traditional anxiety food"
        ],
        "avoid_if": [
          "Bitter lauki - can be toxic"
        ]
      },
      {
        "name": "Saffron Rice Pudding",
        "description": "Light rice kheer with saffron and rose water.",
        "emoji": "🍚",
        "tags": [
          "Soothing",
          "Fragrant",
          "Gentle"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 240,
        "prep_time": "30 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 40,
          "fats": 6,
          "protein_pct": 16,
          "carbs_pct": 80,
          "fats_pct": 18
        },
        "benefits": [
          "Saffron clinical proven antidepressant",
          "Crocin reduces anxiety symptoms",
          "Milk tryptophan for calm",
          "Rose water calming aroma"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Green Tea Tulsi",
        "description": "Green tea brewed with holy basil and honey.",
        "emoji": "🍵",
        "tags": [
          "Antioxidant",
          "Calming",
          "Herbal"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 15,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 3,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 10,
          "fats_pct": 2
        },
        "benefits": [
          "L-theanine promotes calm alertness",
          "Tulsi adaptogen reduces stress",
          "Antioxidants reduce inflammation",
          "Low caffeine"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Blood thinners"
        ]
      },
      {
        "name": "Methi Tea",
        "description": "Fenugreek seed tea with honey - traditional remedy.",
        "emoji": "🫖",
        "tags": [
          "Traditional",
          "Herbal",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 15,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 3,
        "nutrition": {
          "protein": 0,
          "carbs": 3,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 8,
          "fats_pct": 2
        },
        "benefits": [
          "Fenugreek reduces blood sugar anxiety",
          "Magnesium calms nerves",
          "Traditional Ayurvedic remedy",
          "Anti-inflammatory"
        ],
        "avoid_if": [
          "Pregnant women",
          "Blood thinners",
          "Diabetic medication"
        ]
      },
      {
        "name": "Alsi Ladoo",
        "description": "Roasted flaxseed ladoos with jaggery.",
        "emoji": "🟤",
        "tags": [
          "Omega-3",
          "Traditional",
          "Calming"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 25,
          "fats": 9,
          "protein_pct": 14,
          "carbs_pct": 62,
          "fats_pct": 28
        },
        "benefits": [
          "Flaxseed highest plant omega-3",
          "Reduces anxiety inflammation",
          "Lignans balance hormones",
          "Traditional anxiety remedy"
        ],
        "avoid_if": [
          "Blood thinners",
          "Hormone-sensitive"
        ]
      },
      {
        "name": "Buttermilk",
        "description": "Thin spiced yogurt drink with jeera and rock salt.",
        "emoji": "🥛",
        "tags": [
          "Cooling",
          "Probiotic",
          "Digestive"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Afternoon",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 6,
          "fats": 1,
          "protein_pct": 28,
          "carbs_pct": 30,
          "fats_pct": 8
        },
        "benefits": [
          "Probiotics reduce gut anxiety",
          "Digestive aid reduces bloating",
          "Cooling for tense mind",
          "Very low calorie"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Warm Chamomile Oats",
        "description": "Slow-cooked oats with chamomile-infused milk and honey.",
        "emoji": "🌾",
        "tags": [
          "Calming",
          "Gentle",
          "Nourishing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 290,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 9,
          "carbs": 48,
          "fats": 5,
          "protein_pct": 25,
          "carbs_pct": 85,
          "fats_pct": 16
        },
        "benefits": [
          "Chamomile reduces anxiety",
          "Oats contain tryptophan",
          "Honey stabilizes blood sugar",
          "Grounding morning ritual"
        ],
        "avoid_if": [
          "Oat/gluten sensitivity",
          "Chamomile allergy"
        ]
      },
      {
        "name": "Sprouts Chaat",
        "description": "Mixed sprouted legumes with lemon and chaat masala.",
        "emoji": "🌱",
        "tags": [
          "Healthy",
          "Light",
          "Nutritious"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 3,
        "nutrition": {
          "protein": 12,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 38,
          "carbs_pct": 65,
          "fats_pct": 6
        },
        "benefits": [
          "Very high protein",
          "B vitamins for nervous system",
          "Fiber stabilizes blood sugar",
          "Zinc for mood"
        ],
        "avoid_if": [
          "IBS",
          "Kidney disease"
        ]
      }
    ]
  },
  "sick": {
    "emoji": "🤒",
    "color": "#90BE6D",
    "tagline": "Healing Indian foods to nurse you back to health.",
    "foods": [
      {
        "name": "Ginger Lemon Honey Tea",
        "description": "Hot ginger tea with fresh lemon juice, raw honey and black pepper.",
        "emoji": "🍋",
        "tags": [
          "Healing",
          "Immunity",
          "Soothing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 45,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 11,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 30,
          "fats_pct": 2
        },
        "benefits": [
          "Ginger most potent anti-nausea agent",
          "Honey antibacterial",
          "Vitamin C boosts immunity",
          "Warmth soothes sore throat"
        ],
        "avoid_if": [
          "Acid reflux",
          "Blood thinners"
        ]
      },
      {
        "name": "Moong Dal Khichdi",
        "description": "Light moong dal rice porridge with turmeric and ghee - India sick food.",
        "emoji": "🍲",
        "tags": [
          "Healing",
          "Easy Digest",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 260,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 42,
          "fats": 5,
          "protein_pct": 35,
          "carbs_pct": 80,
          "fats_pct": 16
        },
        "benefits": [
          "Easiest food to digest when sick",
          "Turmeric powerful healer",
          "Protein for recovery",
          "Ghee soothes intestines"
        ],
        "avoid_if": [
          "Legume allergy"
        ]
      },
      {
        "name": "Yakhni Chicken Soup",
        "description": "Clear bone broth with ginger, garlic and aromatic spices.",
        "emoji": "🍜",
        "tags": [
          "Healing",
          "Warm",
          "Protein-rich"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 160,
        "prep_time": "60 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 8,
          "fats": 5,
          "protein_pct": 55,
          "carbs_pct": 20,
          "fats_pct": 16
        },
        "benefits": [
          "Scientifically proven reduces cold",
          "Steam opens nasal passages",
          "Electrolytes prevent dehydration",
          "Collagen heals gut"
        ],
        "avoid_if": [
          "Vegetarians",
          "Chicken allergy"
        ]
      },
      {
        "name": "Tulsi Ginger Kadha",
        "description": "Traditional immunity decoction - tulsi, ginger, cloves, black pepper.",
        "emoji": "🫖",
        "tags": [
          "Immunity",
          "Traditional",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 30,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "2-3 times daily when sick",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 6,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 18,
          "fats_pct": 2
        },
        "benefits": [
          "Tulsi antiviral and antibacterial",
          "Ginger anti-nausea and warming",
          "Cloves antibacterial",
          "Black pepper bioavailability booster"
        ],
        "avoid_if": [
          "Blood thinners",
          "Pregnant women"
        ]
      },
      {
        "name": "Haldi Doodh",
        "description": "Golden milk with turmeric, ginger and black pepper.",
        "emoji": "🥛",
        "tags": [
          "Anti-inflammatory",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 150,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 16,
          "fats": 6,
          "protein_pct": 18,
          "carbs_pct": 42,
          "fats_pct": 20
        },
        "benefits": [
          "Curcumin powerful anti-inflammatory",
          "Reduces fever-causing inflammation",
          "Ginger antibacterial",
          "Traditional healing drink"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Blood thinners"
        ]
      },
      {
        "name": "Coconut Water",
        "description": "Fresh tender coconut water - nature ORS for sick body.",
        "emoji": "🥥",
        "tags": [
          "Hydrating",
          "Electrolytes",
          "Natural ORS"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Anytime when sick",
        "mood_score": 5,
        "nutrition": {
          "protein": 1,
          "carbs": 14,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 42,
          "fats_pct": 2
        },
        "benefits": [
          "Natural electrolytes better than ORS",
          "Cytokinins boost immunity",
          "Prevents dehydration from fever",
          "Easily absorbed when sick"
        ],
        "avoid_if": [
          "High potassium",
          "Kidney disease"
        ]
      },
      {
        "name": "Banana Curd Rice",
        "description": "Soft curd rice with ripe banana - gentle on sick stomach.",
        "emoji": "🍌",
        "tags": [
          "BRAT Diet",
          "Gentle",
          "Probiotic"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 260,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 48,
          "fats": 3,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 10
        },
        "benefits": [
          "BRAT diet approved for illness",
          "Banana pectin soothes gut",
          "Probiotics restore flora",
          "Potassium from banana"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Severe diarrhea"
        ]
      },
      {
        "name": "Amla Juice",
        "description": "Indian gooseberry juice with honey - highest natural Vitamin C.",
        "emoji": "🟢",
        "tags": [
          "Vitamin C",
          "Immunity"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 12,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 38,
          "fats_pct": 2
        },
        "benefits": [
          "20x more Vitamin C than oranges",
          "Antioxidants fight infection",
          "Iron absorption booster",
          "Ayurvedic immunity tonic"
        ],
        "avoid_if": [
          "Severe acid reflux",
          "Blood thinners"
        ]
      },
      {
        "name": "Rice Kanji Ganji",
        "description": "Thin rice gruel with jeera water - gentlest food when very sick.",
        "emoji": "🍚",
        "tags": [
          "Ultra-gentle",
          "Traditional",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 120,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Anytime when sick",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 26,
          "fats": 0,
          "protein_pct": 8,
          "carbs_pct": 72,
          "fats_pct": 2
        },
        "benefits": [
          "Most digestible food possible",
          "Electrolytes from jeera water",
          "Prevents dehydration",
          "Traditional sick food"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      },
      {
        "name": "Sabudana Khichdi",
        "description": "Light sago khichdi - gentle on sick stomach.",
        "emoji": "⚪",
        "tags": [
          "Gentle",
          "Gluten-free",
          "Easy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 340,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 62,
          "fats": 9,
          "protein_pct": 16,
          "carbs_pct": 90,
          "fats_pct": 26
        },
        "benefits": [
          "Gluten-free easy digestion",
          "Gentle on sick stomach",
          "Peanuts protein",
          "Quick energy for recovery"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      },
      {
        "name": "Nimbu Pani Warm",
        "description": "Warm lemon water with rock salt and honey.",
        "emoji": "🍋",
        "tags": [
          "Hydrating",
          "Vitamin C",
          "Alkalizing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 30,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 7,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 20,
          "fats_pct": 2
        },
        "benefits": [
          "Vitamin C boosts immunity",
          "Alkalizes body pH when sick",
          "Hydration with electrolytes",
          "Detoxifying"
        ],
        "avoid_if": [
          "Severe acid reflux",
          "Tooth enamel sensitivity"
        ]
      },
      {
        "name": "Ginger Adrak Chai",
        "description": "Strong ginger tea with milk and minimal sugar.",
        "emoji": "☕",
        "tags": [
          "Warming",
          "Anti-nausea"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 60,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 2,
          "carbs": 10,
          "fats": 2,
          "protein_pct": 8,
          "carbs_pct": 38,
          "fats_pct": 8
        },
        "benefits": [
          "Gingerols most potent anti-nausea",
          "Opens nasal congestion",
          "Warms cold sick body",
          "Traditional sick day drink"
        ],
        "avoid_if": [
          "Acid reflux",
          "Blood thinners"
        ]
      },
      {
        "name": "Boiled Potato with Salt",
        "description": "Plain boiled potato with rock salt and jeera - BRAT approved.",
        "emoji": "🥔",
        "tags": [
          "BRAT Diet",
          "Bland",
          "Gentle"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 120,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Anytime when sick",
        "mood_score": 3,
        "nutrition": {
          "protein": 3,
          "carbs": 26,
          "fats": 0,
          "protein_pct": 8,
          "carbs_pct": 72,
          "fats_pct": 2
        },
        "benefits": [
          "BRAT diet staple",
          "Potassium replaces lost minerals",
          "Easy to digest bland food",
          "Gentle on nauseous stomach"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      },
      {
        "name": "Mulethi Tea",
        "description": "Licorice root tea with honey - traditional sore throat remedy.",
        "emoji": "🍵",
        "tags": [
          "Sore Throat",
          "Herbal",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 20,
        "prep_time": "8 mins",
        "difficulty": "Easy",
        "best_time": "2-3 times when sick",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 4,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 12,
          "fats_pct": 2
        },
        "benefits": [
          "Licorice antiviral properties",
          "Soothes sore throat",
          "Anti-inflammatory for respiratory",
          "Traditional remedy"
        ],
        "avoid_if": [
          "High blood pressure",
          "Pregnant women",
          "Heart conditions"
        ]
      },
      {
        "name": "Soft Idli Sambhar",
        "description": "Extra-soft steamed idlis with thin lentil soup.",
        "emoji": "🫓",
        "tags": [
          "Soft",
          "Easy Digest",
          "Protein-rich"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 260,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 46,
          "fats": 3,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 10
        },
        "benefits": [
          "Fermented probiotic",
          "Protein from lentils",
          "Light and easy to digest",
          "South Indian sick food"
        ],
        "avoid_if": [
          "Rice allergy"
        ]
      },
      {
        "name": "Jeera Water",
        "description": "Boiled cumin seed water - traditional digestive remedy.",
        "emoji": "🫖",
        "tags": [
          "Digestive",
          "Traditional",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 10,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 2,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 6,
          "fats_pct": 2
        },
        "benefits": [
          "Relieves nausea and indigestion",
          "Antibacterial properties",
          "Reduces gas and bloating",
          "Ancient remedy"
        ],
        "avoid_if": [
          "Rarely contraindicated"
        ]
      },
      {
        "name": "Thin Moong Dal Soup",
        "description": "Very thin moong dal water with minimal spices.",
        "emoji": "🍵",
        "tags": [
          "Ultra-gentle",
          "Protein",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 150,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 22,
          "fats": 1,
          "protein_pct": 32,
          "carbs_pct": 60,
          "fats_pct": 4
        },
        "benefits": [
          "Most digestible protein source",
          "Zinc boosts immune response",
          "Prevents muscle wasting",
          "Traditional sick food"
        ],
        "avoid_if": [
          "Legume allergy"
        ]
      },
      {
        "name": "Suji Kheer",
        "description": "Light semolina pudding with cardamom and raisins.",
        "emoji": "🍮",
        "tags": [
          "Gentle",
          "Sweet",
          "Easy"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 240,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Meals when sick",
        "mood_score": 3,
        "nutrition": {
          "protein": 6,
          "carbs": 42,
          "fats": 6,
          "protein_pct": 16,
          "carbs_pct": 82,
          "fats_pct": 18
        },
        "benefits": [
          "Easy to eat with sore throat",
          "Milk calcium for recovery",
          "Raisins natural iron",
          "Comforting when ill"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Sattu Drink Salted",
        "description": "Roasted gram flour in water with lemon and rock salt.",
        "emoji": "🥤",
        "tags": [
          "Electrolytes",
          "Protein",
          "Rehydrating"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 130,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Anytime when sick",
        "mood_score": 3,
        "nutrition": {
          "protein": 10,
          "carbs": 20,
          "fats": 2,
          "protein_pct": 32,
          "carbs_pct": 55,
          "fats_pct": 6
        },
        "benefits": [
          "Electrolyte replacement",
          "Protein for immunity",
          "Cooling for fever",
          "Traditional sick drink"
        ],
        "avoid_if": [
          "Chickpea allergy"
        ]
      },
      {
        "name": "Daliya Soup",
        "description": "Thin broken wheat soup with minimal spices.",
        "emoji": "🌾",
        "tags": [
          "Gentle",
          "Wholesome",
          "Recovery"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch when sick",
        "mood_score": 3,
        "nutrition": {
          "protein": 6,
          "carbs": 32,
          "fats": 3,
          "protein_pct": 18,
          "carbs_pct": 75,
          "fats_pct": 10
        },
        "benefits": [
          "Whole grain gentle recovery food",
          "B vitamins for immunity",
          "Easy to digest",
          "Warming when feverish"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Plain Rice with Ghee",
        "description": "Soft boiled rice with a teaspoon of ghee and rock salt.",
        "emoji": "🍚",
        "tags": [
          "Simplest Sick Food",
          "Easy Digest"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 280,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Anytime when sick",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 58,
          "fats": 5,
          "protein_pct": 12,
          "carbs_pct": 88,
          "fats_pct": 16
        },
        "benefits": [
          "Easiest food possible when sick",
          "Ghee soothes gut lining",
          "Rice provides gentle energy",
          "Rock salt electrolytes"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      }
    ]
  },
  "motivated": {
    "emoji": "💪",
    "color": "#2DC653",
    "tagline": "Power foods to fuel your fire and keep you going!",
    "foods": [
      {
        "name": "Egg White Bhurji",
        "description": "Scrambled egg whites with vegetables and minimal oil.",
        "emoji": "🍳",
        "tags": [
          "High Protein",
          "Low Fat",
          "Power"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 180,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 24,
          "carbs": 8,
          "fats": 4,
          "protein_pct": 72,
          "carbs_pct": 18,
          "fats_pct": 12
        },
        "benefits": [
          "Purest protein source",
          "Choline for focus and memory",
          "Zero fat",
          "B12 for energy metabolism"
        ],
        "avoid_if": [
          "Egg allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Chana Masala",
        "description": "Spicy North Indian chickpea curry - protein powerhouse.",
        "emoji": "🫘",
        "tags": [
          "High Protein",
          "Filling",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 58,
          "fats": 8,
          "protein_pct": 45,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Highest plant protein",
          "Iron prevents energy crashes",
          "Complex carbs for stamina",
          "Zinc"
        ],
        "avoid_if": [
          "IBS",
          "Kidney disease"
        ]
      },
      {
        "name": "Grilled Chicken Seekh Kebab",
        "description": "Minced chicken kebabs grilled with minimal oil.",
        "emoji": "🍗",
        "tags": [
          "High Protein",
          "Lean",
          "Power"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 280,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 35,
          "carbs": 5,
          "fats": 12,
          "protein_pct": 92,
          "carbs_pct": 12,
          "fats_pct": 38
        },
        "benefits": [
          "Highest protein",
          "Complete amino acids",
          "Iron for oxygen",
          "B12 for energy"
        ],
        "avoid_if": [
          "Vegetarians"
        ]
      },
      {
        "name": "Sattu Paratha",
        "description": "High-protein roasted gram stuffed flatbread.",
        "emoji": "🫓",
        "tags": [
          "High Protein",
          "Traditional",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 350,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 16,
          "carbs": 52,
          "fats": 8,
          "protein_pct": 42,
          "carbs_pct": 84,
          "fats_pct": 24
        },
        "benefits": [
          "Sattu highest plant protein",
          "Iron-rich",
          "Cooling energy food",
          "Sustained power"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Chickpea allergy"
        ]
      },
      {
        "name": "Peanut Butter Banana Smoothie",
        "description": "Thick peanut butter and banana blended with milk.",
        "emoji": "🥤",
        "tags": [
          "Pre-workout",
          "Protein",
          "Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 420,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Pre-workout",
        "mood_score": 5,
        "nutrition": {
          "protein": 16,
          "carbs": 58,
          "fats": 14,
          "protein_pct": 42,
          "carbs_pct": 88,
          "fats_pct": 42
        },
        "benefits": [
          "Banana quick energy",
          "Peanut butter protein",
          "Milk for recovery",
          "Potassium prevents cramps"
        ],
        "avoid_if": [
          "Peanut allergy",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Quinoa Khichdi",
        "description": "Quinoa cooked with dal and vegetables.",
        "emoji": "🌾",
        "tags": [
          "Complete Protein",
          "Modern",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 52,
          "fats": 6,
          "protein_pct": 38,
          "carbs_pct": 85,
          "fats_pct": 18
        },
        "benefits": [
          "Quinoa has all 9 amino acids",
          "Complete plant protein",
          "Iron prevents energy crashes",
          "Fiber for fuel"
        ],
        "avoid_if": [
          "Quinoa intolerance"
        ]
      },
      {
        "name": "Ragi Mudde with Sambhar",
        "description": "Dense finger millet balls with lentil soup.",
        "emoji": "🟤",
        "tags": [
          "Superfood",
          "Calcium",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 380,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 72,
          "fats": 4,
          "protein_pct": 28,
          "carbs_pct": 92,
          "fats_pct": 12
        },
        "benefits": [
          "Highest calcium grain",
          "Iron for energy",
          "Slow release energy",
          "Gluten-free power"
        ],
        "avoid_if": [
          "Kidney stones"
        ]
      },
      {
        "name": "Fish Tikka Grilled",
        "description": "Marinated fish fillets grilled with minimal oil.",
        "emoji": "🐟",
        "tags": [
          "Omega-3",
          "Lean Protein",
          "Power"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 240,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 30,
          "carbs": 5,
          "fats": 10,
          "protein_pct": 80,
          "carbs_pct": 12,
          "fats_pct": 32
        },
        "benefits": [
          "Omega-3 boosts brain and mood",
          "High lean protein",
          "Iodine for thyroid",
          "Selenium for performance"
        ],
        "avoid_if": [
          "Fish allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Dry Fruit Power Mix",
        "description": "Almonds, walnuts, cashews, raisins, pumpkin seeds.",
        "emoji": "🥜",
        "tags": [
          "Power Snack",
          "Omega-3",
          "Natural Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 260,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Pre-workout",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 25,
          "fats": 18,
          "protein_pct": 22,
          "carbs_pct": 55,
          "fats_pct": 55
        },
        "benefits": [
          "Complete nutrition profile",
          "Healthy fats for sustained energy",
          "Protein for muscle",
          "Zinc and selenium"
        ],
        "avoid_if": [
          "Nut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Palak Paneer",
        "description": "Iron-rich spinach with high protein paneer.",
        "emoji": "🥬",
        "tags": [
          "Iron",
          "Protein",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 340,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 18,
          "carbs": 16,
          "fats": 20,
          "protein_pct": 48,
          "carbs_pct": 32,
          "fats_pct": 62
        },
        "benefits": [
          "Iron + protein combo for energy",
          "Folate for red blood cells",
          "Calcium from paneer",
          "Vitamin K"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Kidney stones"
        ]
      },
      {
        "name": "Sprouts Chaat",
        "description": "Mixed sprouted legumes with chaat masala.",
        "emoji": "🌱",
        "tags": [
          "Raw Protein",
          "Vitamin C",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 180,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 38,
          "carbs_pct": 68,
          "fats_pct": 6
        },
        "benefits": [
          "Protein increases when sprouted",
          "Enzymes aid absorption",
          "Vitamin C sky-rockets in sprouts",
          "Iron for oxygen"
        ],
        "avoid_if": [
          "IBS",
          "Kidney disease"
        ]
      },
      {
        "name": "Black Coffee Filter",
        "description": "Strong south Indian filter coffee - motivation in a cup.",
        "emoji": "☕",
        "tags": [
          "Focus",
          "Energy",
          "Pre-workout"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 10,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 2,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 6,
          "fats_pct": 2
        },
        "benefits": [
          "Caffeine boosts focus and alertness",
          "Dopamine release enhances motivation",
          "Improves physical performance 11%",
          "Antioxidants"
        ],
        "avoid_if": [
          "Anxiety sufferers",
          "Acid reflux",
          "Pregnant women"
        ]
      },
      {
        "name": "Rajma Chawal",
        "description": "Protein-rich kidney bean curry with rice.",
        "emoji": "🍛",
        "tags": [
          "Complete Protein",
          "Iron",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 440,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 18,
          "carbs": 70,
          "fats": 6,
          "protein_pct": 42,
          "carbs_pct": 90,
          "fats_pct": 18
        },
        "benefits": [
          "Iron + plant protein combo",
          "Complex carbs for sustained energy",
          "Fiber slows energy release",
          "Zinc"
        ],
        "avoid_if": [
          "Kidney disease",
          "IBS"
        ]
      },
      {
        "name": "Soya Keema",
        "description": "Textured soya protein cooked like minced meat with spices.",
        "emoji": "🟤",
        "tags": [
          "Plant Protein",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 22,
          "carbs": 22,
          "fats": 8,
          "protein_pct": 62,
          "carbs_pct": 48,
          "fats_pct": 24
        },
        "benefits": [
          "Highest plant protein source",
          "Isoflavones for balance",
          "Iron from soya",
          "Complete amino acids"
        ],
        "avoid_if": [
          "Soy allergy",
          "Hypothyroidism"
        ]
      },
      {
        "name": "Mutton Rogan Josh",
        "description": "Aromatic Kashmiri mutton curry with whole spices.",
        "emoji": "🍖",
        "tags": [
          "High Iron",
          "Rich",
          "Power"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 420,
        "prep_time": "60 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 38,
          "carbs": 10,
          "fats": 26,
          "protein_pct": 92,
          "carbs_pct": 22,
          "fats_pct": 78
        },
        "benefits": [
          "Highest iron in red meat",
          "Complete protein",
          "Zinc boosts testosterone",
          "B12 for energy"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol",
          "Gout"
        ]
      },
      {
        "name": "Pumpkin Seeds Mix",
        "description": "Roasted pumpkin seeds with almonds and dark chocolate.",
        "emoji": "🌰",
        "tags": [
          "Zinc",
          "Magnesium",
          "Power Snack"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 200,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 14,
          "fats": 14,
          "protein_pct": 30,
          "carbs_pct": 35,
          "fats_pct": 42
        },
        "benefits": [
          "Zinc highest in pumpkin seeds",
          "Magnesium for muscle function",
          "Healthy fats for power",
          "Iron for oxygen"
        ],
        "avoid_if": [
          "Seed allergy"
        ]
      },
      {
        "name": "Dahi Vada",
        "description": "Lentil fritters in yogurt with chutneys.",
        "emoji": "🫙",
        "tags": [
          "Protein",
          "Probiotic",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 300,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 42,
          "fats": 8,
          "protein_pct": 38,
          "carbs_pct": 80,
          "fats_pct": 24
        },
        "benefits": [
          "Dal protein + yogurt protein combo",
          "Probiotics for gut energy",
          "Tamarind aids digestion",
          "Satisfying"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Chana Dal",
        "description": "Simple protein-rich yellow lentil with spices.",
        "emoji": "🟡",
        "tags": [
          "High Protein",
          "Iron",
          "Simple"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 15,
          "carbs": 42,
          "fats": 4,
          "protein_pct": 42,
          "carbs_pct": 80,
          "fats_pct": 12
        },
        "benefits": [
          "Highest split-lentil protein",
          "Iron for oxygen",
          "B vitamins for metabolism",
          "Fiber"
        ],
        "avoid_if": [
          "Legume intolerance",
          "IBS"
        ]
      },
      {
        "name": "Paneer Bhurji with Roti",
        "description": "Scrambled paneer with rotis - quick protein meal.",
        "emoji": "🧀",
        "tags": [
          "Quick Protein",
          "Filling",
          "Power"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 420,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 22,
          "carbs": 48,
          "fats": 16,
          "protein_pct": 55,
          "carbs_pct": 80,
          "fats_pct": 48
        },
        "benefits": [
          "High protein from paneer",
          "Roti complex carbs",
          "Calcium for bones",
          "Quick to prepare"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Nachni Ragi Ladoo",
        "description": "Finger millet ladoos with jaggery and nuts.",
        "emoji": "🟤",
        "tags": [
          "Superfood",
          "Natural Energy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 30,
          "fats": 6,
          "protein_pct": 14,
          "carbs_pct": 72,
          "fats_pct": 20
        },
        "benefits": [
          "Calcium powerhouse grain",
          "Iron for energy",
          "Jaggery for fuel",
          "Gluten-free"
        ],
        "avoid_if": [
          "Kidney stones"
        ]
      },
      {
        "name": "Ghee Roast Dosa",
        "description": "Crispy dosa roasted in ghee with coconut chutney.",
        "emoji": "🫓",
        "tags": [
          "Crispy",
          "Energizing",
          "South Indian"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 380,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 62,
          "fats": 12,
          "protein_pct": 18,
          "carbs_pct": 88,
          "fats_pct": 35
        },
        "benefits": [
          "Fermented probiotic energy",
          "Ghee medium chain fats for brain",
          "Carbs for sustained energy",
          "Iron from fermented rice"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      }
    ]
  },
  "nostalgic": {
    "emoji": "🥹",
    "color": "#E9C46A",
    "tagline": "Classic Indian flavors that take you back in time.",
    "foods": [
      {
        "name": "Aloo Paratha with Makhan",
        "description": "Crispy potato paratha with white butter, pickle and lassi.",
        "emoji": "🫓",
        "tags": [
          "Classic",
          "Homestyle",
          "Punjabi"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 480,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 9,
          "carbs": 68,
          "fats": 18,
          "protein_pct": 22,
          "carbs_pct": 90,
          "fats_pct": 55
        },
        "benefits": [
          "Nostalgia strongest mood-lifter",
          "Butter fat-soluble vitamins",
          "Comfort food serotonin",
          "Potato quick energy"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Maggi Masala",
        "description": "The iconic 2-minute noodles of every Indian childhood.",
        "emoji": "🍜",
        "tags": [
          "Iconic",
          "Nostalgic",
          "2-Minute"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 10,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 32
        },
        "benefits": [
          "Strongest nostalgia trigger in India",
          "Iron-fortified",
          "Instant happiness",
          "Every Indian memory"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Low sodium"
        ]
      },
      {
        "name": "Gulab Jamun",
        "description": "Soft milk solid balls in rose cardamom syrup.",
        "emoji": "🍮",
        "tags": [
          "Festival",
          "Classic",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 350,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 58,
          "fats": 12,
          "protein_pct": 15,
          "carbs_pct": 90,
          "fats_pct": 38
        },
        "benefits": [
          "Strongest childhood memory food",
          "Rose water calming",
          "Serotonin from sweetness",
          "Festival joy"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Masala Chai with Biscuit",
        "description": "Strong masala chai with cardamom and milk - dunked biscuits.",
        "emoji": "☕",
        "tags": [
          "Iconic",
          "Daily Ritual",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 160,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 4,
          "carbs": 28,
          "fats": 4,
          "protein_pct": 12,
          "carbs_pct": 65,
          "fats_pct": 12
        },
        "benefits": [
          "Most universal Indian nostalgic food",
          "Chai ritual is meditative",
          "Cardamom antioxidant",
          "Ginger digestive"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Rajma Chawal Sunday Special",
        "description": "Red kidney bean curry with rice - every Punjabi Sunday meal.",
        "emoji": "🍛",
        "tags": [
          "Sunday Special",
          "Comfort",
          "Punjabi Classic"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 440,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Sunday Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 18,
          "carbs": 70,
          "fats": 6,
          "protein_pct": 42,
          "carbs_pct": 90,
          "fats_pct": 18
        },
        "benefits": [
          "Sunday lunch nostalgia",
          "High plant protein",
          "Iron-rich",
          "Comfort food"
        ],
        "avoid_if": [
          "Kidney disease",
          "IBS"
        ]
      },
      {
        "name": "Dal Baati Churma",
        "description": "Baked wheat balls with dal and sweet churma - Rajasthani classic.",
        "emoji": "🫙",
        "tags": [
          "Rajasthani",
          "Traditional",
          "Special"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 580,
        "prep_time": "60 mins",
        "difficulty": "Hard",
        "best_time": "Lunch (Special)",
        "mood_score": 5,
        "nutrition": {
          "protein": 16,
          "carbs": 80,
          "fats": 22,
          "protein_pct": 38,
          "carbs_pct": 92,
          "fats_pct": 65
        },
        "benefits": [
          "Traditional recipe nostalgia",
          "Dal protein",
          "Ghee for satiety",
          "Regional pride"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High calorie"
        ]
      },
      {
        "name": "Hot Jalebi",
        "description": "Crispy fresh jalebis straight from the kadhai with rabri.",
        "emoji": "🌀",
        "tags": [
          "Crispy",
          "Hot",
          "Festival Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 3,
          "carbs": 62,
          "fats": 10,
          "protein_pct": 8,
          "carbs_pct": 92,
          "fats_pct": 30
        },
        "benefits": [
          "Festival and fair nostalgia",
          "Saffron mood-lifting",
          "Instant energy boost",
          "Pure joy"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Sabudana Vada",
        "description": "Crispy sago and peanut fritters - Maharashtra fasting food.",
        "emoji": "🔵",
        "tags": [
          "Crispy",
          "Maharashtra",
          "Fasting Food"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 280,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 48,
          "fats": 10,
          "protein_pct": 18,
          "carbs_pct": 85,
          "fats_pct": 30
        },
        "benefits": [
          "Peanuts protein",
          "Navratri and fasting memories",
          "Gluten-free",
          "Crispy joy"
        ],
        "avoid_if": [
          "Peanut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Kadhi Chawal",
        "description": "Tangy yogurt kadhi with pakoras over steamed rice.",
        "emoji": "🍲",
        "tags": [
          "Comfort",
          "Homestyle",
          "Weekly Meal"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 58,
          "fats": 12,
          "protein_pct": 24,
          "carbs_pct": 88,
          "fats_pct": 35
        },
        "benefits": [
          "Probiotics from yogurt",
          "Gram flour protein",
          "Comfort food nostalgia",
          "Warm home feeling"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Gajar Halwa",
        "description": "Slow-cooked carrot halwa - winter must-have in North India.",
        "emoji": "🥕",
        "tags": [
          "Winter Special",
          "Sweet",
          "Homemade"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 340,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 58,
          "fats": 12,
          "protein_pct": 14,
          "carbs_pct": 90,
          "fats_pct": 35
        },
        "benefits": [
          "Beta-carotene boost",
          "Winter nostalgia",
          "Milk calcium",
          "Slow-cooked love"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Poha Kanda Batata",
        "description": "Flattened rice with onions, potatoes, peanuts and lime.",
        "emoji": "🍚",
        "tags": [
          "Morning Staple",
          "Quick",
          "Western India"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 260,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 46,
          "fats": 7,
          "protein_pct": 18,
          "carbs_pct": 85,
          "fats_pct": 22
        },
        "benefits": [
          "Iron-fortified",
          "School morning nostalgia",
          "Light and energizing",
          "Quick"
        ],
        "avoid_if": [
          "Peanut allergy"
        ]
      },
      {
        "name": "Idli Sambhar Mom Style",
        "description": "Soft idlis with hot sambhar and coconut chutney.",
        "emoji": "🫓",
        "tags": [
          "South Indian",
          "Wholesome",
          "Morning Comfort"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 48,
          "fats": 4,
          "protein_pct": 28,
          "carbs_pct": 82,
          "fats_pct": 12
        },
        "benefits": [
          "Fermented probiotic",
          "South Indian home nostalgia",
          "Protein from lentils",
          "Light morning meal"
        ],
        "avoid_if": [
          "Rice allergy"
        ]
      },
      {
        "name": "Vada Pav",
        "description": "Mumbai soul food - potato vada in pav with dry garlic chutney.",
        "emoji": "🍔",
        "tags": [
          "Mumbai Classic",
          "Street Food",
          "Iconic"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 300,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 11,
          "protein_pct": 16,
          "carbs_pct": 88,
          "fats_pct": 32
        },
        "benefits": [
          "Mumbai nostalgia",
          "Quick energy",
          "Spices boost mood",
          "Most beloved street food"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High BP"
        ]
      },
      {
        "name": "Suji Halwa Prasad",
        "description": "Sweet semolina halwa with ghee - sacred temple prasad.",
        "emoji": "🟡",
        "tags": [
          "Sacred",
          "Sweet",
          "Temple Food"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 350,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 58,
          "fats": 14,
          "protein_pct": 12,
          "carbs_pct": 90,
          "fats_pct": 42
        },
        "benefits": [
          "Sacred prasad deep emotional comfort",
          "Cardamom calming",
          "Serotonin from sweetness",
          "Ghee nourishment"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Chole Puri",
        "description": "Fluffy puri with spicy chickpea curry - Sunday special.",
        "emoji": "🍳",
        "tags": [
          "Sunday Special",
          "Festive",
          "Indulgent"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 550,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Sunday Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 14,
          "carbs": 78,
          "fats": 22,
          "protein_pct": 30,
          "carbs_pct": 92,
          "fats_pct": 65
        },
        "benefits": [
          "Sunday celebration nostalgia",
          "Chickpea protein",
          "Iron-rich",
          "Festival happiness"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Namak Para",
        "description": "Crispy salted diamond-shaped snacks - homemade jar staple.",
        "emoji": "🟡",
        "tags": [
          "Homemade",
          "Crunchy",
          "Jar Snack"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 220,
        "prep_time": "30 mins",
        "difficulty": "Easy",
        "best_time": "Tea-time",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 35,
          "fats": 8,
          "protein_pct": 14,
          "carbs_pct": 78,
          "fats_pct": 24
        },
        "benefits": [
          "Grandmother kitchen nostalgia",
          "Crunching relieves stress",
          "Simple comfort food",
          "Homemade love"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Low sodium"
        ]
      },
      {
        "name": "Meetha Paan",
        "description": "Betel leaf stuffed with gulkand, coconut and fennel.",
        "emoji": "🌿",
        "tags": [
          "After-meal",
          "Digestive",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 80,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "After Meals",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 18,
          "fats": 1,
          "protein_pct": 4,
          "carbs_pct": 55,
          "fats_pct": 4
        },
        "benefits": [
          "Fennel digestive aid",
          "Gulkand cooling and mood-lifting",
          "After-meal ritual nostalgia",
          "Betel leaf antibacterial"
        ],
        "avoid_if": [
          "Pregnant women",
          "Betel nut addicts"
        ]
      },
      {
        "name": "Matar Kulcha",
        "description": "White flour buns with spicy dried peas curry - Delhi street food.",
        "emoji": "🫔",
        "tags": [
          "Delhi Street Food",
          "Spicy",
          "Classic"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 420,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 72,
          "fats": 10,
          "protein_pct": 28,
          "carbs_pct": 90,
          "fats_pct": 30
        },
        "benefits": [
          "Delhi street food nostalgia",
          "Protein from matar",
          "Iron-rich peas",
          "Spice mood-booster"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Acid reflux"
        ]
      },
      {
        "name": "Kheer Rice Pudding",
        "description": "Creamy rice pudding with saffron and cardamom.",
        "emoji": "🍚",
        "tags": [
          "Festival",
          "Classic",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "40 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 55,
          "fats": 10,
          "protein_pct": 20,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Festival and celebration nostalgia",
          "Saffron lifts mood",
          "Calcium from milk",
          "Sweetness boosts serotonin"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Atta Halwa Prasad",
        "description": "Whole wheat flour halwa with ghee - sacred temple prasad.",
        "emoji": "🟤",
        "tags": [
          "Sacred",
          "Prasad",
          "Warmth"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 380,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 55,
          "fats": 16,
          "protein_pct": 12,
          "carbs_pct": 88,
          "fats_pct": 48
        },
        "benefits": [
          "Temple prasad deepest comfort",
          "Ghee nourishes and warms",
          "Sacred sweetness reduces emptiness",
          "Spiritual connection"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Churma Ladoo",
        "description": "Whole wheat ladoos with ghee and jaggery - Rajasthani home sweet.",
        "emoji": "🟤",
        "tags": [
          "Wholesome",
          "Home Sweet",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 260,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 40,
          "fats": 10,
          "protein_pct": 12,
          "carbs_pct": 82,
          "fats_pct": 30
        },
        "benefits": [
          "Home sweet memories",
          "Ghee warmth",
          "Jaggery iron",
          "Whole wheat nutrition"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Diabetic"
        ]
      }
    ]
  },
  "lonely": {
    "emoji": "🥺",
    "color": "#A8DADC",
    "tagline": "Warm comforting Indian foods to make you feel held.",
    "foods": [
      {
        "name": "Dal Chawal with Ghee",
        "description": "Simple yellow dal and rice with generous ghee - mother cooking.",
        "emoji": "🍛",
        "tags": [
          "Homely",
          "Comforting",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 400,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 14,
          "carbs": 60,
          "fats": 10,
          "protein_pct": 35,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Mother cooking feeling",
          "Tryptophan promotes serotonin",
          "Ghee comfort effect",
          "Complete amino acids"
        ],
        "avoid_if": [
          "Legume intolerance"
        ]
      },
      {
        "name": "Maggi at Midnight",
        "description": "Classic Maggi noodles - universal Indian lonely night companion.",
        "emoji": "🍜",
        "tags": [
          "Midnight Snack",
          "Comfort",
          "Quick"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Night",
        "mood_score": 5,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 10,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 32
        },
        "benefits": [
          "Universal comfort food",
          "Nostalgia reduces loneliness",
          "Quick to make alone",
          "Iron-fortified"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Low sodium"
        ]
      },
      {
        "name": "Chai with Parle-G",
        "description": "Hot masala chai with iconic Parle-G biscuit.",
        "emoji": "☕",
        "tags": [
          "Iconic Duo",
          "Comfort",
          "Daily Ritual"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 180,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 4,
          "carbs": 32,
          "fats": 5,
          "protein_pct": 10,
          "carbs_pct": 78,
          "fats_pct": 15
        },
        "benefits": [
          "Chai ritual creates comfort",
          "Dunking biscuit meditative",
          "Warmth reduces loneliness",
          "India most familiar taste"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Haldi Doodh",
        "description": "Warm golden milk - traditional Indian bedtime comfort.",
        "emoji": "🥛",
        "tags": [
          "Warm",
          "Comforting",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 160,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Evening",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 18,
          "fats": 6,
          "protein_pct": 18,
          "carbs_pct": 45,
          "fats_pct": 20
        },
        "benefits": [
          "Tryptophan in milk for serotonin",
          "Warmth reduces emotional coldness",
          "Curcumin anti-depressant",
          "Bedtime hug in a cup"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Blood thinners"
        ]
      },
      {
        "name": "Khichdi with Pickle",
        "description": "Comfort khichdi with tangy mango pickle.",
        "emoji": "🍲",
        "tags": [
          "Comfort",
          "Home",
          "Simple"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 340,
        "prep_time": "25 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 55,
          "fats": 8,
          "protein_pct": 32,
          "carbs_pct": 85,
          "fats_pct": 24
        },
        "benefits": [
          "Comfort food reduces loneliness",
          "Complete nutrition",
          "Ghee for warmth",
          "Simple home cooking"
        ],
        "avoid_if": [
          "Legume intolerance"
        ]
      },
      {
        "name": "Roti with Ghee and Sugar",
        "description": "Soft roti rolled with ghee and sprinkled with sugar.",
        "emoji": "🫓",
        "tags": [
          "Simplest Comfort",
          "Sweet",
          "Childhood"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 260,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 48,
          "fats": 8,
          "protein_pct": 14,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Simplest comfort food ever",
          "Sweet taste serotonin boost",
          "Ghee warmth",
          "Childhood memory"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Samosa with Chai",
        "description": "Crispy samosas with hot masala chai - perfect pair.",
        "emoji": "🔺",
        "tags": [
          "Classic Duo",
          "Comfort",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 360,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Tea-time",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 52,
          "fats": 14,
          "protein_pct": 14,
          "carbs_pct": 85,
          "fats_pct": 42
        },
        "benefits": [
          "Most comforting food pair",
          "Shared or solo happiness",
          "Spices mood-lifting",
          "Street food warmth"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Pav Bhaji",
        "description": "Buttery mashed vegetable curry with toasted pav buns.",
        "emoji": "🍞",
        "tags": [
          "Buttery",
          "Warm",
          "Filling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 460,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 70,
          "fats": 16,
          "protein_pct": 22,
          "carbs_pct": 90,
          "fats_pct": 48
        },
        "benefits": [
          "Butter comfort effect",
          "Vegetables provide nutrients",
          "Street food memories",
          "Satisfying comfort meal"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Kadhi Chawal",
        "description": "Tangy kadhi with pakoras over rice.",
        "emoji": "🍲",
        "tags": [
          "Comfort",
          "Homestyle",
          "Warm"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 58,
          "fats": 12,
          "protein_pct": 24,
          "carbs_pct": 88,
          "fats_pct": 35
        },
        "benefits": [
          "Probiotics calm gut-brain",
          "Besan protein",
          "Warm comfort for lonely evenings",
          "Home cooking feeling"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Kheer",
        "description": "Creamy rice pudding with saffron - festival warmth.",
        "emoji": "🍚",
        "tags": [
          "Sweet",
          "Warm",
          "Festival Feeling"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "40 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 55,
          "fats": 10,
          "protein_pct": 20,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Festival memory warmth",
          "Serotonin from sweetness",
          "Saffron mood-lifting",
          "Milk calcium"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Makhani Dal Slow Cooked",
        "description": "Overnight slow-cooked black dal in butter and cream.",
        "emoji": "🫕",
        "tags": [
          "Slow Cooked",
          "Rich",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 440,
        "prep_time": "Overnight",
        "difficulty": "Medium",
        "best_time": "Dinner",
        "mood_score": 5,
        "nutrition": {
          "protein": 16,
          "carbs": 52,
          "fats": 20,
          "protein_pct": 36,
          "carbs_pct": 80,
          "fats_pct": 58
        },
        "benefits": [
          "Slow-cooked love reduces loneliness",
          "Black lentil iron",
          "Protein for wellbeing",
          "Butter comfort effect"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Besan Ka Sheera",
        "description": "Roasted gram flour halwa with ghee and jaggery.",
        "emoji": "🟡",
        "tags": [
          "Sweet",
          "Warm",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 300,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 45,
          "fats": 12,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 36
        },
        "benefits": [
          "Warmth reduces loneliness",
          "Protein from besan",
          "Jaggery iron",
          "Grandmother remedy"
        ],
        "avoid_if": [
          "Diabetic",
          "Chickpea allergy"
        ]
      },
      {
        "name": "Moong Dal Halwa",
        "description": "Rich slow-cooked moong dal halwa with ghee and dry fruits.",
        "emoji": "🟡",
        "tags": [
          "Rich",
          "Winter",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 420,
        "prep_time": "45 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 10,
          "carbs": 55,
          "fats": 18,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 52
        },
        "benefits": [
          "Protein from moong dal",
          "Winter celebration memories",
          "Ghee nourishment",
          "Rich comfort food"
        ],
        "avoid_if": [
          "Diabetic",
          "High cholesterol"
        ]
      },
      {
        "name": "Dosa with Extra Butter",
        "description": "Crispy masala dosa with extra butter and chutneys.",
        "emoji": "🫓",
        "tags": [
          "Crispy",
          "South Indian",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 420,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 64,
          "fats": 14,
          "protein_pct": 18,
          "carbs_pct": 88,
          "fats_pct": 42
        },
        "benefits": [
          "Butter comfort effect",
          "Fermented probiotic",
          "Crispy texture mood-lifting",
          "South Indian comfort"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Phirni",
        "description": "Set ground rice pudding in earthen pots.",
        "emoji": "🍯",
        "tags": [
          "Earthen Pot",
          "Fragrant",
          "Special"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 300,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 8,
          "protein_pct": 18,
          "carbs_pct": 88,
          "fats_pct": 24
        },
        "benefits": [
          "Saffron antidepressant",
          "Rose water calming",
          "Special occasion memories",
          "Warmth in every bite"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Sabudana Khichdi",
        "description": "Sago pearl khichdi with peanuts - fasting comfort food.",
        "emoji": "⚪",
        "tags": [
          "Fasting Food",
          "Comfort",
          "Light"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 380,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 68,
          "fats": 10,
          "protein_pct": 18,
          "carbs_pct": 92,
          "fats_pct": 28
        },
        "benefits": [
          "Navratri fasting memories",
          "Gluten-free comfort",
          "Peanuts protein",
          "Quick energy"
        ],
        "avoid_if": [
          "Diabetic"
        ]
      },
      {
        "name": "Til Gur Ladoo",
        "description": "Sesame and jaggery ladoos - Makar Sankranti warmth.",
        "emoji": "⚫",
        "tags": [
          "Winter Festival",
          "Iron-rich",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Winter",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 28,
          "fats": 10,
          "protein_pct": 14,
          "carbs_pct": 65,
          "fats_pct": 30
        },
        "benefits": [
          "Makar Sankranti warmth",
          "Iron from jaggery",
          "Calcium from sesame",
          "Gifting brings connection"
        ],
        "avoid_if": [
          "Sesame allergy"
        ]
      },
      {
        "name": "Atta Halwa Prasad",
        "description": "Whole wheat flour halwa with ghee - sacred temple prasad.",
        "emoji": "🟤",
        "tags": [
          "Sacred",
          "Prasad",
          "Warmth"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 380,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 5,
        "nutrition": {
          "protein": 6,
          "carbs": 55,
          "fats": 16,
          "protein_pct": 12,
          "carbs_pct": 88,
          "fats_pct": 48
        },
        "benefits": [
          "Temple prasad deepest comfort",
          "Ghee nourishes and warms",
          "Sacred sweetness reduces emptiness",
          "Spiritual connection"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Chole Puri Special",
        "description": "Fluffy puri with spicy chickpea curry.",
        "emoji": "🍳",
        "tags": [
          "Festive",
          "Filling",
          "Comforting"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 550,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Special Days",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 78,
          "fats": 22,
          "protein_pct": 30,
          "carbs_pct": 92,
          "fats_pct": 65
        },
        "benefits": [
          "Celebration food joy",
          "Chickpea protein",
          "Festival memories",
          "Iron-rich"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Lapsi Sweet",
        "description": "Sweet broken wheat cooked with jaggery and ghee.",
        "emoji": "🟤",
        "tags": [
          "Gujarat",
          "Traditional",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 6,
          "carbs": 55,
          "fats": 10,
          "protein_pct": 14,
          "carbs_pct": 88,
          "fats_pct": 30
        },
        "benefits": [
          "Jaggery iron",
          "Whole grain fiber",
          "Warm comfort in winter",
          "Regional home comfort"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Churma Ladoo",
        "description": "Whole wheat ladoos with ghee and jaggery.",
        "emoji": "🟤",
        "tags": [
          "Wholesome",
          "Home Sweet",
          "Rajasthani"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 260,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 40,
          "fats": 10,
          "protein_pct": 12,
          "carbs_pct": 82,
          "fats_pct": 30
        },
        "benefits": [
          "Home sweet memories",
          "Ghee warmth",
          "Jaggery iron",
          "Whole wheat nutrition"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Diabetic"
        ]
      }
    ]
  },
  "bored": {
    "emoji": "😑",
    "color": "#F4A261",
    "tagline": "Fun exciting Indian snacks to spark your taste buds!",
    "foods": [
      {
        "name": "Pani Puri Multiple Flavors",
        "description": "Experiment with hing, jeera, pudina and imli flavored pani puri.",
        "emoji": "🫙",
        "tags": [
          "Fun",
          "Interactive",
          "Street Food"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 160,
        "prep_time": "15 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 30,
          "fats": 3,
          "protein_pct": 18,
          "carbs_pct": 78,
          "fats_pct": 10
        },
        "benefits": [
          "Making and eating is fun activity",
          "Multiple flavors excite palate",
          "Social food",
          "Tamarind digestive"
        ],
        "avoid_if": [
          "Acid reflux",
          "Stomach infections"
        ]
      },
      {
        "name": "Chaat Platter",
        "description": "Papdi chaat, dahi bhalla, aloo tikki and bhel in one platter.",
        "emoji": "🥗",
        "tags": [
          "Variety",
          "Chatpata",
          "Fun Platter"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 450,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 15,
          "carbs": 72,
          "fats": 14,
          "protein_pct": 32,
          "carbs_pct": 90,
          "fats_pct": 40
        },
        "benefits": [
          "Variety excites bored mind",
          "Social eating",
          "Multiple textures and flavors",
          "Probiotics from dahi"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Acid reflux"
        ]
      },
      {
        "name": "Masala Popcorn",
        "description": "Air-popped corn with chaat masala, amchur and butter.",
        "emoji": "🍿",
        "tags": [
          "Crunchy",
          "Low Calorie",
          "Movie Snack"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 180,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Movie",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 30,
          "fats": 5,
          "protein_pct": 12,
          "carbs_pct": 72,
          "fats_pct": 16
        },
        "benefits": [
          "Whole grain fiber",
          "Low calorie snacking",
          "Crunching relieves boredom",
          "Movie time ritual"
        ],
        "avoid_if": [
          "Corn allergy",
          "Acid reflux"
        ]
      },
      {
        "name": "Makhana Flavored Pops",
        "description": "Roasted fox nuts in peri peri, cheese or mint masala.",
        "emoji": "🌸",
        "tags": [
          "Crunchy",
          "Healthy",
          "Flavored"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 160,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 9,
          "carbs": 28,
          "fats": 2,
          "protein_pct": 28,
          "carbs_pct": 65,
          "fats_pct": 6
        },
        "benefits": [
          "Low calorie crunchy snack",
          "Magnesium for mood",
          "Experiment with flavors",
          "Better than chips"
        ],
        "avoid_if": [
          "Rarely contraindicated"
        ]
      },
      {
        "name": "Bhel Puri Homemade",
        "description": "Customize your own bhel with various add-ins and chutneys.",
        "emoji": "🍿",
        "tags": [
          "DIY",
          "Light",
          "Fun"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 38,
          "fats": 5,
          "protein_pct": 14,
          "carbs_pct": 82,
          "fats_pct": 16
        },
        "benefits": [
          "Assembling activity is fun",
          "Customizable for any taste",
          "Low calorie snack",
          "Mumbai nostalgia"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Acid reflux"
        ]
      },
      {
        "name": "Steamed Momos",
        "description": "Steamed dumplings with schezwan sauce - street food craze.",
        "emoji": "🥟",
        "tags": [
          "Trendy",
          "Filling",
          "Street Food"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 14,
          "carbs": 42,
          "fats": 10,
          "protein_pct": 38,
          "carbs_pct": 80,
          "fats_pct": 30
        },
        "benefits": [
          "Making momos is therapeutic",
          "Protein from filling",
          "Dipping sauce excitement",
          "Modern street food"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Corn Chaat Masala",
        "description": "Boiled corn with butter, lime, chaat masala and red chilli.",
        "emoji": "🌽",
        "tags": [
          "Quick",
          "Tangy",
          "Street Food"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 38,
          "fats": 5,
          "protein_pct": 12,
          "carbs_pct": 82,
          "fats_pct": 16
        },
        "benefits": [
          "Fiber beats boredom hunger",
          "Chatpata taste excitement",
          "Low calorie",
          "Quick to make"
        ],
        "avoid_if": [
          "Corn allergy"
        ]
      },
      {
        "name": "Aloo Chaat Crispy",
        "description": "Crispy fried potato chunks with chutneys and spices.",
        "emoji": "🥔",
        "tags": [
          "Chatpata",
          "Crispy",
          "Fun"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 280,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 48,
          "fats": 10,
          "protein_pct": 10,
          "carbs_pct": 85,
          "fats_pct": 30
        },
        "benefits": [
          "Crispy texture excitement",
          "Tamarind digestive",
          "Quick mood-lifter",
          "Street food joy"
        ],
        "avoid_if": [
          "High cholesterol",
          "Diabetic"
        ]
      },
      {
        "name": "Paneer Pakora",
        "description": "Crispy gram flour battered cottage cheese fritters.",
        "emoji": "🧀",
        "tags": [
          "Crispy",
          "Protein-rich",
          "Fun"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 14,
          "carbs": 30,
          "fats": 18,
          "protein_pct": 38,
          "carbs_pct": 65,
          "fats_pct": 52
        },
        "benefits": [
          "High protein snack",
          "Calcium from paneer",
          "Crispy satisfaction",
          "Rain day activity"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Bread Pakora",
        "description": "Potato-stuffed bread dipped in besan batter and fried.",
        "emoji": "🍞",
        "tags": [
          "School Tiffin",
          "Crispy",
          "Nostalgic Fun"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 350,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 5,
        "nutrition": {
          "protein": 9,
          "carbs": 52,
          "fats": 14,
          "protein_pct": 22,
          "carbs_pct": 85,
          "fats_pct": 42
        },
        "benefits": [
          "School tiffin nostalgia",
          "Protein from besan",
          "Fun rainy day activity",
          "Crispy comfort"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Fruit Chaat Spiced",
        "description": "Mixed fruits with chaat masala, black salt and lime.",
        "emoji": "🍎",
        "tags": [
          "Healthy",
          "Tangy",
          "Colorful"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 160,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 2,
          "carbs": 36,
          "fats": 1,
          "protein_pct": 6,
          "carbs_pct": 88,
          "fats_pct": 4
        },
        "benefits": [
          "Vitamins and antioxidants",
          "Colorful and visually exciting",
          "Natural sugar energy",
          "Low calorie"
        ],
        "avoid_if": [
          "Citrus allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Cheese Maggi",
        "description": "Maggi noodles with melted cheese - ultimate guilty pleasure.",
        "emoji": "🍜",
        "tags": [
          "Indulgent",
          "Fusion",
          "Comfort"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 420,
        "prep_time": "7 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 5,
        "nutrition": {
          "protein": 12,
          "carbs": 55,
          "fats": 18,
          "protein_pct": 26,
          "carbs_pct": 85,
          "fats_pct": 52
        },
        "benefits": [
          "Nostalgic happiness",
          "Calcium from cheese",
          "Quick mood lifter",
          "Ultimate comfort fusion"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Medu Vada",
        "description": "Crispy donut-shaped lentil fritters with sambar and chutney.",
        "emoji": "🍩",
        "tags": [
          "South Indian",
          "Crispy",
          "Fun Shape"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 280,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 38,
          "fats": 12,
          "protein_pct": 32,
          "carbs_pct": 78,
          "fats_pct": 36
        },
        "benefits": [
          "Making vadas is therapeutic",
          "Protein from urad dal",
          "Probiotics from sambar",
          "Fun shape and eating"
        ],
        "avoid_if": [
          "Gluten intolerant (usually GF)"
        ]
      },
      {
        "name": "Kachori Chaat",
        "description": "Flaky kachoris topped with chutneys, dahi and sev.",
        "emoji": "🫔",
        "tags": [
          "Flaky",
          "Chatpata",
          "Rajasthani"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 58,
          "fats": 16,
          "protein_pct": 24,
          "carbs_pct": 85,
          "fats_pct": 46
        },
        "benefits": [
          "Lentil protein",
          "Multiple textures excite",
          "Probiotics from dahi",
          "Flaky satisfaction"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Lactose intolerant"
        ]
      },
      {
        "name": "DIY Dosa Experiment",
        "description": "Make dosa with unusual fillings - paneer tikka, pizza style.",
        "emoji": "🫓",
        "tags": [
          "Creative",
          "Interactive",
          "Fusion"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 380,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 60,
          "fats": 12,
          "protein_pct": 22,
          "carbs_pct": 88,
          "fats_pct": 35
        },
        "benefits": [
          "Cooking activity beats boredom",
          "Creative expression",
          "Fermented probiotic",
          "Endless experimentation"
        ],
        "avoid_if": [
          "Gluten intolerant"
        ]
      },
      {
        "name": "Masala Chai Experiment",
        "description": "Try rose, saffron, kashmiri pink or tulsi chai varieties.",
        "emoji": "☕",
        "tags": [
          "Experimental",
          "Flavors",
          "Fun"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 100,
        "prep_time": "8 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 14,
          "fats": 3,
          "protein_pct": 10,
          "carbs_pct": 48,
          "fats_pct": 10
        },
        "benefits": [
          "Experimenting beats boredom",
          "Antioxidants from different spices",
          "Mindful cooking activity",
          "Discovering new flavors"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Egg Muttai Dosa",
        "description": "Crispy dosa with egg cracked on top.",
        "emoji": "🥚",
        "tags": [
          "Quick",
          "Protein",
          "Crispy"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 320,
        "prep_time": "15 mins",
        "difficulty": "Easy",
        "best_time": "Breakfast",
        "mood_score": 4,
        "nutrition": {
          "protein": 16,
          "carbs": 42,
          "fats": 12,
          "protein_pct": 42,
          "carbs_pct": 78,
          "fats_pct": 35
        },
        "benefits": [
          "Protein from egg",
          "Fermented dosa probiotic",
          "Quick boredom buster",
          "South Indian creativity"
        ],
        "avoid_if": [
          "Egg allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Bhakarwadi",
        "description": "Crispy spiral snacks with sweet and spicy filling.",
        "emoji": "🌀",
        "tags": [
          "Crispy",
          "Sweet-Spicy",
          "Maharashtrian"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 240,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 35,
          "fats": 10,
          "protein_pct": 14,
          "carbs_pct": 78,
          "fats_pct": 30
        },
        "benefits": [
          "Unique flavor combination",
          "Spiral shape fun eating",
          "Maharashtrian snack nostalgia",
          "Long-lasting crunch"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "Nut allergy"
        ]
      },
      {
        "name": "Chakli",
        "description": "Crispy spiral rice flour snack with sesame and spices.",
        "emoji": "🌀",
        "tags": [
          "Crispy",
          "Spiral",
          "Festival Snack"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 220,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 35,
          "fats": 10,
          "protein_pct": 12,
          "carbs_pct": 78,
          "fats_pct": 30
        },
        "benefits": [
          "Making chakli is therapeutic",
          "Gluten-free snack option",
          "Festival snack nostalgia",
          "Sesame nutrition"
        ],
        "avoid_if": [
          "Sesame allergy"
        ]
      },
      {
        "name": "Namkeen Mix",
        "description": "Mixed Indian savory snack with sev, chana, peanuts and spices.",
        "emoji": "🥜",
        "tags": [
          "Mixed",
          "Crunchy",
          "Anytime"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 250,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 32,
          "fats": 14,
          "protein_pct": 22,
          "carbs_pct": 72,
          "fats_pct": 42
        },
        "benefits": [
          "Variety fights boredom",
          "Peanuts protein",
          "Crunching relieves tension",
          "Anytime snack"
        ],
        "avoid_if": [
          "Nut allergy",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Golgappa Challenge",
        "description": "Eat 10 golgappas non-stop - ultimate boredom buster!",
        "emoji": "🫙",
        "tags": [
          "Challenge",
          "Fun",
          "Street Food"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 200,
        "prep_time": "15 mins",
        "difficulty": "Medium",
        "best_time": "Challenge",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 38,
          "fats": 4,
          "protein_pct": 15,
          "carbs_pct": 82,
          "fats_pct": 12
        },
        "benefits": [
          "Eating challenge beats boredom",
          "Social fun activity",
          "Tamarind digestion",
          "Pure joy"
        ],
        "avoid_if": [
          "Acid reflux",
          "Stomach infections"
        ]
      }
    ]
  },
  "angry": {
    "emoji": "😠",
    "color": "#E63946",
    "tagline": "Cooling Indian foods to calm your fire and restore peace.",
    "foods": [
      {
        "name": "Coconut Water",
        "description": "Fresh tender coconut water - nature instant anger cooler.",
        "emoji": "🥥",
        "tags": [
          "Cooling",
          "Natural",
          "Instant"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 60,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Immediately",
        "mood_score": 5,
        "nutrition": {
          "protein": 1,
          "carbs": 14,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 42,
          "fats_pct": 2
        },
        "benefits": [
          "Instant cooling effect",
          "Electrolytes balance nervous system",
          "L-citrulline lowers blood pressure",
          "Natural anger management"
        ],
        "avoid_if": [
          "High potassium",
          "Kidney disease"
        ]
      },
      {
        "name": "Aam Panna Cold",
        "description": "Chilled raw mango drink with mint, rock salt and jeera.",
        "emoji": "🥤",
        "tags": [
          "Cooling",
          "Tangy",
          "Refreshing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 80,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 1,
          "carbs": 18,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 55,
          "fats_pct": 2
        },
        "benefits": [
          "Raw mango cooling in Ayurveda",
          "Mint calms nervous system",
          "Prevents heat-related anger",
          "Electrolyte balance"
        ],
        "avoid_if": [
          "Acid reflux",
          "Diabetic"
        ]
      },
      {
        "name": "Cucumber Raita Chilled",
        "description": "Cold yogurt with grated cucumber, roasted cumin and mint.",
        "emoji": "🥒",
        "tags": [
          "Cooling",
          "Probiotic",
          "Calm"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 100,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 10,
          "fats": 3,
          "protein_pct": 20,
          "carbs_pct": 35,
          "fats_pct": 12
        },
        "benefits": [
          "Cucumber most cooling in Ayurveda",
          "Cold yogurt lowers body temperature",
          "Probiotics calm gut-anger",
          "Magnesium calms muscles"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Watermelon Juice",
        "description": "Fresh watermelon blended with mint and black salt.",
        "emoji": "🍉",
        "tags": [
          "Cooling",
          "Hydrating",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 90,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 1,
          "carbs": 20,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 58,
          "fats_pct": 2
        },
        "benefits": [
          "92% water instant cooling",
          "L-citrulline lowers blood pressure",
          "Lycopene anti-inflammatory",
          "Mint calms nervous system"
        ],
        "avoid_if": [
          "Diabetic",
          "Watermelon allergy"
        ]
      },
      {
        "name": "Dark Chocolate 70 percent",
        "description": "High-percentage dark chocolate with a glass of water.",
        "emoji": "🍫",
        "tags": [
          "Magnesium",
          "Calming",
          "Mindful"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 160,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 3,
          "carbs": 16,
          "fats": 12,
          "protein_pct": 8,
          "carbs_pct": 38,
          "fats_pct": 38
        },
        "benefits": [
          "Magnesium reduces anger and irritability",
          "Serotonin boost calms mind",
          "Mindful eating slows anger response",
          "Endorphin release"
        ],
        "avoid_if": [
          "Caffeine sensitive",
          "Migraine patients",
          "Diabetic"
        ]
      },
      {
        "name": "Lauki Sabzi",
        "description": "Light bottle gourd vegetable - Ayurveda anger-cooling food.",
        "emoji": "🟢",
        "tags": [
          "Cooling",
          "Ayurvedic",
          "Light"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 120,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 18,
          "fats": 4,
          "protein_pct": 10,
          "carbs_pct": 55,
          "fats_pct": 14
        },
        "benefits": [
          "Most pitta-cooling food in Ayurveda",
          "Reduces body heat",
          "Calms overheated body",
          "Traditional anger management"
        ],
        "avoid_if": [
          "Bitter lauki - can be toxic"
        ]
      },
      {
        "name": "Nimbu Pani Cold",
        "description": "Cold lemon water with sugar, rock salt - instant calmer.",
        "emoji": "🍋",
        "tags": [
          "Immediate Calming",
          "Electrolytes",
          "Simple"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 50,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Immediately when angry",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 12,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 35,
          "fats_pct": 2
        },
        "benefits": [
          "Holding cold water calms anger",
          "Vitamin C reduces cortisol",
          "Rock salt electrolytes balance",
          "Taking break calms"
        ],
        "avoid_if": [
          "Severe acid reflux"
        ]
      },
      {
        "name": "Rose Sherbet Rooh Afza",
        "description": "Chilled rose syrup drink - India summer cooling tradition.",
        "emoji": "🌹",
        "tags": [
          "Rose",
          "Cooling",
          "Fragrant"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 120,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 5,
        "nutrition": {
          "protein": 0,
          "carbs": 30,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 80,
          "fats_pct": 2
        },
        "benefits": [
          "Rose fragrance proven calming",
          "Cooling red color psychological effect",
          "Tradition of cooling during anger",
          "Instant comfort"
        ],
        "avoid_if": [
          "Diabetic",
          "Rose allergy"
        ]
      },
      {
        "name": "Khus Sherbet",
        "description": "Cooling vetiver grass syrup drink - traditional summer cooler.",
        "emoji": "🟢",
        "tags": [
          "Traditional",
          "Ultra-cooling",
          "Herbal"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 100,
        "prep_time": "2 mins",
        "difficulty": "Easy",
        "best_time": "Summer",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 24,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 65,
          "fats_pct": 2
        },
        "benefits": [
          "Vetiver most cooling herb in Ayurveda",
          "Reduces pitta dramatically",
          "Aromatherapy calming effect",
          "Traditional anger remedy"
        ],
        "avoid_if": [
          "Diabetic",
          "Pregnant women"
        ]
      },
      {
        "name": "Cold Lassi Salted",
        "description": "Chilled salted lassi with roasted cumin.",
        "emoji": "🥛",
        "tags": [
          "Cooling",
          "Probiotic",
          "Immediate"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 140,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Immediately",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 14,
          "fats": 4,
          "protein_pct": 22,
          "carbs_pct": 42,
          "fats_pct": 14
        },
        "benefits": [
          "Cold temp reduces anger arousal",
          "Probiotics calm gut inflammation",
          "Cumin digestive calming",
          "Protein stabilizes mood"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Jaljeera",
        "description": "Spiced cumin drink with mint, tamarind and black salt.",
        "emoji": "🥤",
        "tags": [
          "Digestive",
          "Cooling",
          "Tangy"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 50,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Anytime",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 10,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 30,
          "fats_pct": 2
        },
        "benefits": [
          "Cumin digestive calms gut anger",
          "Mint cooling effect",
          "Tamarind cools pitta",
          "Traditional cooling drink"
        ],
        "avoid_if": [
          "Severe acid reflux"
        ]
      },
      {
        "name": "Mosambi Juice",
        "description": "Fresh sweet lime juice - cooling and alkalizing.",
        "emoji": "🍋",
        "tags": [
          "Citrus",
          "Cooling",
          "Alkalizing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 80,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 18,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 55,
          "fats_pct": 2
        },
        "benefits": [
          "Vitamin C reduces cortisol",
          "Alkalizes acidic angry body",
          "Natural cooling agent",
          "Blood pressure reduction"
        ],
        "avoid_if": [
          "Acid reflux",
          "Kidney stones"
        ]
      },
      {
        "name": "Banana Plain",
        "description": "A simple ripe banana - nature mood stabilizer.",
        "emoji": "🍌",
        "tags": [
          "Simple",
          "Grounding",
          "Natural"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 90,
        "prep_time": "0 mins",
        "difficulty": "Easy",
        "best_time": "Immediately",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 22,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 62,
          "fats_pct": 2
        },
        "benefits": [
          "Serotonin precursor tryptophan",
          "Potassium lowers blood pressure",
          "Natural sugar stabilizes mood",
          "Mindful eating calms anger"
        ],
        "avoid_if": [
          "Diabetic",
          "Latex-fruit syndrome"
        ]
      },
      {
        "name": "Aloe Vera Juice",
        "description": "Fresh aloe vera juice with lemon and honey - cooling detox.",
        "emoji": "🟢",
        "tags": [
          "Cooling",
          "Detox",
          "Healing"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 40,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Morning",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 8,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 22,
          "fats_pct": 2
        },
        "benefits": [
          "Most cooling plant juice",
          "Reduces inflammation from anger",
          "Alkalizes acidic body state",
          "Detoxifying and calming"
        ],
        "avoid_if": [
          "Pregnant women",
          "Diabetic medication",
          "Laxative sensitivity"
        ]
      },
      {
        "name": "Fennel Saunf Tea",
        "description": "Fennel seed tea with honey - traditional anger cooling remedy.",
        "emoji": "🫖",
        "tags": [
          "Herbal",
          "Digestive",
          "Cooling"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 15,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "After Meals",
        "mood_score": 4,
        "nutrition": {
          "protein": 0,
          "carbs": 3,
          "fats": 0,
          "protein_pct": 2,
          "carbs_pct": 8,
          "fats_pct": 2
        },
        "benefits": [
          "Fennel most anti-pitta herb",
          "Anethole calms nervous system",
          "Digestive - anger often from indigestion",
          "Traditional post-anger remedy"
        ],
        "avoid_if": [
          "Estrogen-sensitive",
          "Pregnant women"
        ]
      },
      {
        "name": "Pudina Chutney with Papad",
        "description": "Fresh green mint chutney with crispy papad.",
        "emoji": "🌿",
        "tags": [
          "Cooling",
          "Minty",
          "Fresh"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "Low Carb"
        ],
        "calories": 100,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "With Meals",
        "mood_score": 4,
        "nutrition": {
          "protein": 3,
          "carbs": 14,
          "fats": 2,
          "protein_pct": 12,
          "carbs_pct": 55,
          "fats_pct": 8
        },
        "benefits": [
          "Mint cools body and mind instantly",
          "Menthol calms nervous system",
          "Crunching papad relieves tension",
          "Refreshing taste changes mood"
        ],
        "avoid_if": [
          "GERD sufferers"
        ]
      },
      {
        "name": "Curd Plain Cold",
        "description": "Cold homemade yogurt eaten plain with a pinch of sugar.",
        "emoji": "🥣",
        "tags": [
          "Immediate Cooling",
          "Probiotic",
          "Simple"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 130,
        "prep_time": "1 min",
        "difficulty": "Easy",
        "best_time": "Immediately",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 12,
          "fats": 4,
          "protein_pct": 32,
          "carbs_pct": 38,
          "fats_pct": 14
        },
        "benefits": [
          "Cold temperature cools anger",
          "Probiotics calm inflammation",
          "GABA production reduces anger",
          "Most accessible Indian calmer"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Sattu Sharbat Cold",
        "description": "Cold roasted gram flour drink with lemon and mint.",
        "emoji": "🥤",
        "tags": [
          "Cooling",
          "Protein",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan",
          "High Protein"
        ],
        "calories": 140,
        "prep_time": "3 mins",
        "difficulty": "Easy",
        "best_time": "Summer",
        "mood_score": 4,
        "nutrition": {
          "protein": 10,
          "carbs": 20,
          "fats": 2,
          "protein_pct": 32,
          "carbs_pct": 55,
          "fats_pct": 6
        },
        "benefits": [
          "Cooling for angry body",
          "Protein stabilizes blood sugar anger",
          "Bihar traditional anger-cooling drink",
          "Mint calms nerves"
        ],
        "avoid_if": [
          "Chickpea allergy"
        ]
      },
      {
        "name": "Sabja Basil Seeds Drink",
        "description": "Sweet basil seeds in rose water and cold milk.",
        "emoji": "🫧",
        "tags": [
          "Cooling Gel",
          "Unique",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 120,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Summer",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 16,
          "fats": 3,
          "protein_pct": 14,
          "carbs_pct": 45,
          "fats_pct": 10
        },
        "benefits": [
          "Sabja seeds cool body from inside",
          "Rose water calming aroma",
          "Gel texture mindful eating",
          "Traditional Indian anger cooler"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Pregnant women"
        ]
      },
      {
        "name": "Thandai Non-Bhang",
        "description": "Chilled spiced milk with rose, almonds and fennel seeds.",
        "emoji": "🥛",
        "tags": [
          "Cooling",
          "Festive",
          "Soothing"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 240,
        "prep_time": "15 mins",
        "difficulty": "Medium",
        "best_time": "Evening",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 32,
          "fats": 10,
          "protein_pct": 22,
          "carbs_pct": 72,
          "fats_pct": 30
        },
        "benefits": [
          "Rose water calming",
          "Fennel cooling digestive",
          "Almonds magnesium calms anger",
          "Cold temperature reduces arousal"
        ],
        "avoid_if": [
          "Nut allergy",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Bel Sharbat",
        "description": "Wood apple drink with black salt - traditional pitta cooler.",
        "emoji": "🟡",
        "tags": [
          "Traditional",
          "Ultra-cooling",
          "Pitta Cooler"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 80,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Summer",
        "mood_score": 4,
        "nutrition": {
          "protein": 1,
          "carbs": 18,
          "fats": 0,
          "protein_pct": 4,
          "carbs_pct": 50,
          "fats_pct": 2
        },
        "benefits": [
          "Bel fruit most cooling in Ayurveda",
          "Reduces pitta dosha",
          "Traditional anger management drink",
          "Digestive and cooling"
        ],
        "avoid_if": [
          "Diabetic",
          "Constipation issues"
        ]
      }
    ]
  },
  "excited": {
    "emoji": "🤩",
    "color": "#FF6B35",
    "tagline": "Celebratory Indian flavors to match your electric energy!",
    "foods": [
      {
        "name": "Celebration Biryani",
        "description": "Dum biryani with saffron, fried onions and whole spices.",
        "emoji": "🍛",
        "tags": [
          "Celebration",
          "Aromatic",
          "Special"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 560,
        "prep_time": "90 mins",
        "difficulty": "Hard",
        "best_time": "Celebration Lunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 28,
          "carbs": 72,
          "fats": 16,
          "protein_pct": 65,
          "carbs_pct": 92,
          "fats_pct": 48
        },
        "benefits": [
          "Saffron mood-enhancing",
          "Celebration food joy",
          "Whole spices antioxidants",
          "Aromatic experience"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol"
        ]
      },
      {
        "name": "Paneer Lababdar",
        "description": "Triple-cooked paneer in smoky rich onion-tomato gravy.",
        "emoji": "🧀",
        "tags": [
          "Rich",
          "Celebration",
          "Smoky"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 440,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Dinner",
        "mood_score": 5,
        "nutrition": {
          "protein": 20,
          "carbs": 24,
          "fats": 28,
          "protein_pct": 48,
          "carbs_pct": 42,
          "fats_pct": 78
        },
        "benefits": [
          "High protein celebration food",
          "Smoky flavor excitement",
          "Calcium from paneer",
          "Restaurant-style joy"
        ],
        "avoid_if": [
          "Lactose intolerant"
        ]
      },
      {
        "name": "Chole Bhature Party Size",
        "description": "Huge fluffy bhature with extra spicy chole.",
        "emoji": "🫓",
        "tags": [
          "Party Food",
          "Big",
          "Festive"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 620,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Brunch",
        "mood_score": 5,
        "nutrition": {
          "protein": 16,
          "carbs": 82,
          "fats": 22,
          "protein_pct": 36,
          "carbs_pct": 95,
          "fats_pct": 65
        },
        "benefits": [
          "Celebration food joy",
          "Chickpea protein",
          "Iron-rich",
          "Festival energy"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High BP"
        ]
      },
      {
        "name": "Rabri Falooda",
        "description": "Thick sweetened milk with falooda, basil seeds and ice cream.",
        "emoji": "🍧",
        "tags": [
          "Festive",
          "Rich",
          "Special Drink"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 450,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 72,
          "fats": 16,
          "protein_pct": 18,
          "carbs_pct": 95,
          "fats_pct": 48
        },
        "benefits": [
          "Visual excitement",
          "Serotonin from sweetness",
          "Rose water calming joy",
          "Festive celebration"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Mutton Korma",
        "description": "Slow-cooked mutton in aromatic yogurt-cashew gravy.",
        "emoji": "🍖",
        "tags": [
          "Royal",
          "Celebratory",
          "Rich"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 520,
        "prep_time": "60 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Dinner",
        "mood_score": 5,
        "nutrition": {
          "protein": 36,
          "carbs": 18,
          "fats": 32,
          "protein_pct": 88,
          "carbs_pct": 35,
          "fats_pct": 95
        },
        "benefits": [
          "Celebration protein",
          "Cashew mood-boosting",
          "Aromatic spices excitement",
          "Rich royal dining"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol",
          "Nut allergy"
        ]
      },
      {
        "name": "Kaju Katli",
        "description": "Pure cashew diamond-shaped sweets - celebration mithai.",
        "emoji": "💎",
        "tags": [
          "Premium",
          "Gift",
          "Celebration Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 300,
        "prep_time": "20 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 42,
          "fats": 14,
          "protein_pct": 20,
          "carbs_pct": 82,
          "fats_pct": 42
        },
        "benefits": [
          "Cashew tryptophan for serotonin",
          "Premium celebration sweet",
          "Silver leaf excitement",
          "Gifting creates joy"
        ],
        "avoid_if": [
          "Nut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Dahi Bhalle Celebration",
        "description": "Soft vada in sweetened yogurt with all chutneys.",
        "emoji": "🫙",
        "tags": [
          "Festival Food",
          "Sweet-Tangy",
          "Special"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 350,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Party Snack",
        "mood_score": 4,
        "nutrition": {
          "protein": 12,
          "carbs": 55,
          "fats": 10,
          "protein_pct": 28,
          "carbs_pct": 85,
          "fats_pct": 30
        },
        "benefits": [
          "Dal protein",
          "Probiotics from yogurt",
          "Festival celebration food",
          "Multiple flavors excitement"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Malai Kofta",
        "description": "Creamy cottage cheese balls in rich cream tomato gravy.",
        "emoji": "🧀",
        "tags": [
          "Restaurant-style",
          "Rich",
          "Celebration"
        ],
        "is_veg": True,
        "diet_type": [
          "High Protein"
        ],
        "calories": 480,
        "prep_time": "45 mins",
        "difficulty": "Hard",
        "best_time": "Celebration Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 16,
          "carbs": 36,
          "fats": 32,
          "protein_pct": 36,
          "carbs_pct": 65,
          "fats_pct": 92
        },
        "benefits": [
          "Celebration-worthy dish",
          "Paneer protein",
          "Rich cream comfort",
          "Restaurant joy at home"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Chicken 65",
        "description": "Crispy spiced deep-fried chicken - party favorite.",
        "emoji": "🍗",
        "tags": [
          "Crispy",
          "Spicy",
          "Party Food"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 380,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Party Starter",
        "mood_score": 5,
        "nutrition": {
          "protein": 32,
          "carbs": 18,
          "fats": 18,
          "protein_pct": 82,
          "carbs_pct": 38,
          "fats_pct": 55
        },
        "benefits": [
          "Party excitement food",
          "High protein",
          "Capsaicin endorphin release",
          "Crispy satisfaction"
        ],
        "avoid_if": [
          "Vegetarians",
          "High cholesterol"
        ]
      },
      {
        "name": "Kulfi Falooda",
        "description": "Traditional kulfi with rose falooda and basil seeds.",
        "emoji": "🍦",
        "tags": [
          "Traditional",
          "Festive",
          "Cooling Dessert"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 380,
        "prep_time": "10 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 5,
        "nutrition": {
          "protein": 7,
          "carbs": 58,
          "fats": 14,
          "protein_pct": 16,
          "carbs_pct": 88,
          "fats_pct": 42
        },
        "benefits": [
          "Saffron kulfi mood-enhancing",
          "Rose water calming joy",
          "Festival dessert nostalgia",
          "Visual excitement"
        ],
        "avoid_if": [
          "Lactose intolerant",
          "Diabetic"
        ]
      },
      {
        "name": "Tandoori Mixed Platter",
        "description": "Mixed tandoori - chicken, paneer, seekh, boti.",
        "emoji": "🍢",
        "tags": [
          "Party Platter",
          "Mixed",
          "Smoky"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein"
        ],
        "calories": 500,
        "prep_time": "3 hours",
        "difficulty": "Hard",
        "best_time": "Party",
        "mood_score": 5,
        "nutrition": {
          "protein": 42,
          "carbs": 16,
          "fats": 28,
          "protein_pct": 95,
          "carbs_pct": 32,
          "fats_pct": 85
        },
        "benefits": [
          "Variety excites taste buds",
          "High protein celebration",
          "Smoky aroma creates atmosphere",
          "Social sharing food"
        ],
        "avoid_if": [
          "Vegetarians only",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Sevaiyan Kheer",
        "description": "Vermicelli milk pudding with dry fruits - Eid celebration.",
        "emoji": "🍮",
        "tags": [
          "Eid Special",
          "Festival",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 380,
        "prep_time": "20 mins",
        "difficulty": "Easy",
        "best_time": "Festival",
        "mood_score": 5,
        "nutrition": {
          "protein": 8,
          "carbs": 62,
          "fats": 12,
          "protein_pct": 18,
          "carbs_pct": 90,
          "fats_pct": 35
        },
        "benefits": [
          "Eid celebration nostalgia",
          "Dry fruits nutrients",
          "Serotonin from sweetness",
          "Community sharing food"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Gujiya Holi Sweet",
        "description": "Crescent-shaped fried sweet dumplings - Holi tradition.",
        "emoji": "🥟",
        "tags": [
          "Holi",
          "Festival",
          "Sweet"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 320,
        "prep_time": "45 mins",
        "difficulty": "Hard",
        "best_time": "Holi",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 52,
          "fats": 14,
          "protein_pct": 12,
          "carbs_pct": 85,
          "fats_pct": 42
        },
        "benefits": [
          "Holi excitement tradition",
          "Khoya nutrition",
          "Making together is joyful",
          "Festival celebration"
        ],
        "avoid_if": [
          "Diabetic",
          "Gluten intolerant",
          "High cholesterol"
        ]
      },
      {
        "name": "Motichoor Ladoo",
        "description": "Tiny boondi ladoos in bright orange - celebration must-have.",
        "emoji": "🟠",
        "tags": [
          "Auspicious",
          "Celebration",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 250,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Celebration",
        "mood_score": 5,
        "nutrition": {
          "protein": 5,
          "carbs": 40,
          "fats": 10,
          "protein_pct": 12,
          "carbs_pct": 82,
          "fats_pct": 30
        },
        "benefits": [
          "Auspicious celebration sweet",
          "Besan protein",
          "Excitement of orange color",
          "Gifting brings joy"
        ],
        "avoid_if": [
          "Diabetic",
          "Chickpea allergy"
        ]
      },
      {
        "name": "Paan Ice Cream",
        "description": "Betel leaf flavored ice cream - uniquely Indian excitement.",
        "emoji": "🍦",
        "tags": [
          "Unique",
          "Indian Fusion",
          "Special"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 280,
        "prep_time": "5 mins",
        "difficulty": "Easy",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 4,
          "carbs": 42,
          "fats": 12,
          "protein_pct": 10,
          "carbs_pct": 82,
          "fats_pct": 36
        },
        "benefits": [
          "Unique flavor excitement",
          "Paan digestive properties",
          "Rose water calming",
          "Conversation starter"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant"
        ]
      },
      {
        "name": "Pista Barfi",
        "description": "Pistachio milk fudge with cardamom and silver leaf.",
        "emoji": "🟢",
        "tags": [
          "Premium",
          "Green Color",
          "Celebration"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 280,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 6,
          "carbs": 38,
          "fats": 14,
          "protein_pct": 16,
          "carbs_pct": 78,
          "fats_pct": 42
        },
        "benefits": [
          "Pistachio B6 for serotonin",
          "Beautiful green color excitement",
          "Calcium from milk",
          "Premium celebration gift"
        ],
        "avoid_if": [
          "Nut allergy",
          "Diabetic"
        ]
      },
      {
        "name": "Fish Fry Coastal",
        "description": "Crispy spiced fish fry with coconut chutney.",
        "emoji": "🐟",
        "tags": [
          "Crispy",
          "Celebration",
          "Coastal"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 300,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Lunch",
        "mood_score": 4,
        "nutrition": {
          "protein": 28,
          "carbs": 10,
          "fats": 14,
          "protein_pct": 78,
          "carbs_pct": 22,
          "fats_pct": 42
        },
        "benefits": [
          "Omega-3 mood enhancement",
          "High protein celebration",
          "Crispy excitement",
          "Coastal tradition pride"
        ],
        "avoid_if": [
          "Fish allergy",
          "Vegetarians"
        ]
      },
      {
        "name": "Shahi Tukda",
        "description": "Fried bread soaked in saffron cream milk - Mughal dessert.",
        "emoji": "🍞",
        "tags": [
          "Royal",
          "Mughal",
          "Rich Dessert"
        ],
        "is_veg": True,
        "diet_type": [],
        "calories": 420,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Dessert",
        "mood_score": 4,
        "nutrition": {
          "protein": 8,
          "carbs": 62,
          "fats": 18,
          "protein_pct": 18,
          "carbs_pct": 90,
          "fats_pct": 52
        },
        "benefits": [
          "Saffron mood-enhancing",
          "Royal celebration feeling",
          "Rabri excitement",
          "Mughal tradition pride"
        ],
        "avoid_if": [
          "Diabetic",
          "Lactose intolerant",
          "Gluten intolerant"
        ]
      },
      {
        "name": "Dum Aloo Restaurant",
        "description": "Baby potatoes slow-cooked in rich spiced gravy.",
        "emoji": "🥔",
        "tags": [
          "Rich",
          "Festive",
          "Celebration"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 380,
        "prep_time": "35 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 7,
          "carbs": 52,
          "fats": 16,
          "protein_pct": 16,
          "carbs_pct": 82,
          "fats_pct": 48
        },
        "benefits": [
          "Festive vegetarian celebration",
          "Spices boost mood",
          "Potato comfort energy",
          "Restaurant experience at home"
        ],
        "avoid_if": [
          "High BP"
        ]
      },
      {
        "name": "Jhinga Masala Special",
        "description": "Spicy coastal prawn curry - festive seafood celebration.",
        "emoji": "🍤",
        "tags": [
          "Seafood",
          "Special",
          "Coastal"
        ],
        "is_veg": False,
        "diet_type": [
          "High Protein",
          "Low Carb"
        ],
        "calories": 340,
        "prep_time": "25 mins",
        "difficulty": "Medium",
        "best_time": "Celebration Dinner",
        "mood_score": 4,
        "nutrition": {
          "protein": 28,
          "carbs": 10,
          "fats": 18,
          "protein_pct": 75,
          "carbs_pct": 22,
          "fats_pct": 55
        },
        "benefits": [
          "Zinc boosts mood",
          "Omega-3 heart health",
          "Festive celebration food",
          "Coastal celebration tradition"
        ],
        "avoid_if": [
          "Shellfish allergy",
          "High cholesterol"
        ]
      },
      {
        "name": "Namkeen Mathri",
        "description": "Crispy flaky salted biscuits - festival snack tradition.",
        "emoji": "🟡",
        "tags": [
          "Festival Snack",
          "Crispy",
          "Traditional"
        ],
        "is_veg": True,
        "diet_type": [
          "Vegan"
        ],
        "calories": 260,
        "prep_time": "30 mins",
        "difficulty": "Medium",
        "best_time": "Festival",
        "mood_score": 4,
        "nutrition": {
          "protein": 5,
          "carbs": 38,
          "fats": 12,
          "protein_pct": 14,
          "carbs_pct": 80,
          "fats_pct": 36
        },
        "benefits": [
          "Festival celebration snack",
          "Crispy satisfaction",
          "Making together is fun",
          "Traditional gifting food"
        ],
        "avoid_if": [
          "Gluten intolerant",
          "High cholesterol"
        ]
      }
    ]
  }
}

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Feel Good Foodie API running!"})

@app.route("/api/moods", methods=["GET"])
def get_moods():
    moods = [{"id": k, "emoji": v["emoji"], "label": k.capitalize(), "color": v["color"]} for k, v in MOOD_FOODS.items()]
    return jsonify({"moods": moods})

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "").lower()
    if mood not in MOOD_FOODS:
        return jsonify({"error": "Mood not found"}), 404
    d = MOOD_FOODS[mood]
    return jsonify({"mood": mood, "emoji": d["emoji"], "color": d["color"], "tagline": d["tagline"], "recommendations": d["foods"]})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
