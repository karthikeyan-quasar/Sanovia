from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Feedback Page
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

# Model Page
@app.route("/model")
def model():
    return render_template("model.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/tc")
def tc():
    return render_template("tc.html")
def model(text):
    symptoms = [
    "common cold",
    "influenza",
    "flu",
    "covid 19",
    "corona",
    "malaria",
    "dengue",
    "typhoid",
    "diarrhea",
    "cholera",
    "food poisoning",
    "worm infestation",
    "pneumonia",
    "tuberculosis",
    "asthma",
    "hypertension",
    "hypotension",
    "diabetes",
    "anemia",
    "skin infection",
    "scabies",
    "fungal infection",
    "snake bite",
    "dog bite",
    "heat exhaustion",
    "dehydration",
    "fracture",
    "sprain",
    "burn",
    "conjunctivitis",
    "ear infection",
    "bleeding",
    "amputation",
    "electric shock",
    "electric",
    "current",
    "hypothermia",
    "methanol poisoning",
    "centipede",
    "running nose",
    "watery nose",
    "sneezing",
    "sneeze",
    "nose dripping",
    "throat pain",
    "pain when swallowing",
    "cough",
    "coughing",
    "red throat",
    "fever",
    "warm body",
    "mild fever",
    "hot body",
    "body pain",
    "body ache",
    "body breaking",
    "tired",
    "no strength",
    "weakness",
    "fast heart",
    "heart beating fast",
    "heart racing",
    "dry cough",
    "cannot smell",
    "no smell",
    "no taste",
    "cannot taste food",
    "low oxygen",
    "breathless",
    "hard to breathe",
    "gasping for air",
    "shivering",
    "chills",
    "shaking body",
    "sweating",
    "bad headache",
    "head pain",
    "pale skin",
    "yellow skin",
    "white face",
    "bloodless look",
    "bone pain",
    "skin rash",
    "red spots",
    "eye pain",
    "pain behind eyes",
    "tiny red dots",
    "low bp",
    "feeling dizzy when standing",
    "weak pulse",
    "long fever",
    "fever not going",
    "fever for days",
    "stomach pain",
    "stomach hurts",
    "belly ache",
    "white tongue",
    "dirty tongue",
    "coated tongue",
    "severe cough",
    "bad cough",
    "short of breath",
    "rattling chest",
    "chest noise",
    "fast breathing",
    "breathing very fast",
    "cough for weeks",
    "old cough",
    "coughing blood",
    "losing weight",
    "getting thin",
    "sweating at night",
    "heavy weakness",
    "wheezing",
    "whistling chest",
    "gasping",
    "tight chest",
    "whistling sound",
    "very thirsty",
    "always thirsty",
    "peeing a lot",
    "going to pee all night",
    "cuts wont heal",
    "slow healing wounds",
    "high blood sugar",
    "high bp",
    "high blood pressure",
    "severe headache",
    "bad head pain",
    "head bursting",
    "no symptoms",
    "feels normal",
    "blurry eyes",
    "dizzy",
    "feeling spinny",
    "head spinning",
    "giddy",
    "fainting",
    "passed out",
    "everything blacked out",
    "cold hands",
    "cold feet",
    "always tired",
    "no energy",
    "body feels heavy",
    "cannot work",
    "white inner eyelids",
    "pale eyes",
    "white nails",
    "extreme thirst",
    "very dry mouth",
    "no spit",
    "dark yellow urine",
    "loose potty",
    "watery potty",
    "loose motion",
    "frequent bathroom trips",
    "vomiting",
    "throwing up",
    "dry mouth",
    "fast pulse",
    "fast heartbeat",
    "watery motion",
    "nonstop potty",
    "no energy at all",
    "sunken eyes",
    "no urine",
    "not peeing",
    "passing out",
    "stomach cramps",
    "stomach twisting",
    "stomach painful to touch",
    "belly hurts when pressed",
    "sweating a lot",
    "tired in sun",
    "faint from heat",
    "cool wet skin",
    "clammy skin",
    "headache",
    "uncontrollable shivering",
    "slurred speech",
    "stuttering",
    "confused",
    "acting strange",
    "freezing cold",
    "cold skin",
    "very low body temperature",
    "slow heart",
    "intense pain",
    "skin redness",
    "blister",
    "water blisters",
    "burn",
    "fire burn",
    "hot water burn",
    "burnt area",
    "charred skin",
    "black skin",
    "peeling skin",
    "severe bone pain",
    "broken bone",
    "broken arm",
    "broken leg",
    "swelling",
    "crooked arm",
    "crooked leg",
    "bone popping out",
    "cannot move limb",
    "joint pain",
    "ankle pain",
    "wrist pain",
    "rapid swelling",
    "catch",
    "sprain",
    "twisted foot",
    "painful to touch",
    "black and blue skin",
    "bruised joint",
    "snake bite",
    "snake bit",
    "snake puncture",
    "snake teeth marks",
    "spreading swelling",
    "swelling going up",
    "cold sweat",
    "dog bite",
    "dog attacked",
    "animal teeth mark",
    "deep cut",
    "flesh torn",
    "flesh showing",
    "bone showing",
    "heavy bleeding",
    "bee sting",
    "wasp sting",
    "honeybee",
    "swelling at sting spot",
    "red lump",
    "choking",
    "scorpion",
    "scorpion sting",
    "scorpion ",
    "extreme burning pain",
    "pain ",
    "burning pain",
    "centipede",
    "two small dot marks",
    "local swelling",
    "severe muscle pain",
    "numbness",
    "unconscious",
    "current shock",
    "electric shock",
    "burn marks from wire",
    "stiff muscles",
    "tight body",
    "irregular heart",
    "heart jumping",
    "severe pain",
    "body part crushed",
    "body part trapped",
    "heavy weight fell on limb",
    "dark urine",
    "black urine",
    "numb limb",
    "blood spurting",
    "blood flowing fast",
    "cut finger",
    "ear pain",
    "earache",
    "red inside ear",
    "pus from ear",
    "fluid leaking from ear",
    "ear draining",
    "red eye",
    "pink eye",
    "sticky eye",
    "eye discharge",
    "infected eye",
    "red eyeballs",
    "itchy eye",
    "watery eyes",
    "sharp eye pain",
    "something in eye",
    "dirt in eye",
    "dust in eye",
    "visible speck in eye",
    "scratchy feeling",
    "red skin",
    "swollen skin",
    "boil",
    "pus",
    "skin infection",
    "warm skin",
    "hot to touch",
    "itchy circular rash",
    "round rash",
    "itchy skin",
    "ring rash",
    "ringworm",
    "circle mark on skin",
    "red border rash",
    "itching",
    "scratching",
    "scratching all night",
    "small pimples",
    "lines on skin",
    "rash between fingers",
    "burrows",
    "intense itching",
    "itching in bottom",
    "worms in potty",
    "grinding teeth at night",
    "bloated stomach",
    "swollen belly",
    "blurry vision",
    "cannot see clearly",
    "blindness",
    "fake alcohol",
    "bad liquor",
    "big wide eyes",
    "pupils not moving"
]
    user = text.lower()
    user_symp=[]
    for i in symptoms:
        if i in user:
            user_symp.append(i)
    disease = {
    "Common Cold": ["$common cold","$running nose", "$watery nose", "$sneezing", "$sneeze", "$nose dripping",
                    "throat pain", "pain when swallowing", "cough", "coughing", "red throat", "fever", "warm body", "mild fever"],

    "Influenza (Flu)": ["$influenza","$fever", "$hot body", "$body pain", "$body ache", "$body breaking", "$tired", "$no strength", "$weakness",
                         "cough", "sore throat", "throat pain", "fast heart", "heart beating fast", "heart racing"],

    "COVID-19": ["$corona","$covid 19","$fever", "$cough", "$dry cough", "$cannot smell", "$no smell", "$no taste", "$cannot taste food",
                 "low oxygen", "breathless", "hard to breathe", "gasping for air"],

    "Malaria": ["$malaria","$fever", "$shivering", "$chills", "$shaking body", "$sweating", "$bad headache", "$head pain",
                "pale skin", "yellow skin", "white face", "bloodless look"],

    "Dengue Fever": ["$dengue","$fever", "$bad headache", "$body pain", "$bone pain", "$skin rash", "$red spots", "$eye pain", "$pain behind eyes",
                      "tiny red dots", "low bp", "feeling dizzy when standing", "weak pulse"],

    "Typhoid Fever": ["$typhoid","$long fever", "$fever not going", "$fever for days", "$stomach pain", "$stomach hurts", "$belly ache",
                      "white tongue", "dirty tongue", "coated tongue"],

    "Pneumonia": ["$pneumonia","$severe cough", "$bad cough", "$fever", "$breathlessness", "$hard to breathe", "$short of breath",
                  "rattling chest", "chest noise", "fast breathing", "breathing very fast"],

    "Tuberculosis": ["$tuberculosis","$cough for weeks", "$old cough", "$coughing blood", "$losing weight", "$getting thin", "$sweating at night",
                     "chest noise", "rattling lung", "heavy weakness"],

    "Asthma": ["$asthma","$wheezing", "$whistling chest", "$cough", "$breathlessness", "$gasping", "$tight chest",
               "whistling sound", "breathing very fast", "rapid breathing"],

    "Diabetes": ["$diabetes","$very thirsty", "$always thirsty", "$peeing a lot", "$going to pee all night", "$losing weight",
                 "cuts wont heal", "slow healing wounds", "high blood sugar"],

    "Hypertension": ["$hypertension","$high bp", "$high blood pressure", "$severe headache", "$bad head pain", "$head bursting",
                     "no symptoms", "feels normal", "blurry eyes"],

    "Hypotension": ["$hypotension","$dizzy", "$feeling spinny", "$head spinning", "$giddy", "$fainting", "$passed out", "$everything blacked out",
                    "pale skin", "low bp", "cold hands", "cold feet"],

    "Anemia": ["$anemia","$always tired", "$no energy", "$heavy weakness", "$body feels heavy", "$cannot work",
               "white inner eyelids", "pale eyes", "white nails", "fast heart"],

    "Dehydration": ["$dehydration","$very thirsty", "$extreme thirst", "$dizzy", "$feeling spinny",
                    "very dry mouth", "no spit", "fast heart", "low bp", "dark yellow urine"],

    "Acute Diarrhea": ["$diarrhea","$loose potty", "$watery potty", "$loose motion", "$frequent bathroom trips", "$vomiting", "$throwing up",
                       "dry mouth", "very thirsty", "fast pulse", "fast heartbeat"],

    "Cholera": ["$cholera","$loose potty", "$watery motion", "$nonstop potty", "$extreme thirst", "$no energy at all",
                "low bp", "sunken eyes", "no urine", "not peeing", "fainting", "passing out"],

    "Food Poisoning": ["$food poisoning","$vomiting", "$throwing up", "$loose potty", "$stomach cramps", "$stomach twisting",
                       "fever", "stomach painful to touch", "belly hurts when pressed"],

    "Heat Exhaustion": ["$heat exhaustion","$sweating a lot", "$dizzy", "$giddy", "$feeling spinny", "$tired in sun", "$faint from heat",
                        "cool wet skin", "clammy skin", "fast pulse", "headache"],

    "Hypothermia": ["$hypothermia","$uncontrollable shivering", "$slurred speech", "$stuttering", "$confused", "$acting strange", "$freezing cold",
                    "cold skin", "pale skin", "very low body temperature", "slow heart"],

    "Burns": ["$burn","$intense pain", "$skin redness", "$blister", "$water blisters", "$burn", "$fire burn", "$hot water burn",
              "burnt area", "charred skin", "black skin", "peeling skin"],

    "Fracture": ["$fracture","$severe bone pain", "$broken bone", "$broken arm", "$broken leg", "$swelling",
                 "crooked arm", "crooked leg", "bone popping out", "cannot move limb"],

    "Sprain": ["$sprain","$joint pain", "$ankle pain", "$wrist pain", "$rapid swelling", "$catch", "$twisted foot",
               "painful to touch", "black and blue skin", "bruised joint"],

    "Snake Bite": ["$snake bite","$snake bit", "$snake puncture", "$snake teeth marks",
                   "spreading swelling", "swelling going up", "fainting", "cold sweat", "hard to breathe"],

    "Dog Bite": ["$dog bite","$dog bit", "$dog attacked", "$animal teeth mark", "$deep cut",
                 "flesh torn", "flesh showing", "bone showing", "heavy bleeding"],

    "Bee/Wasp Sting": ["$bee sting","$wasp sting", "$honeybee",
                       "swelling at sting spot", "red lump", "low bp", "choking", "hard to breathe"],

    "Scorpion Sting": ["$scorpion","$scorpion sting", "$scorpion bite",
                       "fast heart", "extreme burning pain", "sweating a lot"],

    "Centipede Bite": ["$centipede","$pain in one spot", "$burning pain", "$centipede bite",
                       "two small dot marks", "local swelling", "fast heart"],

    "Electric Shock": ["$electric shock","$current", "$severe muscle pain", "$numbness", "$passed out", "$unconscious",
                       "burn marks from wire", "stiff muscles", "tight body", "irregular heart", "heart jumping"],

    "Crush Injury": ["$severe pain", "$body part crushed", "$body part trapped", "$heavy weight fell on limb",
                     "dark urine", "black urine", "fast heart", "low bp", "numb limb"],

    "Severe Bleeding / Amputation": ["$amputation","$bleeding","$severe bleeding", "$blood spurting", "$blood flowing fast", "$dizzy", "$cold sweat", "$deep cut", "$cut finger",
                                     "flesh torn", "fast heart", "weak pulse", "low bp", "passing out"],

    "Ear Infection": ["$ear infection","$ear pain", "$earache", "$fever",
                      "red inside ear", "pus from ear", "fluid leaking from ear", "ear draining"],

    "Conjunctivitis": ["$conjunctivitis","$red eye", "$pink eye", "$sticky eye", "$eye discharge", "$infected eye",
                       "red eyeballs", "itchy eye", "watery eyes"],

    "Foreign Body in Eye": ["$sharp eye pain", "$something in eye", "$dirt in eye", "$dust in eye",
                            "visible speck in eye", "scratchy feeling", "red eye"],

    "Skin Infection": ["$skin infection","$red skin", "$swelling", "$swollen skin", "$pain in one spot", "$boil", "$pus", "$skin infection",
                       "warm skin", "hot to touch", "mild fever"],

    "Fungal Infection": ["$fungal infection","$itchy circular rash", "$round rash", "$itchy skin", "$ring rash",
                         "ringworm", "circle mark on skin", "red border rash"],

    "Scabies": ["$scabies","$itching", "$scratching", "$scratching all night", "$skin rash", "$small pimples",
                "lines on skin", "rash between fingers", "burrows"],

    "Worm Infestation": ["$worm infestation","$stomach pain", "$belly ache", "$intense itching", "$itching in bottom", "$losing weight", "$getting thin",
                         "worms in potty", "grinding teeth at night", "bloated stomach", "swollen belly"],

    "Methanol Poisoning": ["$methanol","$methanol poisoning","$blurry vision", "$cannot see clearly", "$blindness", "$stomach pain", "$vomiting", "$fake alcohol", "$bad liquor",
                           "big wide eyes", "pupils not moving", "gasping for air", "low bp"]
    }
    score = {
    "Common Cold": 0,
    "Influenza (Flu)": 0,
    "COVID-19": 0,
    "Malaria": 0,
    "Dengue Fever": 0,
    "Typhoid Fever": 0,
    "Pneumonia": 0,
    "Tuberculosis": 0,
    "Asthma": 0,
    "Diabetes": 0,
    "Hypertension": 0,
    "Hypotension": 0,
    "Anemia": 0,
    "Dehydration": 0,
    "Acute Diarrhea": 0,
    "Cholera": 0,
    "Food Poisoning": 0,
    "Heat Exhaustion": 0,
    "Hypothermia": 0,
    "Burns": 0,
    "Fracture": 0,
    "Sprain": 0,
    "Snake Bite": 0,
    "Dog Bite": 0,
    "Bee/Wasp Sting": 0,
    "Scorpion Sting": 0,
    "Centipede Bite": 0,
    "Electric Shock": 0,
    "Crush Injury": 0,
    "Severe Bleeding / Amputation": 0,
    "Ear Infection": 0,
    "Conjunctivitis": 0,
    "Foreign Body in Eye": 0,
    "Skin Infection": 0,
    "Fungal Infection": 0,
    "Scabies": 0,
    "Worm Infestation": 0,
    "Methanol Poisoning": 0
}
    keys=list(disease)
    for i in keys:
        count=0
        samp_disease= disease[i]
        for j in user_symp:
            for k in samp_disease:
                if j in k and '$'in k:
                    count+=5
                elif j in k:
                    count+=1
        score[i]=count
    max_score=0  
    index = []
    for i in keys:
        if score[i]>max_score:
            max_score = score[i]
    for i in keys:
        if score[i]==max_score:
            index.append(i)
    cure = {
    "Common Cold": "Rest in bed and drink warm water. Breathe in steam to clear your nose. Go to a doctor if a high fever lasts more than three days.",

    "Influenza (Flu)": "Stay alone in a room to protect others. Rest completely and drink plenty of fluids. Go to a hospital quickly if you have trouble breathing.",

    "COVID-19": "Stay isolated at home. Check your oxygen level with a machine every six hours. Go to the hospital immediately if oxygen drops below 94 percent.",

    "Malaria": "Look for danger signs like constant vomiting or extreme weakness. Sponge the body with cool water to lower fever. Get a blood test immediately.",

    "Dengue Fever": "Drink plenty of coconut water, juices, or ORS liquid. Do not take pain killers like ibuprofen. Watch for bleeding from gums or severe stomach pain.",

    "Typhoid Fever": "Eat soft food and drink plenty of clean water. If the stomach swells, vomiting continues, or fever stays high after five days, go to the hospital.",

    "Acute Diarrhea": "Drink ORS solution every time you pass watery stool. Check if the skin or mouth feels dry. Go to the hospital if you see blood in stool.",

    "Cholera": "If the patient is very weak, start giving ORS water if they can swallow. Take them immediately to an emergency hospital for life-saving IV fluids.",

    "Food Poisoning": "Do not give solid food for a few hours. Give small sips of ORS water frequently. See a doctor if vomiting does not stop or if stool has blood.",

    "Worm Infestation": "Keep hands clean and cut fingernails short. Wash all clothes and bed sheets in hot water. Go to a clinic if the person looks very pale.",

    "Pneumonia": "Sit up straight to breathe easily. Use oxygen if available. Go to the hospital immediately if breathing is very fast or if the patient is confused.",

    "Tuberculosis": "Give the patient a mask to wear. Keep them in a well-ventilated room. Go to a government center for a sputum test and chest X-ray.",

    "Asthma": "Sit upright and loosen tight clothes. Inhale 2 to 4 puffs of your inhaler immediately. Go to the emergency room if you cannot speak a full sentence.",

    "Hypertension": "Rest quietly for 15 minutes and recheck blood pressure. Reduce salt intake, walk daily, and stop smoking. Seek emergency care if BP is extremely high.",

    "Hypotension": "Make the patient lie flat and raise their legs. Give ORS water if they are alert. Go to the hospital if they remain faint.",

    "Diabetes": "Check blood sugar immediately. Go to the emergency room if the patient is confused or breathing very fast with a fruity breath smell.",

    "Anemia": "Look for causes like heavy bleeding. Get a blood test. Visit a doctor if dizziness or shortness of breath is severe.",

    "Skin Infection": "Clean the affected area with antiseptic. Mark the red border to monitor spreading. Go to the hospital if redness spreads rapidly.",

    "Scabies": "Cut fingernails short. Treat everyone in the household at the same time. Wash all clothes and bedding in hot water.",

    "Fungal Infection": "Keep the affected area clean and dry. Wear loose cotton clothes. Avoid sharing towels or combs. See a dermatologist if it spreads.",

    "Snake Bite": "Keep the person completely still to stop venom spread. Tie a simple splint to support the limb below heart level. Go to a big hospital immediately.",

    "Dog Bite": "Wash the bite wound with running water and soap for 15 minutes. Do not stitch the wound. Go to a rabies clinic immediately for life-saving injections.",

    "Scorpion Sting": "Wash with soap and water. Apply a cloth-wrapped ice pack to reduce pain. Go to the hospital if you notice constant vomiting or heavy sweating.",

    "Bee/Wasp Sting": "Remove the stinger gently with a flat edge. Apply a cold cloth. Go to the hospital immediately if the face swells or breathing becomes difficult.",

    "Heat Exhaustion": "Move the person to a cool shade. Lie them down and lift their feet. Give them cool ORS water or normal water to drink slowly.",

    "Dehydration": "Check how dry the mouth or skin feels. Give small sips of ORS water very frequently. Take the person to a clinic if they become too sleepy.",

    "Fracture": "Support and tie the broken bone with a straight wooden stick so it cannot move. Do not give food or water. Take them to an orthopedic hospital.",

    "Sprain": "Rest the joint completely. Apply ice packs for 15 minutes. Wrap a tight stretchy bandage around it and keep the leg or arm lifted high.",

    "Burns": "Pour clean, cool tap water over the burn for 20 minutes. Remove rings or tight clothes. Cover loosely with a clean cloth. Do not use ice or paste.",

    "Conjunctivitis": "Clean eye crust gently with a wet cotton ball from inside to outside corner. Wash hands often. See an eye doctor if vision changes or pain increases.",

    "Ear Infection": "Keep the ear completely dry; do not put water or cotton buds inside. Apply a warm cloth outside for pain. See a doctor if foul-smelling pus flows.",

    "Severe Bleeding / Amputation": "Press a clean, thick cloth firmly on the wound to stop bleeding. Raise the injured limb if possible. Rush to a surgical hospital immediately.",

    "Crush Injury": "Remove the trapped heavy object safely. Keep the crushed limb steady at heart level. Take the person to the nearest emergency hospital immediately.",

    "Electric Shock": "Turn off the main power before touching the person. Begin CPR if they have no pulse or are not breathing. Cover burns and go to the hospital.",

    "Hypothermia": "Move the person to a warm place. Remove wet clothes and wrap them in warm blankets. Give warm sweet drinks only if they are fully awake.",

    "Foreign Body in Eye": "Do not rub the eye. Rinse it with plenty of clean water or saline. If pain or blurred vision continues, cover the eye loosely and seek medical care.",

    "Methanol Poisoning": "Keep the airway open and place the person on their side if vomiting. Do not induce vomiting. Rush immediately to a hospital.",

    "Centipede Bite": "Wash the bite area with soap and water. Apply a hot or cold compress to reduce pain. Seek medical care if swelling becomes severe or the skin changes color."
    }

    disease_detected = index[0]
    if max_score == 0:
        return 'You said: '+text+' Disease detected: None cure: None'
    else:
        return 'You said: '+text+' Disease detected: '+disease_detected+' cure: '+cure[disease_detected] 
# Voice Processing
@app.route("/process", methods=["POST"])
def process():

    data = request.get_json()

    text = data["text"]

    text = text.lower()
    result = model(text)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)