from flask import Flask, render_template, request
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
import os

app = Flask(__name__)

# 1️: Load model and tokenizer
MODEL_PATH = os.path.join("model")  # Folder where your HuggingFace model is saved
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# 2️: Prediction function
def predict(text):
    enc = tokenizer(text, padding="max_length", truncation=True, max_length=128, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**enc).logits
        probs = torch.softmax(logits, dim=1).cpu().numpy()[0]
    label = "Hate/Offensive" if np.argmax(probs) == 1 else "Safe/Neutral"
    return {"label": label, "probability": float(probs[np.argmax(probs)])}

# 3️: Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        text = request.form["text"]
        prediction = predict(text)
    return render_template("index.html", prediction=prediction)

# 4️: Run server
if __name__ == "__main__":
    app.run(debug=True)
