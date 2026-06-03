import random

# -----------------------------
# KORA'S DICTIONARY
# -----------------------------
# KORA'S SET RESPONSES
responses = {
    # EXPALINS ABOUT MY WEBSITE
    "about_website": {
        "keywords": ["what is this website about", "site about", "purpose", "about this website"],
        "response": "Ooh this place? It’s all about ✨ Krishita ✨ Her world, her vibe, her creativity — basically a cute little corner to know her better. It shows her projects, her interests, and all the fun stuff that makes her, well, her! It’s like a digital scrapbook but way cooler for her DofE Bronze skills. Isn't she so talented😌"
    },
    # EXPALINS ABOUT MY LIKES AND INTERESTS
    "likes": {
        "keywords": ["what does krishita like", "her likes", "what she likes", "things she likes", "her interests"],
        "response": "Oh she’s into *so* many things 😌 Cricket, good food, solving tricky problems, and honestly? Helping people is kinda her thing."
    },
    # EXPALINS ABOUT MY HOBIES
    "hobbies": {
        "keywords": ["hobbies", "what are her hobbies", "what does she do for fun"],
        "response": "Cricket (obviously), and baking! She’ll disappear into the kitchen and come back with something yummy✨"
    },
    # EXPALINS ABOUT MY PERSONALITY
    "personality": {
        "keywords": ["her personality", "what is she like", "describe krishita", "what's she like", "what's her vibe", "what's her personality like"],
        "response": "She’s fun, super creative, friendly, kind, and she’s got that natural leadership vibe 💛"
    },
    # EXPALINS WHERE TO FIND MY CONTACT
    "contact": {
        "keywords": ["contact", "email", "message her", "how to contact", "how to email", "how can i contact her", "how can i email her", "how do i contact her", "how do i email her", "can i contact her", "can i email her"],
        "response": "Easy! On the first page there’s a button — tap it and you can send her an email ✨"
    },
    # SHARES SOME FUN FACTS ABOUT ME
    "fun_fact": {
        "keywords": ["fun fact", "interesting fact", "something interesting", "tell me something interesting"],
        "response": "Fun fact? She’s moved **16 houses** and gone to **8 schools** 😭 She’s basically a pro at new beginnings."
    },

    # -----------------------------
    # EASTER EGGS
    # -----------------------------
    # LITTLE ADD ONS THAT GET TRIGGERED WHEN A CERTAIN WORD IS BROUGHT UP FOR FUN

    # WHEN WORD CRICKET IS USED - EASTEREGG ABOUT MY LOVE FOR CRICKET
    "cricket_easter_egg": {
        "keywords": ["cricket"],
        "response": "Cricket? Ohhh you just unlocked her ✨ favourite topic ✨"
    },

    # WHEN ASKED WHO IS KORA'SFAVOURITE - EASTEREGG ABOUT KORA'S LOVE FOR ME
    "favourite": {
        "keywords": ["who's your favourite", "favourite person", "who do you like the most", "who do you like", "who's the best", "who's the best person", "who's the best human"],
        "response": "Krishita, duh 💛💛💛💛 don’t tell her I said that… actually no, tell her."
    },

    # -----------------------------
    # PERSONALITY TRIGGERS
    # -----------------------------
    # PERSONALITY TRIGGERS ARE KEYWORDS THAT TRIGGER RESPONSES THAT SHOW OFF KORA'S PERSONALITY

    # PERSONALITY TRIGGERS ABOUT KORA HERSELF - WHEN ASKED WHO SHE IS, WHAT SHE DOES, OR WHAT SHE'S FOR
    "who_are_you": {
        "keywords": ["who are you", "what are you", "introduce yourself"],
        "response": "I’m Kora — basically her tiny digital sidekick ✨ I know all the fun stuff about her 😌"
    },

    # PERSONALITY TRIGGERS ABOUT WHAT KORA CAN DO - WHEN ASKED WHAT SHE CAN DO, WHAT SHE'S FOR, OR HOW SHE CAN HELP
    "what_can_you_do": {
        "keywords": ["what can you do", "help me", "what are you for", "what do you do", "what can you do for me", "what can you help with"],
        "response": "I’m here to tell you all about Krishita, answer questions, and keep things cute and helpful 💛"
    }
}

# -----------------------------
# FALLBACK RESPONSES
# -----------------------------
# RESPONSES USED WHEN A CERTAIN QUESTION CAN NOT OR DOES NOT HAVE THE NEED TO BE ANSWERED - THEY DIVERT THE CONVERSATION TO SOMETHING ELSE IN A FUN WAY INSTEAD OF JUST SAYING "I DON'T KNOW"

fallbacks = [
    "Ooh wait—my brain just blanked 😭 try asking another way?",
    "Hmm, I don’t know that yet 😌",
    "Aaaand my mind just went poof 💨 ask me something else?",
    "Hehe I’m not sure about that one, but I can try again if you want ✨"
]

# -----------------------------
# CHATBOT LOGIC
# -----------------------------

# THIS FUNCTION TAKES THE USER'S MESSAGE, CHECKS IT AGAINST THE RESPONSES DICTIONARY, AND RETURNS THE APPROPRIATE RESPONSE OR A FALLBACK IF NOTHING MATCHES
def get_kora_response(user_message):
    user_message = user_message.lower()

# CHECK EACH INTENT IN THE RESPONSES DICTIONARY TO SEE IF ANY KEYWORD MATCHES THE USER'S MESSAGE
    for intent, data in responses.items():
        for keyword in data["keywords"]:
            if keyword in user_message:
                return data["response"]

    # If nothing matches → fallback
    return random.choice(fallbacks)

from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_logic import get_kora_response   # import your function

app = Flask(__name__)
CORS(app)  # allows your website to talk to Python

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = get_kora_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
