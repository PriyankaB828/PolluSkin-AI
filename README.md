# PolluSkin AI

An AI-powered skin and scalp health analysis system that combines deep learning and real-time pollution data to provide condition prediction, pollutant impact analysis, and personalized recommendations.

---

## Overview

PolluSkin AI is an intelligent healthcare application that analyzes skin and scalp conditions such as acne and hair loss using deep learning models. The system also integrates real-time air quality data to identify environmental factors that may contribute to the detected condition.

By combining computer vision with pollution intelligence, PolluSkin AI provides more context-aware insights than traditional image-only analysis systems.

---

## Problem Statement

Air pollution can significantly affect skin and scalp health, leading to issues such as acne, inflammation, premature aging, and hair loss. Most existing AI-based diagnostic systems focus only on image analysis and ignore environmental influences.

PolluSkin AI addresses this gap by integrating:

* Deep learning-based image classification
* Real-time pollution monitoring
* Pollutant impact analysis
* Personalized recommendations

---

## Features

* Skin and scalp condition classification (Acne, Normal Skin, Hair Loss, Healthy Scalp)
* Deep learning-based prediction using MobileNetV2 with confidence score visualization
* Real-time Air Quality Index (AQI) analysis through WAQI API integration
* Pollutant impact and cause analysis for environmental health assessment
* Personalized skincare, scalp-care, and product recommendations
* Image upload, camera capture, and interactive result dashboard support

---

## Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### AI & Computer Vision

* TensorFlow
* Keras
* MobileNetV2
* OpenCV
* NumPy

### APIs

* WAQI API

### Development Tools

* VS Code
* Git
* GitHub
* Jupyter Notebook

---

## System Architecture

```text
User
   ↓
Image Upload / Camera Capture
   ↓
Image Preprocessing
   ↓
MobileNetV2 Prediction Model
   ↓
Condition Classification
   ↓
WAQI API
   ↓
Pollution Data Analysis
   ↓
Pollutant Cause Analysis
   ↓
Recommendations & Results
```

---

## Project Structure

```text
PolluSkin_AI/
│
├── dataset/
│   ├── Skin/
│   └── Scalp/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── train_skin.py
├── train_scalp.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. User uploads or captures a skin/scalp image.
2. The image is preprocessed and resized for analysis.
3. MobileNetV2 models extract visual features and predict the skin or scalp condition.
4. Real-time pollution data is fetched using the WAQI API.
5. Pollutants are analyzed to identify major environmental factors affecting the detected condition.
6. Personalized recommendations and results are generated and displayed.

---

## Model Information

### Classification Categories

#### Skin

* Acne
* Normal Skin

#### Scalp

* Hair Loss
* Healthy Scalp

### Model

* MobileNetV2 (Transfer Learning)
* Adam Optimizer
* Categorical Cross-Entropy Loss
* Data Augmentation
* 80:20 Train-Validation Split

---

## Performance

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Validation Loss

### Results

* Model Accuracy: **85% – 92%**
* MobileNetV2 outperformed the baseline CNN model.
* Achieved reliable prediction performance for both skin and scalp classification tasks.

---

## Screenshots

### Home Page

* Image Upload
* Camera Capture
* City Input

### Result Dashboard

* Predicted Condition
* Confidence Score
* AQI Information
* Pollutant Analysis
* Personalized Recommendations


     <img width="483" height="449" alt="image" src="https://github.com/user-attachments/assets/f49554e9-26aa-492b-ae91-f343a7a10d35" />

   <img width="618" height="601" alt="image" src="https://github.com/user-attachments/assets/3b882fc8-840c-42c1-9d3b-04f222983042" />

   <img width="862" height="388" alt="image" src="https://github.com/user-attachments/assets/5cafeb71-7a2a-40ac-ad87-f62fb0d920b3" />

   <img width="653" height="487" alt="image" src="https://github.com/user-attachments/assets/e5583acb-6319-4d31-a7bc-3500e586cf5d" />

   <img width="748" height="569" alt="image" src="https://github.com/user-attachments/assets/f2627abc-ec52-4a6f-ac1f-a1aacc49556d" />


---

## Project Highlights

* Developed a multimodal AI healthcare application.
* Built separate deep learning models for skin and scalp analysis.
* Implemented MobileNetV2 transfer learning architecture.
* Integrated real-time pollution monitoring using WAQI API.
* Developed pollutant cause analysis for environmental impact assessment.
* Generated personalized recommendations based on prediction results.
* Designed a user-friendly web interface for image-based diagnosis.

---

## Skills Demonstrated

* Python Programming & Flask Development
* Deep Learning, TensorFlow, Keras & Transfer Learning
* Computer Vision, OpenCV & MobileNetV2
* API Integration & Environmental Data Analysis
* Healthcare AI, Data Preprocessing & Model Evaluation
* Git & GitHub

---

## Future Enhancements

* Support for additional skin diseases
* Mobile application deployment
* Advanced recommendation system
* EfficientNet and ResNet integration
* Explainable AI visualizations
* Cloud deployment and scalability
* User authentication and history tracking

---

## Author

### Priyanka B
