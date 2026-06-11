# Sign Language Recognition System

A real-time Sign Language Recognition System that translates hand gestures representing alphabets (A–Z) into text using Computer Vision and Machine Learning.
The project uses MediaPipe Hand Tracking for landmark extraction and XGBoost for gesture classification, achieving an accuracy of **97.5%** on the collected dataset.

## Features

* Real-time hand gesture recognition using webcam
* Recognition of 26 English alphabets (A–Z)
* Landmark-based feature extraction using MediaPipe
* XGBoost classifier for gesture prediction
* Majority voting buffer to reduce prediction flickering
* Sentence formation from recognized gestures
* Backspace and space functionality
* Text-to-Speech conversion
* Flask-based web interface

## Project Workflow

1. Capture hand gestures using webcam.
2. Detect hand landmarks using MediaPipe.
3. Normalize landmarks for scale and translation invariance.
4. Transform landmarks into feature vectors.
5. Pass features through a trained XGBoost model.
6. Predict the corresponding alphabet.
7. Form words and sentences from recognized letters.
8. Convert generated text into speech.

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Scikit-Learn
* XGBoost
* Flask
* HTML
* CSS
* JavaScript

## Dataset Collection

A custom dataset was created by capturing hand landmarks for each alphabet.

### Preprocessing

* Wrist landmark used as origin.
* Translation normalization performed.
* Scale normalization using distance between landmark 5 and landmark 17.
* Flattened landmark coordinates used as model features.

Feature vector size:
21 landmarks × 3 coordinates = 63 features

## Model Training
Trained the model in jupyter notebook

### Algorithm

* XGBoost Classifier

### Hyperparameters

```python
XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```

### Performance

| Metric   | Value   |
| -------- | ------- |
| Accuracy | 97.5%   |
| Classes  | 26      |
| Model    | XGBoost |

## Confusion Matrix Analysis

The confusion matrix revealed that most alphabets were classified correctly.

Misclassifications mainly occurred between visually similar gestures.

To improve performance:

* Additional samples were collected for confusing classes.
* XGBoost was used instead of simpler classifiers.
* Prediction smoothing was implemented using majority voting.

## Project Structure

```text
SIGN_LANG/
│
├── app.py
├── xgb_model.pkl
├── Standard_scaler.pkl
├── requirements.txt
│
├── static/
│   ├── script.js
│   └── styles.css
│
├── templates/
│   └── index.html
│
└── dataset/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sign-language-recognition.git
```

Move into project directory:

```bash
cd sign-language-recognition
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate environment:

### Windows

```bash
myenv\Scripts\activate
```

### Linux / Mac

```bash
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Start Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Allow camera access when prompted.

## Future Improvements

* Support for complete ISL/ASL words
* Dynamic gesture recognition
* Transformer-based sequence models
* Mobile application deployment
* Real-time sentence auto-completion
* Speech-to-sign conversion
* User-independent adaptation

## Results

* Real-time inference
* 97.5% classification accuracy
* Smooth predictions using temporal voting
* Text generation from gestures


## Author

Hardik Goel

B.Tech Student | Machine Learning & Computer Vision Enthusiast
