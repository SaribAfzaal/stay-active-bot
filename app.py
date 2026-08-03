from flask import Flask, jsonify
import random

app = Flask(__name__)

MESSAGES = {
    "stretch": [
        "Time to stand up and stretch your arms and back for a minute.",
        "Roll your shoulders and stretch your neck gently.",
        "Stand up, reach for the ceiling, and stretch your spine."
    ],
    "eyes": [
        "Look away from your screen for 20 seconds and focus on something far away.",
        "Blink a few times and rest your eyes for a moment.",
        "Give your eyes a break — look out a window if you can."
    ],
    "hydrate": [
        "Grab a glass of water and take a sip.",
        "Time to hydrate — drink some water.",
        "Don't forget to drink water this hour."
    ],
    "walk": [
        "Take a short 2-3 minute walk around your space.",
        "Stand up and walk around for a bit.",
        "Step away from your desk and walk a little."
    ]
}

@app.route("/reminder", methods=["GET"])
def get_reminder():
    category = random.choice(list(MESSAGES.keys()))
    message = random.choice(MESSAGES[category])
    return jsonify({
        "category": category,
        "message": message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)