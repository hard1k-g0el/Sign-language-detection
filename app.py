from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import cv2
import base64
import mediapipe as mp
from collections import Counter, deque

app = Flask("Sign Language Detection")

xgb = pickle.load(open("xgb_model.pkl", "rb"))
scaler = pickle.load(open("Standard_scaler.pkl", "rb"))

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

buffer = deque(maxlen=6)

mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.8
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["image"]

    encoded = data.split(",")[1]
    img_bytes = base64.b64decode(encoded)

    np_arr = np.frombuffer(img_bytes, np.uint8)

    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands_detector.process(rgb)

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]

        lm = []

        for point in hand.landmark:
            lm.append([point.x, point.y, point.z])

        lm = np.array(lm, dtype=np.float32)

        lm -= lm[0]

        scale = np.linalg.norm(lm[5] - lm[17])

        if scale > 0:
            lm /= scale

        test = lm.reshape(1, -1)

        test_scaled = scaler.transform(test)

        pred = xgb.predict(test_scaled)

        letter = letters[pred[0]]

        buffer.append(letter)

        stable_letter = Counter(buffer).most_common(1)[0][0]

        return jsonify({
            "prediction": stable_letter
        })

    return jsonify({
        "prediction": ""
    })


if __name__ == "__main__":
    app.run(debug=True)