from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mood-based food recommendations data
MOOD_FOODS = {
    "happy": {
        "emoji": "😄",
        "color": "#FFD700",
        "tagline": "Celebrate your joy with vibrant flavors!",
        "foods": [
            {
                "name": "Rainbow Fruit Bowl",
                "description": "A burst of colorful tropical fruits — mango, papaya, kiwi, and berries drizzled with honey.",
                "emoji": "🍓",
                "tags": ["Fresh", "Sweet", "Colorful"],
                "calories": 210,
                "prep_time": "5 mins"
            },
            {
                "name": "Margherita Pizza",
                "description": "Classic Neapolitan pizza with fresh basil, mozzarella, and sun-ripened tomato sauce.",
                "emoji": "🍕",
                "tags": ["Cheesy", "Classic", "Satisfying"],
                "calories": 480,
                "prep_time": "20 mins"
            },
            {
                "name": "Mango Lassi",
                "description": "Creamy blended yogurt drink with sweet Alphonso mangoes and a hint of cardamom.",
                "emoji": "🥭",
                "tags": ["Refreshing", "Creamy", "Tropical"],
                "calories": 180,
                "prep_time": "5 mins"
            },
            {
                "name": "Pani Puri",
                "description": "Crispy hollow puris filled with spiced tamarind water, chickpeas, and chutneys — pure street food bliss.",
                "emoji": "🫙",
                "tags": ["Tangy", "Crunchy", "Fun"],
                "calories": 150,
                "prep_time": "15 mins"
            }
        ]
    },
    "sad": {
        "emoji": "😢",
        "color": "#6B9BD2",
        "tagline": "Warm comfort food to wrap your soul in a hug.",
        "foods": [
            {
                "name": "Masala Khichdi",
                "description": "Soothing rice and lentil porridge with ghee, cumin, and warming spices. The ultimate comfort bowl.",
                "emoji": "🍲",
                "tags": ["Warm", "Comfort", "Hearty"],
                "calories": 320,
                "prep_time": "25 mins"
            },
            {
                "name": "Chocolate Lava Cake",
                "description": "Decadent dark chocolate cake with a gooey molten center — because you deserve something magical.",
                "emoji": "🍫",
                "tags": ["Sweet", "Indulgent", "Warm"],
                "calories": 420,
                "prep_time": "15 mins"
            },
            {
                "name": "Tomato Basil Soup",
                "description": "Velvety roasted tomato soup with fresh basil, cream, and crusty garlic bread on the side.",
                "emoji": "🍅",
                "tags": ["Cozy", "Velvety", "Warm"],
                "calories": 260,
                "prep_time": "30 mins"
            },
            {
                "name": "Mac and Cheese",
                "description": "Creamy three-cheese macaroni baked golden on top — nostalgic and deeply comforting.",
                "emoji": "🧀",
                "tags": ["Creamy", "Cheesy", "Nostalgic"],
                "calories": 540,
                "prep_time": "30 mins"
            }
        ]
    },
    "stressed": {
        "emoji": "😤",
        "color": "#FF6B6B",
        "tagline": "Let these calming foods melt your tension away.",
        "foods": [
            {
                "name": "Chamomile Honey Oatmeal",
                "description": "Slow-cooked oats with chamomile-infused milk, honey, and sliced almonds — gentle and grounding.",
                "emoji": "🌾",
                "tags": ["Calming", "Gentle", "Nourishing"],
                "calories": 290,
                "prep_time": "10 mins"
            },
            {
                "name": "Avocado Toast with Egg",
                "description": "Creamy avocado on sourdough with a perfectly poached egg, chili flakes, and microgreens.",
                "emoji": "🥑",
                "tags": ["Balanced", "Protein-rich", "Grounding"],
                "calories": 380,
                "prep_time": "10 mins"
            },
            {
                "name": "Dark Chocolate & Nuts",
                "description": "85% dark chocolate with roasted walnuts and almonds — proven stress-busters in every bite.",
                "emoji": "🍫",
                "tags": ["Antioxidant", "Crunchy", "Rich"],
                "calories": 220,
                "prep_time": "2 mins"
            },
            {
                "name": "Herbal Green Tea & Dates",
                "description": "Warm jasmine green tea paired with Medjool dates and cashews to steady your energy.",
                "emoji": "🍵",
                "tags": ["Calming", "Natural", "Light"],
                "calories": 120,
                "prep_time": "3 mins"
            }
        ]
    },
    "energetic": {
        "emoji": "⚡",
        "color": "#FF9F1C",
        "tagline": "Power foods to match your unstoppable energy!",
        "foods": [
            {
                "name": "Acai Power Bowl",
                "description": "Thick acai blend topped with granola, banana, chia seeds, coconut flakes, and almond butter.",
                "emoji": "🫐",
                "tags": ["Energizing", "Superfood", "Bold"],
                "calories": 450,
                "prep_time": "10 mins"
            },
            {
                "name": "Grilled Chicken Wrap",
                "description": "Spiced grilled chicken with quinoa, roasted veggies, and hummus in a whole wheat wrap.",
                "emoji": "🌯",
                "tags": ["Protein", "Filling", "Power"],
                "calories": 520,
                "prep_time": "20 mins"
            },
            {
                "name": "Banana Peanut Butter Smoothie",
                "description": "Frozen banana, natural peanut butter, oats, and almond milk blended into a fuel-packed shake.",
                "emoji": "🍌",
                "tags": ["Protein", "Creamy", "Quick"],
                "calories": 350,
                "prep_time": "5 mins"
            },
            {
                "name": "Egg & Veggie Scramble",
                "description": "Protein-packed scrambled eggs with spinach, bell peppers, onions, and feta on whole grain toast.",
                "emoji": "🍳",
                "tags": ["Protein", "Fresh", "Fast"],
                "calories": 410,
                "prep_time": "15 mins"
            }
        ]
    },
    "romantic": {
        "emoji": "❤️",
        "color": "#FF6B9D",
        "tagline": "Indulge in flavors crafted for love and togetherness.",
        "foods": [
            {
                "name": "Strawberry Tiramisu",
                "description": "Classic Italian tiramisu layered with fresh strawberries, mascarpone, and rose-flavored cream.",
                "emoji": "🍓",
                "tags": ["Indulgent", "Elegant", "Sweet"],
                "calories": 390,
                "prep_time": "20 mins"
            },
            {
                "name": "Butter Garlic Prawns",
                "description": "Juicy tiger prawns tossed in herb butter, white wine, garlic, and lemon — date night perfection.",
                "emoji": "🍤",
                "tags": ["Luxurious", "Savory", "Elegant"],
                "calories": 340,
                "prep_time": "15 mins"
            },
            {
                "name": "Red Velvet Pancakes",
                "description": "Fluffy crimson pancakes with cream cheese glaze, fresh raspberries, and powdered sugar.",
                "emoji": "🥞",
                "tags": ["Dreamy", "Sweet", "Showstopper"],
                "calories": 460,
                "prep_time": "20 mins"
            },
            {
                "name": "Caprese Salad with Balsamic",
                "description": "Heirloom tomatoes, fresh buffalo mozzarella, fragrant basil with aged balsamic reduction.",
                "emoji": "🥗",
                "tags": ["Fresh", "Elegant", "Italian"],
                "calories": 280,
                "prep_time": "10 mins"
            }
        ]
    },
    "tired": {
        "emoji": "😴",
        "color": "#9B8EC4",
        "tagline": "Easy, nourishing bites to restore your energy gently.",
        "foods": [
            {
                "name": "Banana & Honey Toast",
                "description": "Whole grain toast topped with sliced banana, raw honey, and a sprinkle of cinnamon — simple and restorative.",
                "emoji": "🍌",
                "tags": ["Quick", "Natural Energy", "Simple"],
                "calories": 240,
                "prep_time": "3 mins"
            },
            {
                "name": "Warm Turmeric Milk",
                "description": "Golden milk with turmeric, ginger, black pepper, and coconut oil to soothe inflammation and fatigue.",
                "emoji": "🥛",
                "tags": ["Healing", "Warm", "Anti-inflammatory"],
                "calories": 130,
                "prep_time": "5 mins"
            },
            {
                "name": "Spinach & Lentil Dal",
                "description": "Iron-rich red lentil dal with wilted spinach, tempered with mustard seeds and curry leaves.",
                "emoji": "🥬",
                "tags": ["Iron-rich", "Restorative", "Warm"],
                "calories": 310,
                "prep_time": "25 mins"
            },
            {
                "name": "Mixed Nuts & Dried Fruit",
                "description": "A handful of walnuts, cashews, raisins, and dried apricots — nature's instant energy boost.",
                "emoji": "🥜",
                "tags": ["Quick", "Energizing", "No-cook"],
                "calories": 200,
                "prep_time": "1 min"
            }
        ]
    }
}


@app.route('/api/moods', methods=['GET'])
def get_moods():
    moods = [
        {"id": key, "emoji": val["emoji"], "label": key.capitalize(), "color": val["color"]}
        for key, val in MOOD_FOODS.items()
    ]
    return jsonify({"moods": moods})


@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get('mood', '').lower()

    if mood not in MOOD_FOODS:
        return jsonify({"error": "Mood not found"}), 404

    mood_data = MOOD_FOODS[mood]
    return jsonify({
        "mood": mood,
        "emoji": mood_data["emoji"],
        "color": mood_data["color"],
        "tagline": mood_data["tagline"],
        "recommendations": mood_data["foods"]
    })


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Feel Good Foodie API is running!"})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))    
    app.run(debug=False, host='0.0.0.0', port=port)