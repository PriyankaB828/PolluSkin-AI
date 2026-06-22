from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
import pandas as pd

app = Flask(__name__)

# Load models
skin_model = tf.keras.models.load_model("model/skin_model.h5")
scalp_model = tf.keras.models.load_model("model/scalp_model.h5")

# Load pollution dataset
pollution_data = pd.read_csv("dataset/pollution.csv")
pollution_data.columns = pollution_data.columns.str.lower()
pollution_data["city"] = pollution_data["city"].str.lower()


# Image preprocessing
def preprocess_image(file):
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


# Recommendations
def get_recommendations(result, pollution_level):
    suggestions = []
    products = []

    result = result.lower()

    if "acne" in result:
        suggestions = [
            "Use gentle face cleanser",
            "Avoid oily food",
            "Stay hydrated"
        ]
        products = [
            "Cetaphil Cleanser",
            "Niacinamide Serum",
            "Sunscreen SPF 50"
        ]

    elif "hair loss" in result or "alopecia" in result:
        suggestions = [
            "Massage scalp regularly",
            "Reduce stress",
            "Avoid harsh shampoos"
        ]
        products = [
            "Biotin Shampoo",
            "Hair Growth Serum",
            "Anti-Hair Fall Oil"
        ]

    if pollution_level.lower() in ["unhealthy", "very unhealthy"]:
        suggestions.append("Avoid going out in high pollution")
        products.append("Anti-Pollution Face Wash")

    return suggestions, products


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    uploaded_file = request.files.get("image")
    analysis_type = request.form.get("type")
    city = request.form.get("city")

    if not uploaded_file:
        return "No image uploaded"

    img = preprocess_image(uploaded_file)

    # ================= MODEL =================
    if analysis_type == "skin":
        prediction = skin_model.predict(img)
        confidence = float(prediction[0][0])

        if confidence > 0.5:
            result = "Acne / Rosacea Detected"
        else:
            result = "Skin Looks Normal"

    else:
        prediction = scalp_model.predict(img)
        confidence = float(prediction[0][0])

        if confidence > 0.5:
            result = "Hair Loss / Alopecia Detected"
        else:
            result = "Scalp Looks Healthy"

    confidence = round(confidence * 100, 2)

    # ================= POLLUTION =================
    aqi = "Not Available"
    pollution_level = "Unknown"

    if city:
        city = city.strip().lower()

        pollution_row = pollution_data[
            pollution_data["city"].str.contains(city)
        ]

        if not pollution_row.empty:
            aqi = int(pollution_row["pollutant_avg"].max())

            if aqi < 50:
                pollution_level = "Good"
            elif aqi < 100:
                pollution_level = "Moderate"
            elif aqi < 200:
                pollution_level = "Unhealthy"
            else:
                pollution_level = "Very Unhealthy"

    # ================= RECOMMENDATION =================
    suggestions, products = get_recommendations(result, pollution_level)

    # ================= RETURN =================
    return render_template(
        "result.html",
        result=result,
        confidence=confidence,
        city=city,
        aqi=aqi,
        pollution_level=pollution_level,
        suggestions=suggestions,
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)