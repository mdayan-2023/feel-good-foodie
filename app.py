from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
                "prep_time": "5 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Snack",
                "mood_score": 5,
                "benefits": [
                    "Rich in Vitamin C — boosts immunity",
                    "Natural sugars give instant energy",
                    "Antioxidants improve skin health",
                    "High fiber aids digestion"
                ],
                "avoid_if": [
                    "Diabetic patients — high natural sugar",
                    "Fructose intolerant individuals"
                ]
            },
            {
                "name": "Margherita Pizza",
                "description": "Classic Neapolitan pizza with fresh basil, mozzarella, and sun-ripened tomato sauce.",
                "emoji": "🍕",
                "tags": ["Cheesy", "Classic", "Satisfying"],
                "calories": 480,
                "prep_time": "20 mins",
                "difficulty": "Medium",
                "best_time": "Lunch / Dinner",
                "mood_score": 5,
                "benefits": [
                    "Calcium from mozzarella strengthens bones",
                    "Lycopene in tomatoes is heart-healthy",
                    "Carbs provide sustained energy",
                    "Basil has anti-inflammatory properties"
                ],
                "avoid_if": [
                    "Lactose intolerant — contains cheese",
                    "Gluten intolerant — contains wheat",
                    "People on low-carb diet"
                ]
            },
            {
                "name": "Mango Lassi",
                "description": "Creamy blended yogurt drink with sweet Alphonso mangoes and a hint of cardamom.",
                "emoji": "🥭",
                "tags": ["Refreshing", "Creamy", "Tropical"],
                "calories": 180,
                "prep_time": "5 mins",
                "difficulty": "Easy",
                "best_time": "Anytime",
                "mood_score": 4,
                "benefits": [
                    "Probiotics in yogurt improve gut health",
                    "Mango rich in Vitamin A for eyesight",
                    "Cooling effect — great in summer",
                    "Calcium supports strong bones"
                ],
                "avoid_if": [
                    "Lactose intolerant — contains dairy",
                    "Diabetic patients — high sugar content",
                    "People with cold/cough"
                ]
            },
            {
                "name": "Pani Puri",
                "description": "Crispy hollow puris filled with spiced tamarind water, chickpeas, and chutneys.",
                "emoji": "🫙",
                "tags": ["Tangy", "Crunchy", "Fun"],
                "calories": 150,
                "prep_time": "15 mins",
                "difficulty": "Medium",
                "best_time": "Snack / Evening",
                "mood_score": 5,
                "benefits": [
                    "Chickpeas provide plant-based protein",
                    "Tamarind aids digestion",
                    "Mint water is cooling and refreshing",
                    "Low calorie snack option"
                ],
                "avoid_if": [
                    "People with acidity / acid reflux",
                    "Those with stomach infections",
                    "People avoiding spicy food"
                ]
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
                "description": "Soothing rice and lentil porridge with ghee, cumin, and warming spices.",
                "emoji": "🍲",
                "tags": ["Warm", "Comfort", "Hearty"],
                "calories": 320,
                "prep_time": "25 mins",
                "difficulty": "Easy",
                "best_time": "Lunch / Dinner",
                "mood_score": 5,
                "benefits": [
                    "Complete protein from rice + lentils combination",
                    "Easy to digest — gentle on stomach",
                    "Ghee contains healthy fats for brain health",
                    "Turmeric has powerful anti-inflammatory effects"
                ],
                "avoid_if": [
                    "People with severe gluten issues (check spices)",
                    "Those on very low carb diets"
                ]
            },
            {
                "name": "Chocolate Lava Cake",
                "description": "Decadent dark chocolate cake with a gooey molten center.",
                "emoji": "🍫",
                "tags": ["Sweet", "Indulgent", "Warm"],
                "calories": 420,
                "prep_time": "15 mins",
                "difficulty": "Medium",
                "best_time": "Dessert / Evening",
                "mood_score": 5,
                "benefits": [
                    "Dark chocolate triggers serotonin release — mood booster",
                    "Magnesium in chocolate reduces stress",
                    "Antioxidants in cocoa protect heart",
                    "Endorphin boost from sweetness"
                ],
                "avoid_if": [
                    "Diabetic patients — high sugar",
                    "People with chocolate/caffeine sensitivity",
                    "Those with egg allergy"
                ]
            },
            {
                "name": "Tomato Basil Soup",
                "description": "Velvety roasted tomato soup with fresh basil, cream, and crusty garlic bread.",
                "emoji": "🍅",
                "tags": ["Cozy", "Velvety", "Warm"],
                "calories": 260,
                "prep_time": "30 mins",
                "difficulty": "Easy",
                "best_time": "Lunch / Dinner",
                "mood_score": 4,
                "benefits": [
                    "Lycopene in tomatoes reduces cancer risk",
                    "Vitamin C boosts immunity",
                    "Warm soup soothes throat and sinuses",
                    "Low calorie yet filling"
                ],
                "avoid_if": [
                    "People with acid reflux — tomatoes are acidic",
                    "Lactose intolerant — contains cream",
                    "Those avoiding nightshades"
                ]
            },
            {
                "name": "Mac and Cheese",
                "description": "Creamy three-cheese macaroni baked golden on top.",
                "emoji": "🧀",
                "tags": ["Creamy", "Cheesy", "Nostalgic"],
                "calories": 540,
                "prep_time": "30 mins",
                "difficulty": "Easy",
                "best_time": "Lunch / Dinner",
                "mood_score": 5,
                "benefits": [
                    "High calcium content for bone strength",
                    "Carbs boost serotonin levels",
                    "Protein from cheese for muscle repair",
                    "Comfort food reduces emotional stress"
                ],
                "avoid_if": [
                    "Lactose intolerant — heavy dairy content",
                    "Gluten intolerant — contains pasta",
                    "People on calorie-restricted diets"
                ]
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
                "description": "Slow-cooked oats with chamomile-infused milk, honey, and sliced almonds.",
                "emoji": "🌾",
                "tags": ["Calming", "Gentle", "Nourishing"],
                "calories": 290,
                "prep_time": "10 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Evening",
                "mood_score": 5,
                "benefits": [
                    "Chamomile reduces anxiety and promotes sleep",
                    "Oats contain tryptophan — natural stress reliever",
                    "Magnesium in almonds calms nervous system",
                    "Slow-release carbs stabilize blood sugar"
                ],
                "avoid_if": [
                    "People with oat/gluten sensitivity",
                    "Those allergic to chamomile (ragweed family)"
                ]
            },
            {
                "name": "Avocado Toast with Egg",
                "description": "Creamy avocado on sourdough with a perfectly poached egg, chili flakes, and microgreens.",
                "emoji": "🥑",
                "tags": ["Balanced", "Protein-rich", "Grounding"],
                "calories": 380,
                "prep_time": "10 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Brunch",
                "mood_score": 4,
                "benefits": [
                    "Omega-3 in avocado reduces cortisol (stress hormone)",
                    "Eggs provide choline for brain health",
                    "B vitamins support nervous system function",
                    "Healthy fats keep you full and focused"
                ],
                "avoid_if": [
                    "Egg allergy sufferers",
                    "Gluten intolerant — contains bread",
                    "People on low-fat diets"
                ]
            },
            {
                "name": "Dark Chocolate & Nuts",
                "description": "85% dark chocolate with roasted walnuts and almonds — proven stress-busters.",
                "emoji": "🍫",
                "tags": ["Antioxidant", "Crunchy", "Rich"],
                "calories": 220,
                "prep_time": "2 mins",
                "difficulty": "Easy",
                "best_time": "Snack / Anytime",
                "mood_score": 5,
                "benefits": [
                    "Magnesium in dark chocolate lowers stress hormones",
                    "Walnuts contain Omega-3 for brain function",
                    "Endorphin release from chocolate improves mood",
                    "Selenium in nuts protects against oxidative stress"
                ],
                "avoid_if": [
                    "Nut allergy sufferers",
                    "Migraine patients — chocolate can be a trigger",
                    "Diabetic patients — monitor portion size"
                ]
            },
            {
                "name": "Herbal Green Tea & Dates",
                "description": "Warm jasmine green tea paired with Medjool dates and cashews.",
                "emoji": "🍵",
                "tags": ["Calming", "Natural", "Light"],
                "calories": 120,
                "prep_time": "3 mins",
                "difficulty": "Easy",
                "best_time": "Evening / Anytime",
                "mood_score": 4,
                "benefits": [
                    "L-theanine in green tea promotes calm alertness",
                    "Dates provide natural energy without sugar crash",
                    "Antioxidants in green tea reduce inflammation",
                    "Cashews contain zinc which regulates mood"
                ],
                "avoid_if": [
                    "Pregnant women — limit green tea caffeine",
                    "People with caffeine sensitivity",
                    "Those with date/tree nut allergies"
                ]
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
                "prep_time": "10 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Pre-workout",
                "mood_score": 5,
                "benefits": [
                    "Acai berries — highest antioxidant food on earth",
                    "Chia seeds provide sustained energy for hours",
                    "Banana gives instant potassium boost",
                    "Almond butter provides healthy protein and fats"
                ],
                "avoid_if": [
                    "People with tree nut allergies",
                    "Those with irritable bowel — chia seeds can cause bloating",
                    "Diabetic patients — high natural sugar"
                ]
            },
            {
                "name": "Grilled Chicken Wrap",
                "description": "Spiced grilled chicken with quinoa, roasted veggies, and hummus in a whole wheat wrap.",
                "emoji": "🌯",
                "tags": ["Protein", "Filling", "Power"],
                "calories": 520,
                "prep_time": "20 mins",
                "difficulty": "Medium",
                "best_time": "Lunch / Post-workout",
                "mood_score": 4,
                "benefits": [
                    "High protein supports muscle growth and repair",
                    "Quinoa is a complete protein with all amino acids",
                    "Complex carbs provide long-lasting energy",
                    "Iron from chicken prevents fatigue"
                ],
                "avoid_if": [
                    "Vegetarians / Vegans",
                    "Gluten intolerant — contains wheat wrap",
                    "People with sesame allergy — hummus contains tahini"
                ]
            },
            {
                "name": "Banana Peanut Butter Smoothie",
                "description": "Frozen banana, natural peanut butter, oats, and almond milk blended into a fuel-packed shake.",
                "emoji": "🍌",
                "tags": ["Protein", "Creamy", "Quick"],
                "calories": 350,
                "prep_time": "5 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Pre-workout",
                "mood_score": 5,
                "benefits": [
                    "Bananas provide quick energy via natural sugars",
                    "Peanut butter — healthy fats and protein combo",
                    "Oats give sustained slow-release energy",
                    "Potassium prevents muscle cramps during exercise"
                ],
                "avoid_if": [
                    "Peanut allergy sufferers — serious risk",
                    "Nut allergy — contains almond milk",
                    "People on very low calorie diets"
                ]
            },
            {
                "name": "Egg & Veggie Scramble",
                "description": "Protein-packed scrambled eggs with spinach, bell peppers, onions, and feta on whole grain toast.",
                "emoji": "🍳",
                "tags": ["Protein", "Fresh", "Fast"],
                "calories": 410,
                "prep_time": "15 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Brunch",
                "mood_score": 4,
                "benefits": [
                    "Eggs — complete protein with all essential amino acids",
                    "Spinach rich in iron fights fatigue",
                    "Bell peppers highest in Vitamin C",
                    "B12 in eggs boosts energy metabolism"
                ],
                "avoid_if": [
                    "Egg allergy sufferers",
                    "Lactose intolerant — contains feta",
                    "Vegans"
                ]
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
                "prep_time": "20 mins",
                "difficulty": "Medium",
                "best_time": "Dessert / Evening",
                "mood_score": 5,
                "benefits": [
                    "Strawberries rich in Vitamin C — natural aphrodisiac",
                    "Dark chocolate in tiramisu boosts dopamine",
                    "Mood-lifting effect from sweet indulgence",
                    "Calcium from mascarpone supports bone health"
                ],
                "avoid_if": [
                    "Lactose intolerant — heavy dairy",
                    "Egg allergy — contains raw eggs",
                    "Diabetic patients — high sugar content"
                ]
            },
            {
                "name": "Butter Garlic Prawns",
                "description": "Juicy tiger prawns tossed in herb butter, white wine, garlic, and lemon.",
                "emoji": "🍤",
                "tags": ["Luxurious", "Savory", "Elegant"],
                "calories": 340,
                "prep_time": "15 mins",
                "difficulty": "Medium",
                "best_time": "Dinner",
                "mood_score": 5,
                "benefits": [
                    "Prawns high in zinc — boosts libido naturally",
                    "Omega-3 fatty acids support heart health",
                    "Garlic improves blood circulation",
                    "Low calorie yet high protein — guilt-free luxury"
                ],
                "avoid_if": [
                    "Shellfish allergy — can be life-threatening",
                    "People with high cholesterol — monitor intake",
                    "Pregnant women — avoid undercooked prawns"
                ]
            },
            {
                "name": "Red Velvet Pancakes",
                "description": "Fluffy crimson pancakes with cream cheese glaze, fresh raspberries, and powdered sugar.",
                "emoji": "🥞",
                "tags": ["Dreamy", "Sweet", "Showstopper"],
                "calories": 460,
                "prep_time": "20 mins",
                "difficulty": "Medium",
                "best_time": "Breakfast / Brunch",
                "mood_score": 4,
                "benefits": [
                    "Cocoa in red velvet contains mood-boosting flavonoids",
                    "Raspberries rich in Vitamin C and antioxidants",
                    "Carbs trigger serotonin — happiness hormone",
                    "Cream cheese provides calcium and protein"
                ],
                "avoid_if": [
                    "Gluten intolerant — contains flour",
                    "Lactose intolerant — contains dairy",
                    "Egg allergy sufferers"
                ]
            },
            {
                "name": "Caprese Salad with Balsamic",
                "description": "Heirloom tomatoes, fresh buffalo mozzarella, fragrant basil with aged balsamic reduction.",
                "emoji": "🥗",
                "tags": ["Fresh", "Elegant", "Italian"],
                "calories": 280,
                "prep_time": "10 mins",
                "difficulty": "Easy",
                "best_time": "Starter / Lunch",
                "mood_score": 4,
                "benefits": [
                    "Lycopene in tomatoes protects heart health",
                    "Fresh basil has anti-anxiety properties",
                    "Mozzarella provides calcium and protein",
                    "Light and refreshing — won't cause food coma"
                ],
                "avoid_if": [
                    "Lactose intolerant — contains mozzarella",
                    "People with acid reflux — tomatoes and balsamic are acidic",
                    "Those avoiding nightshades"
                ]
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
                "description": "Whole grain toast topped with sliced banana, raw honey, and a sprinkle of cinnamon.",
                "emoji": "🍌",
                "tags": ["Quick", "Natural Energy", "Simple"],
                "calories": 240,
                "prep_time": "3 mins",
                "difficulty": "Easy",
                "best_time": "Breakfast / Snack",
                "mood_score": 4,
                "benefits": [
                    "Banana provides instant glucose for quick energy",
                    "Honey has natural enzymes that aid digestion",
                    "Cinnamon stabilizes blood sugar levels",
                    "Whole grain gives sustained slow-release energy"
                ],
                "avoid_if": [
                    "Gluten intolerant — contains bread",
                    "People with pollen-food syndrome — banana allergy",
                    "Diabetic patients — monitor honey intake"
                ]
            },
            {
                "name": "Warm Turmeric Milk",
                "description": "Golden milk with turmeric, ginger, black pepper, and coconut oil to soothe fatigue.",
                "emoji": "🥛",
                "tags": ["Healing", "Warm", "Anti-inflammatory"],
                "calories": 130,
                "prep_time": "5 mins",
                "difficulty": "Easy",
                "best_time": "Evening / Before bed",
                "mood_score": 5,
                "benefits": [
                    "Curcumin in turmeric is a powerful anti-inflammatory",
                    "Warm milk contains tryptophan — induces sleep",
                    "Ginger boosts circulation and reduces fatigue",
                    "Black pepper increases curcumin absorption by 2000%"
                ],
                "avoid_if": [
                    "Lactose intolerant — use plant milk instead",
                    "People on blood thinners — turmeric affects clotting",
                    "Those with gallbladder issues"
                ]
            },
            {
                "name": "Spinach & Lentil Dal",
                "description": "Iron-rich red lentil dal with wilted spinach, tempered with mustard seeds and curry leaves.",
                "emoji": "🥬",
                "tags": ["Iron-rich", "Restorative", "Warm"],
                "calories": 310,
                "prep_time": "25 mins",
                "difficulty": "Easy",
                "best_time": "Lunch / Dinner",
                "mood_score": 4,
                "benefits": [
                    "Iron in spinach + lentils fights fatigue and anemia",
                    "Plant protein for sustained energy recovery",
                    "Folate supports red blood cell production",
                    "B vitamins boost energy metabolism"
                ],
                "avoid_if": [
                    "People with kidney stones — spinach high in oxalates",
                    "Those with IBS — lentils can cause bloating",
                    "People on blood thinners — high Vitamin K in spinach"
                ]
            },
            {
                "name": "Mixed Nuts & Dried Fruit",
                "description": "A handful of walnuts, cashews, raisins, and dried apricots — nature's instant energy boost.",
                "emoji": "🥜",
                "tags": ["Quick", "Energizing", "No-cook"],
                "calories": 200,
                "prep_time": "1 min",
                "difficulty": "Easy",
                "best_time": "Snack / Anytime",
                "mood_score": 4,
                "benefits": [
                    "Walnuts contain Omega-3 for brain energy",
                    "Iron in dried apricots combats tiredness",
                    "Natural sugars in raisins give quick energy burst",
                    "Magnesium in cashews reduces muscle fatigue"
                ],
                "avoid_if": [
                    "Nut allergy sufferers",
                    "Diabetic patients — dried fruits high in sugar",
                    "People with kidney disease — high potassium"
                ]
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
