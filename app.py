from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOOD_FOODS = {
    "happy": {
        "emoji": "😄", "color": "#FFD700",
        "tagline": "Celebrate your joy with vibrant flavors!",
        "foods": [
            {"name": "Rainbow Fruit Bowl", "description": "A burst of colorful tropical fruits — mango, papaya, kiwi, and berries drizzled with honey.", "emoji": "🍓", "tags": ["Fresh", "Sweet", "Colorful"], "calories": 210, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Breakfast / Snack", "mood_score": 5, "benefits": ["Rich in Vitamin C — boosts immunity", "Natural sugars give instant energy", "Antioxidants improve skin health", "High fiber aids digestion"], "avoid_if": ["Diabetic patients — high natural sugar", "Fructose intolerant individuals"]},
            {"name": "Margherita Pizza", "description": "Classic Neapolitan pizza with fresh basil, mozzarella, and sun-ripened tomato sauce.", "emoji": "🍕", "tags": ["Cheesy", "Classic", "Satisfying"], "calories": 480, "prep_time": "20 mins", "difficulty": "Medium", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Calcium from mozzarella strengthens bones", "Lycopene in tomatoes is heart-healthy", "Carbs provide sustained energy", "Basil has anti-inflammatory properties"], "avoid_if": ["Lactose intolerant — contains cheese", "Gluten intolerant — contains wheat"]},
            {"name": "Mango Lassi", "description": "Creamy blended yogurt drink with sweet Alphonso mangoes and a hint of cardamom.", "emoji": "🥭", "tags": ["Refreshing", "Creamy", "Tropical"], "calories": 180, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Anytime", "mood_score": 4, "benefits": ["Probiotics in yogurt improve gut health", "Mango rich in Vitamin A for eyesight", "Cooling effect — great in summer", "Calcium supports strong bones"], "avoid_if": ["Lactose intolerant — contains dairy", "Diabetic patients — high sugar content"]},
            {"name": "Pani Puri", "description": "Crispy hollow puris filled with spiced tamarind water, chickpeas, and chutneys.", "emoji": "🫙", "tags": ["Tangy", "Crunchy", "Fun"], "calories": 150, "prep_time": "15 mins", "difficulty": "Medium", "best_time": "Snack / Evening", "mood_score": 5, "benefits": ["Chickpeas provide plant-based protein", "Tamarind aids digestion", "Mint water is cooling and refreshing", "Low calorie snack option"], "avoid_if": ["People with acidity / acid reflux", "People avoiding spicy food"]}
        ]
    },
    "sad": {
        "emoji": "😢", "color": "#6B9BD2",
        "tagline": "Warm comfort food to wrap your soul in a hug.",
        "foods": [
            {"name": "Masala Khichdi", "description": "Soothing rice and lentil porridge with ghee, cumin, and warming spices.", "emoji": "🍲", "tags": ["Warm", "Comfort", "Hearty"], "calories": 320, "prep_time": "25 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Complete protein from rice + lentils", "Easy to digest — gentle on stomach", "Ghee contains healthy fats for brain", "Turmeric has anti-inflammatory effects"], "avoid_if": ["People on very low carb diets"]},
            {"name": "Chocolate Lava Cake", "description": "Decadent dark chocolate cake with a gooey molten center.", "emoji": "🍫", "tags": ["Sweet", "Indulgent", "Warm"], "calories": 420, "prep_time": "15 mins", "difficulty": "Medium", "best_time": "Dessert / Evening", "mood_score": 5, "benefits": ["Dark chocolate triggers serotonin — mood booster", "Magnesium reduces stress", "Antioxidants in cocoa protect heart", "Endorphin boost from sweetness"], "avoid_if": ["Diabetic patients — high sugar", "People with chocolate/caffeine sensitivity"]},
            {"name": "Tomato Basil Soup", "description": "Velvety roasted tomato soup with fresh basil, cream, and crusty garlic bread.", "emoji": "🍅", "tags": ["Cozy", "Velvety", "Warm"], "calories": 260, "prep_time": "30 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 4, "benefits": ["Lycopene in tomatoes reduces cancer risk", "Vitamin C boosts immunity", "Warm soup soothes throat", "Low calorie yet filling"], "avoid_if": ["People with acid reflux", "Lactose intolerant — contains cream"]},
            {"name": "Mac and Cheese", "description": "Creamy three-cheese macaroni baked golden on top.", "emoji": "🧀", "tags": ["Creamy", "Cheesy", "Nostalgic"], "calories": 540, "prep_time": "30 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["High calcium for bone strength", "Carbs boost serotonin levels", "Protein from cheese for muscle repair", "Comfort food reduces emotional stress"], "avoid_if": ["Lactose intolerant — heavy dairy", "Gluten intolerant — contains pasta"]}
        ]
    },
    "stressed": {
        "emoji": "😤", "color": "#FF6B6B",
        "tagline": "Let these calming foods melt your tension away.",
        "foods": [
            {"name": "Chamomile Honey Oatmeal", "description": "Slow-cooked oats with chamomile-infused milk, honey, and sliced almonds.", "emoji": "🌾", "tags": ["Calming", "Gentle", "Nourishing"], "calories": 290, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Breakfast / Evening", "mood_score": 5, "benefits": ["Chamomile reduces anxiety", "Oats contain tryptophan — stress reliever", "Magnesium in almonds calms nervous system", "Slow-release carbs stabilize blood sugar"], "avoid_if": ["People with oat/gluten sensitivity", "Those allergic to chamomile"]},
            {"name": "Avocado Toast with Egg", "description": "Creamy avocado on sourdough with a perfectly poached egg and chili flakes.", "emoji": "🥑", "tags": ["Balanced", "Protein-rich", "Grounding"], "calories": 380, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Breakfast / Brunch", "mood_score": 4, "benefits": ["Omega-3 in avocado reduces cortisol", "Eggs provide choline for brain health", "B vitamins support nervous system", "Healthy fats keep you focused"], "avoid_if": ["Egg allergy sufferers", "Gluten intolerant — contains bread"]},
            {"name": "Dark Chocolate & Nuts", "description": "85% dark chocolate with roasted walnuts and almonds.", "emoji": "🍫", "tags": ["Antioxidant", "Crunchy", "Rich"], "calories": 220, "prep_time": "2 mins", "difficulty": "Easy", "best_time": "Snack / Anytime", "mood_score": 5, "benefits": ["Magnesium lowers stress hormones", "Walnuts contain Omega-3 for brain", "Endorphin release improves mood", "Selenium protects against oxidative stress"], "avoid_if": ["Nut allergy sufferers", "Migraine patients — chocolate can trigger"]},
            {"name": "Herbal Green Tea & Dates", "description": "Warm jasmine green tea paired with Medjool dates and cashews.", "emoji": "🍵", "tags": ["Calming", "Natural", "Light"], "calories": 120, "prep_time": "3 mins", "difficulty": "Easy", "best_time": "Evening / Anytime", "mood_score": 4, "benefits": ["L-theanine promotes calm alertness", "Dates provide natural energy", "Antioxidants reduce inflammation", "Cashews contain zinc which regulates mood"], "avoid_if": ["Pregnant women — limit caffeine", "People with caffeine sensitivity"]}
        ]
    },
    "energetic": {
        "emoji": "⚡", "color": "#FF9F1C",
        "tagline": "Power foods to match your unstoppable energy!",
        "foods": [
            {"name": "Acai Power Bowl", "description": "Thick acai blend topped with granola, banana, chia seeds, and almond butter.", "emoji": "🫐", "tags": ["Energizing", "Superfood", "Bold"], "calories": 450, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Breakfast / Pre-workout", "mood_score": 5, "benefits": ["Acai — highest antioxidant food", "Chia seeds provide sustained energy", "Banana gives instant potassium boost", "Almond butter provides protein and fats"], "avoid_if": ["People with tree nut allergies", "Diabetic patients — high natural sugar"]},
            {"name": "Grilled Chicken Wrap", "description": "Spiced grilled chicken with quinoa, roasted veggies, and hummus in a wheat wrap.", "emoji": "🌯", "tags": ["Protein", "Filling", "Power"], "calories": 520, "prep_time": "20 mins", "difficulty": "Medium", "best_time": "Lunch / Post-workout", "mood_score": 4, "benefits": ["High protein supports muscle growth", "Quinoa is a complete protein", "Complex carbs provide lasting energy", "Iron prevents fatigue"], "avoid_if": ["Vegetarians / Vegans", "Gluten intolerant — contains wheat wrap"]},
            {"name": "Banana Peanut Butter Smoothie", "description": "Frozen banana, peanut butter, oats, and almond milk blended into a shake.", "emoji": "🍌", "tags": ["Protein", "Creamy", "Quick"], "calories": 350, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Breakfast / Pre-workout", "mood_score": 5, "benefits": ["Bananas provide quick energy", "Peanut butter — healthy fats and protein", "Oats give slow-release energy", "Potassium prevents muscle cramps"], "avoid_if": ["Peanut allergy sufferers — serious risk", "People on very low calorie diets"]},
            {"name": "Egg & Veggie Scramble", "description": "Scrambled eggs with spinach, bell peppers, onions, and feta on whole grain toast.", "emoji": "🍳", "tags": ["Protein", "Fresh", "Fast"], "calories": 410, "prep_time": "15 mins", "difficulty": "Easy", "best_time": "Breakfast / Brunch", "mood_score": 4, "benefits": ["Eggs — complete protein", "Spinach rich in iron fights fatigue", "Bell peppers highest in Vitamin C", "B12 boosts energy metabolism"], "avoid_if": ["Egg allergy sufferers", "Vegans"]}
        ]
    },
    "romantic": {
        "emoji": "❤️", "color": "#FF6B9D",
        "tagline": "Indulge in flavors crafted for love and togetherness.",
        "foods": [
            {"name": "Strawberry Tiramisu", "description": "Italian tiramisu layered with fresh strawberries and rose-flavored cream.", "emoji": "🍓", "tags": ["Indulgent", "Elegant", "Sweet"], "calories": 390, "prep_time": "20 mins", "difficulty": "Medium", "best_time": "Dessert / Evening", "mood_score": 5, "benefits": ["Strawberries — natural aphrodisiac", "Dark chocolate boosts dopamine", "Mood-lifting effect from sweetness", "Calcium from mascarpone supports bones"], "avoid_if": ["Lactose intolerant", "Egg allergy", "Diabetic patients"]},
            {"name": "Butter Garlic Prawns", "description": "Tiger prawns in herb butter, white wine, garlic, and lemon.", "emoji": "🍤", "tags": ["Luxurious", "Savory", "Elegant"], "calories": 340, "prep_time": "15 mins", "difficulty": "Medium", "best_time": "Dinner", "mood_score": 5, "benefits": ["Prawns high in zinc — boosts libido", "Omega-3 supports heart health", "Garlic improves blood circulation", "Low calorie yet high protein"], "avoid_if": ["Shellfish allergy — life-threatening", "People with high cholesterol"]},
            {"name": "Red Velvet Pancakes", "description": "Crimson pancakes with cream cheese glaze and fresh raspberries.", "emoji": "🥞", "tags": ["Dreamy", "Sweet", "Showstopper"], "calories": 460, "prep_time": "20 mins", "difficulty": "Medium", "best_time": "Breakfast / Brunch", "mood_score": 4, "benefits": ["Cocoa contains mood-boosting flavonoids", "Raspberries rich in Vitamin C", "Carbs trigger serotonin", "Cream cheese provides calcium"], "avoid_if": ["Gluten intolerant", "Lactose intolerant", "Egg allergy sufferers"]},
            {"name": "Caprese Salad with Balsamic", "description": "Heirloom tomatoes, buffalo mozzarella, basil with aged balsamic reduction.", "emoji": "🥗", "tags": ["Fresh", "Elegant", "Italian"], "calories": 280, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Starter / Lunch", "mood_score": 4, "benefits": ["Lycopene protects heart health", "Basil has anti-anxiety properties", "Mozzarella provides calcium", "Light — won't cause food coma"], "avoid_if": ["Lactose intolerant", "People with acid reflux"]}
        ]
    },
    "tired": {
        "emoji": "😴", "color": "#9B8EC4",
        "tagline": "Easy, nourishing bites to restore your energy gently.",
        "foods": [
            {"name": "Banana & Honey Toast", "description": "Whole grain toast with banana, raw honey, and cinnamon.", "emoji": "🍌", "tags": ["Quick", "Natural Energy", "Simple"], "calories": 240, "prep_time": "3 mins", "difficulty": "Easy", "best_time": "Breakfast / Snack", "mood_score": 4, "benefits": ["Banana provides instant glucose", "Honey has enzymes that aid digestion", "Cinnamon stabilizes blood sugar", "Whole grain gives sustained energy"], "avoid_if": ["Gluten intolerant — contains bread", "Diabetic patients — monitor honey"]},
            {"name": "Warm Turmeric Milk", "description": "Golden milk with turmeric, ginger, black pepper, and coconut oil.", "emoji": "🥛", "tags": ["Healing", "Warm", "Anti-inflammatory"], "calories": 130, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Evening / Before bed", "mood_score": 5, "benefits": ["Curcumin is a powerful anti-inflammatory", "Warm milk contains tryptophan — induces sleep", "Ginger reduces fatigue", "Black pepper increases curcumin absorption by 2000%"], "avoid_if": ["Lactose intolerant — use plant milk", "People on blood thinners"]},
            {"name": "Spinach & Lentil Dal", "description": "Iron-rich red lentil dal with spinach, mustard seeds, and curry leaves.", "emoji": "🥬", "tags": ["Iron-rich", "Restorative", "Warm"], "calories": 310, "prep_time": "25 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 4, "benefits": ["Iron fights fatigue and anemia", "Plant protein for energy recovery", "Folate supports red blood cells", "B vitamins boost energy metabolism"], "avoid_if": ["People with kidney stones — high oxalates", "Those with IBS — lentils cause bloating"]},
            {"name": "Mixed Nuts & Dried Fruit", "description": "Walnuts, cashews, raisins, and dried apricots — instant energy boost.", "emoji": "🥜", "tags": ["Quick", "Energizing", "No-cook"], "calories": 200, "prep_time": "1 min", "difficulty": "Easy", "best_time": "Snack / Anytime", "mood_score": 4, "benefits": ["Walnuts contain Omega-3 for brain energy", "Iron in dried apricots combats tiredness", "Natural sugars give quick energy", "Magnesium reduces muscle fatigue"], "avoid_if": ["Nut allergy sufferers", "Diabetic patients — dried fruits high in sugar"]}
        ]
    },
    "anxious": {
        "emoji": "😰", "color": "#7EC8C8",
        "tagline": "Gentle foods to quiet your mind and calm your nerves.",
        "foods": [
            {"name": "Warm Ashwagandha Milk", "description": "Warm milk blended with ashwagandha powder, honey, and nutmeg for deep calm.", "emoji": "🥛", "tags": ["Calming", "Adaptogen", "Warm"], "calories": 140, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Evening / Before bed", "mood_score": 5, "benefits": ["Ashwagandha is a proven anxiety reducer", "Reduces cortisol levels", "Warm milk promotes relaxation", "Nutmeg has natural sedative properties"], "avoid_if": ["Pregnant women — ashwagandha not safe", "People on thyroid medication", "Lactose intolerant — use oat milk"]},
            {"name": "Blueberry Yogurt Parfait", "description": "Layers of Greek yogurt, fresh blueberries, granola, and a drizzle of honey.", "emoji": "🫐", "tags": ["Soothing", "Fresh", "Light"], "calories": 280, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Breakfast / Snack", "mood_score": 4, "benefits": ["Blueberries reduce oxidative stress in brain", "Probiotics improve gut-brain connection", "Magnesium calms nervous system", "Low glycemic — no sugar crash anxiety"], "avoid_if": ["Lactose intolerant — contains yogurt", "People with granola/nut allergies"]},
            {"name": "Cucumber Mint Sandwich", "description": "Cool cucumber and cream cheese on whole grain bread with fresh mint leaves.", "emoji": "🥪", "tags": ["Cool", "Light", "Fresh"], "calories": 220, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Lunch / Snack", "mood_score": 4, "benefits": ["Cucumber has natural cooling properties", "Mint reduces nausea caused by anxiety", "Magnesium in whole grain calms nerves", "Light on stomach — no bloating"], "avoid_if": ["Gluten intolerant — contains bread", "Lactose intolerant — contains cream cheese"]},
            {"name": "Lavender Honey Oats", "description": "Overnight oats with lavender-infused milk, banana, and raw honey.", "emoji": "🌸", "tags": ["Soothing", "Floral", "Gentle"], "calories": 310, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Breakfast", "mood_score": 5, "benefits": ["Lavender proven to reduce anxiety symptoms", "Oats provide steady energy without spikes", "Banana contains serotonin precursors", "Honey stabilizes blood sugar"], "avoid_if": ["People with lavender allergy", "Gluten intolerant — contains oats"]}
        ]
    },
    "bored": {
        "emoji": "😑", "color": "#F4A261",
        "tagline": "Fun, exciting bites to spark your taste buds!",
        "foods": [
            {"name": "Loaded Nachos", "description": "Crispy tortilla chips loaded with melted cheese, jalapeños, salsa, and sour cream.", "emoji": "🧀", "tags": ["Fun", "Cheesy", "Exciting"], "calories": 520, "prep_time": "15 mins", "difficulty": "Easy", "best_time": "Snack / Evening", "mood_score": 5, "benefits": ["Capsaicin in jalapeños releases endorphins", "Social food — great for sharing", "Satisfying crunch elevates mood", "Cheese provides calcium and protein"], "avoid_if": ["Lactose intolerant — heavy cheese", "People with acid reflux — spicy"]},
            {"name": "DIY Sushi Rolls", "description": "Fun to make sushi rolls with rice, avocado, cucumber, and your choice of filling.", "emoji": "🍣", "tags": ["Interactive", "Creative", "Fresh"], "calories": 380, "prep_time": "30 mins", "difficulty": "Medium", "best_time": "Lunch / Dinner", "mood_score": 4, "benefits": ["Making food is therapeutic for boredom", "Nori seaweed rich in iodine", "Omega-3 from fish boosts brain function", "Low calorie yet filling"], "avoid_if": ["Raw fish allergy", "Pregnant women — avoid raw fish"]},
            {"name": "Spicy Masala Popcorn", "description": "Air-popped corn tossed in chaat masala, butter, and lime — the ultimate snack.", "emoji": "🍿", "tags": ["Spicy", "Crunchy", "Addictive"], "calories": 180, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Snack / Movie time", "mood_score": 5, "benefits": ["Whole grain popcorn is high in fiber", "Chaat masala aids digestion", "Low calorie snack option", "Crunching relieves tension and boredom"], "avoid_if": ["People with acid reflux — spicy", "Those with corn allergy"]},
            {"name": "Waffle with Ice Cream", "description": "Crispy Belgian waffle topped with vanilla ice cream, chocolate sauce, and sprinkles.", "emoji": "🧇", "tags": ["Indulgent", "Sweet", "Fun"], "calories": 580, "prep_time": "15 mins", "difficulty": "Easy", "best_time": "Dessert / Snack", "mood_score": 5, "benefits": ["Instant mood elevation from sweetness", "Sugar provides quick brain energy", "Fun dessert breaks monotony", "Nostalgic comfort effect"], "avoid_if": ["Diabetic patients — very high sugar", "Lactose intolerant — contains ice cream"]}
        ]
    },
    "excited": {
        "emoji": "🤩", "color": "#FF6B35",
        "tagline": "Celebratory flavors to match your electric energy!",
        "foods": [
            {"name": "Charcuterie Board", "description": "Artisan cheeses, cured meats, grapes, nuts, and honey on a wooden board.", "emoji": "🍇", "tags": ["Festive", "Elegant", "Social"], "calories": 450, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Party / Evening", "mood_score": 5, "benefits": ["Variety keeps excitement alive", "Cheese provides calcium and protein", "Nuts offer healthy fats for energy", "Grapes rich in resveratrol for heart health"], "avoid_if": ["Lactose intolerant — contains cheese", "Nut allergy sufferers"]},
            {"name": "Celebration Cake Slice", "description": "Fluffy vanilla sponge with buttercream frosting, fresh strawberries, and gold sprinkles.", "emoji": "🎂", "tags": ["Celebratory", "Sweet", "Special"], "calories": 480, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Dessert / Celebration", "mood_score": 5, "benefits": ["Sugar triggers dopamine release", "Strawberries add Vitamin C", "Celebratory eating enhances social bonding", "Mood-boosting serotonin from carbs"], "avoid_if": ["Diabetic patients — very high sugar", "Lactose intolerant"]},
            {"name": "Mango Chili Sorbet", "description": "Vibrant mango sorbet with a chili-lime kick — bold, exciting, and refreshing.", "emoji": "🍧", "tags": ["Bold", "Refreshing", "Unique"], "calories": 160, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Dessert / Anytime", "mood_score": 4, "benefits": ["Mango rich in Vitamin C and A", "Chili releases endorphins", "Low fat and refreshing", "Natural fruit sugars provide quick energy"], "avoid_if": ["People with spice sensitivity", "Diabetic patients — high fruit sugar"]},
            {"name": "Prawn Tacos", "description": "Crispy spiced prawns in corn tortillas with mango salsa, avocado, and lime crema.", "emoji": "🌮", "tags": ["Festive", "Spicy", "Fresh"], "calories": 420, "prep_time": "20 mins", "difficulty": "Medium", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Prawns high in protein and zinc", "Avocado provides healthy fats", "Mango salsa rich in antioxidants", "Corn tortillas are gluten-free"], "avoid_if": ["Shellfish allergy", "People with spice sensitivity"]}
        ]
    },
    "sick": {
        "emoji": "🤒", "color": "#90BE6D",
        "tagline": "Healing foods to nurse you back to health.",
        "foods": [
            {"name": "Ginger Lemon Honey Tea", "description": "Hot ginger tea with fresh lemon juice, raw honey, and a pinch of black pepper.", "emoji": "🍋", "tags": ["Healing", "Soothing", "Immunity"], "calories": 45, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Anytime", "mood_score": 5, "benefits": ["Ginger is a powerful anti-nausea agent", "Honey has antibacterial properties", "Vitamin C in lemon boosts immunity", "Warmth soothes sore throat instantly"], "avoid_if": ["People on blood thinners — ginger affects clotting", "Those with acid reflux — lemon is acidic"]},
            {"name": "Chicken Soup", "description": "Classic chicken broth with soft vegetables, noodles, and healing herbs.", "emoji": "🍜", "tags": ["Healing", "Warm", "Nourishing"], "calories": 180, "prep_time": "40 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Proven to reduce cold symptoms scientifically", "Steam opens blocked nasal passages", "Electrolytes prevent dehydration", "Easily digestible when appetite is low"], "avoid_if": ["Vegetarians / Vegans", "People with chicken allergy"]},
            {"name": "Moong Dal Khichdi", "description": "Simple yellow moong dal with soft rice, turmeric, and a drizzle of ghee.", "emoji": "🍚", "tags": ["Gentle", "Digestible", "Healing"], "calories": 260, "prep_time": "20 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Easiest food to digest when sick", "Turmeric has powerful healing properties", "Provides energy without taxing digestion", "Ghee lubricates intestinal lining"], "avoid_if": ["People with severe legume allergies"]},
            {"name": "Banana & Curd Rice", "description": "Soft cooked rice mixed with fresh curd, ripe banana, and a pinch of salt.", "emoji": "🍌", "tags": ["Soothing", "Probiotic", "Gentle"], "calories": 240, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 4, "benefits": ["Probiotics in curd restore gut flora", "Banana is BRAT diet approved for illness", "Easily digestible bland food", "Potassium replaces lost electrolytes"], "avoid_if": ["Lactose intolerant — contains curd", "People with banana allergy"]}
        ]
    },
    "angry": {
        "emoji": "😠", "color": "#E63946",
        "tagline": "Cool down with these calming, refreshing foods.",
        "foods": [
            {"name": "Cold Watermelon Mint Juice", "description": "Fresh watermelon blended with mint, lime, and black salt — ice cold.", "emoji": "🍉", "tags": ["Cooling", "Refreshing", "Calming"], "calories": 90, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Anytime", "mood_score": 5, "benefits": ["Watermelon is 92% water — instant cooling", "Mint has natural calming effect on nervous system", "L-citrulline reduces blood pressure", "Low calorie anger management!"], "avoid_if": ["Diabetic patients — high natural sugar", "People with watermelon allergy"]},
            {"name": "Chilled Cucumber Raita", "description": "Cold yogurt with grated cucumber, cumin, coriander, and mint.", "emoji": "🥒", "tags": ["Cooling", "Probiotic", "Calm"], "calories": 120, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 4, "benefits": ["Cucumber has natural cooling Ayurvedic properties", "Cold yogurt cools body temperature", "Probiotics improve mood via gut-brain axis", "Magnesium in cumin calms muscle tension"], "avoid_if": ["Lactose intolerant — contains yogurt", "People with cold sensitivity"]},
            {"name": "Dark Chocolate Bark", "description": "Thin dark chocolate bark with sea salt, dried cranberries, and pistachios.", "emoji": "🍫", "tags": ["Rich", "Antioxidant", "Calming"], "calories": 200, "prep_time": "3 mins", "difficulty": "Easy", "best_time": "Snack / Anytime", "mood_score": 5, "benefits": ["Magnesium reduces anger and irritability", "Serotonin boost from dark chocolate", "Sea salt balances electrolytes", "Mindful eating calms the mind"], "avoid_if": ["Nut allergy — contains pistachios", "Caffeine sensitive", "Diabetic patients — monitor portion"]},
            {"name": "Coconut Water with Chia", "description": "Fresh coconut water with soaked chia seeds and a squeeze of lime.", "emoji": "🥥", "tags": ["Cooling", "Hydrating", "Light"], "calories": 110, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Anytime", "mood_score": 4, "benefits": ["Coconut water cools body from inside", "Electrolytes balance nervous system", "Chia seeds provide calming Omega-3", "Natural hydration reduces irritability"], "avoid_if": ["People with high potassium levels", "Those with coconut allergy"]}
        ]
    },
    "motivated": {
        "emoji": "💪", "color": "#2DC653",
        "tagline": "Fuel your fire with power-packed foods!",
        "foods": [
            {"name": "Quinoa Buddha Bowl", "description": "Quinoa with roasted chickpeas, kale, sweet potato, tahini dressing, and seeds.", "emoji": "🥗", "tags": ["Power", "Nutritious", "Complete"], "calories": 480, "prep_time": "25 mins", "difficulty": "Medium", "best_time": "Lunch / Post-workout", "mood_score": 5, "benefits": ["Quinoa contains all 9 essential amino acids", "Iron in kale prevents energy crashes", "Sweet potato provides beta-carotene", "Chickpeas give sustained plant protein"], "avoid_if": ["People with sesame allergy — tahini", "Those with chickpea intolerance"]},
            {"name": "Black Coffee with Dark Chocolate", "description": "Strong black coffee paired with a square of 85% dark chocolate.", "emoji": "☕", "tags": ["Focus", "Energy", "Bold"], "calories": 80, "prep_time": "3 mins", "difficulty": "Easy", "best_time": "Morning / Pre-work", "mood_score": 5, "benefits": ["Caffeine boosts focus and alertness", "Dark chocolate improves blood flow to brain", "Dopamine release enhances motivation", "Antioxidants in both coffee and chocolate"], "avoid_if": ["People with anxiety — caffeine worsens it", "Those with acid reflux", "Pregnant women — limit caffeine"]},
            {"name": "Salmon & Brown Rice Bowl", "description": "Grilled salmon fillet over brown rice with steamed broccoli and soy-ginger sauce.", "emoji": "🐟", "tags": ["Omega-3", "Protein", "Brain food"], "calories": 520, "prep_time": "25 mins", "difficulty": "Medium", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Omega-3 in salmon boosts brain performance", "Complete protein for muscle recovery", "Brown rice gives sustained energy", "Broccoli rich in Vitamin K for focus"], "avoid_if": ["Fish allergy sufferers", "Vegetarians / Vegans"]},
            {"name": "Protein Energy Balls", "description": "No-bake balls with oats, peanut butter, honey, dark chocolate chips, and chia seeds.", "emoji": "⚡", "tags": ["Protein", "No-cook", "Power"], "calories": 180, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Pre-workout / Snack", "mood_score": 4, "benefits": ["Quick protein source for energy", "Oats provide slow-release carbs", "Chia seeds add Omega-3 and fiber", "Portable — eat anywhere anytime"], "avoid_if": ["Peanut allergy — serious risk", "Gluten intolerant — contains oats"]}
        ]
    },
    "nostalgic": {
        "emoji": "🥹", "color": "#E9C46A",
        "tagline": "Classic flavors that take you back in time.",
        "foods": [
            {"name": "Aloo Paratha with Butter", "description": "Crispy stuffed potato paratha with white butter, pickle, and a glass of lassi.", "emoji": "🫓", "tags": ["Classic", "Homestyle", "Comforting"], "calories": 420, "prep_time": "30 mins", "difficulty": "Medium", "best_time": "Breakfast / Lunch", "mood_score": 5, "benefits": ["Potato provides quick comfort energy", "Ghee/butter has fat-soluble vitamins", "Pickle aids digestion", "Homestyle cooking boosts emotional well-being"], "avoid_if": ["Gluten intolerant — contains wheat", "Lactose intolerant — contains butter"]},
            {"name": "Maggi Noodles", "description": "The iconic 2-minute noodles with extra vegetables and a squeeze of lime.", "emoji": "🍜", "tags": ["Nostalgic", "Quick", "Comforting"], "calories": 320, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Snack / Anytime", "mood_score": 5, "benefits": ["Instant mood lifter through nostalgia", "Iron-fortified — combats fatigue", "Quick to make — satisfies cravings fast", "Adding veggies increases nutrition"], "avoid_if": ["Gluten intolerant — contains wheat", "People on low-sodium diet — high salt"]},
            {"name": "Gulab Jamun", "description": "Soft milk solids dumplings soaked in rose cardamom sugar syrup.", "emoji": "🍮", "tags": ["Sweet", "Classic", "Festive"], "calories": 350, "prep_time": "30 mins", "difficulty": "Medium", "best_time": "Dessert / Festivals", "mood_score": 5, "benefits": ["Triggers happy childhood memories", "Sugar boosts serotonin instantly", "Rose water has calming properties", "Milk solids provide calcium and protein"], "avoid_if": ["Diabetic patients — very high sugar", "Lactose intolerant — contains milk solids"]},
            {"name": "Chai & Biscuits", "description": "Masala chai with cardamom, ginger, and milk — paired with classic glucose biscuits.", "emoji": "🍵", "tags": ["Classic", "Cozy", "Simple"], "calories": 160, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Morning / Evening", "mood_score": 5, "benefits": ["Chai spices have powerful antioxidants", "Ginger aids digestion", "Warm drink instantly soothes nerves", "Ritual of making chai is meditative"], "avoid_if": ["Lactose intolerant — contains milk", "People with caffeine sensitivity"]}
        ]
    },
    "lonely": {
        "emoji": "🥺", "color": "#A8DADC",
        "tagline": "Warm, comforting foods to make you feel held.",
        "foods": [
            {"name": "Big Bowl of Ramen", "description": "Rich tonkotsu broth with soft noodles, soft-boiled egg, nori, and mushrooms.", "emoji": "🍜", "tags": ["Warm", "Comforting", "Hearty"], "calories": 480, "prep_time": "30 mins", "difficulty": "Medium", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Warm broth mimics feeling of being cared for", "Noodles provide serotonin-boosting carbs", "Mushrooms contain Vitamin D — mood regulator", "Egg provides complete protein"], "avoid_if": ["Gluten intolerant — contains noodles", "People on low-sodium diet"]},
            {"name": "Grilled Cheese Sandwich", "description": "Golden buttery sourdough with melted cheddar and gouda — crispy outside, gooey inside.", "emoji": "🥪", "tags": ["Warm", "Cozy", "Simple"], "calories": 420, "prep_time": "10 mins", "difficulty": "Easy", "best_time": "Lunch / Snack", "mood_score": 5, "benefits": ["Cheese releases opioid-like compounds — comfort effect", "Warm food reduces feelings of social coldness", "Carbs boost serotonin production", "Simple to make — self-care act"], "avoid_if": ["Lactose intolerant — heavy cheese", "Gluten intolerant — contains bread"]},
            {"name": "Hot Chocolate with Marshmallows", "description": "Rich dark hot chocolate with mini marshmallows, whipped cream, and cinnamon.", "emoji": "☕", "tags": ["Warm", "Sweet", "Cozy"], "calories": 280, "prep_time": "5 mins", "difficulty": "Easy", "best_time": "Evening / Anytime", "mood_score": 5, "benefits": ["Hot chocolate triggers oxytocin — bonding hormone", "Dark cocoa boosts serotonin and dopamine", "Warmth in hands reduces loneliness feelings", "Magnesium in chocolate reduces sadness"], "avoid_if": ["Diabetic patients — high sugar", "Lactose intolerant — contains milk"]},
            {"name": "Dal Chawal with Ghee", "description": "Simple yellow dal poured over steaming rice with a generous spoon of ghee.", "emoji": "🍛", "tags": ["Homely", "Simple", "Nourishing"], "calories": 380, "prep_time": "25 mins", "difficulty": "Easy", "best_time": "Lunch / Dinner", "mood_score": 5, "benefits": ["Dal-chawal is the ultimate Indian comfort food", "Tryptophan in dal promotes serotonin", "Ghee has butyric acid — supports gut health", "Simple food reduces overwhelm"], "avoid_if": ["People on very low-carb diets", "Those with legume intolerance"]}
        ]
    }
}


@app.route('/api/moods', methods=['GET'])
def get_moods():
    moods = [{"id": k, "emoji": v["emoji"], "label": k.capitalize(), "color": v["color"]} for k, v in MOOD_FOODS.items()]
    return jsonify({"moods": moods})


@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get('mood', '').lower()
    if mood not in MOOD_FOODS:
        return jsonify({"error": "Mood not found"}), 404
    d = MOOD_FOODS[mood]
    return jsonify({"mood": mood, "emoji": d["emoji"], "color": d["color"], "tagline": d["tagline"], "recommendations": d["foods"]})


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Feel Good Foodie API is running!"})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
