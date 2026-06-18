# Smart Mental Stress Detection and Risk Prediction System

## 1. Project Title

Smart Mental Stress Detection and Risk Prediction System

---

## 2. Project Objective

The purpose of this project is to develop a web-based machine learning application that predicts the stress level of students based on academic, lifestyle, and mental health factors.

The system will analyze user-provided information and classify the user into Low Stress, Medium Stress, or High Stress categories.

The application will also compare multiple machine learning algorithms and display their performance through a dashboard.

---

## 3. Problem Statement

Students often experience stress due to academic pressure, lack of sleep, excessive screen time, financial concerns, and workload.

Most students do not realize their stress level until it starts affecting their academic performance and health.

This project aims to provide an intelligent system that predicts stress levels early and helps users understand their mental health condition.

---

## 4. Dataset

Dataset Name: Student Depression Dataset

Source: Kaggle

Dataset Link: https://www.kaggle.com/datasets/hopesb/student-depression-dataset

Target Variable: Stress Level

Possible Classes:

- Low
- Medium
- High

---

## 5. Functional Requirements

### User Registration

User registration is optional.

The user can access the system and enter personal information.

### User Input Module

The system must allow users to enter:

- Age
- Gender
- CGPA
- Study Hours Per Day
- Sleep Hours Per Day
- Academic Pressure
- Financial Stress
- Study Satisfaction
- Exercise Hours
- Screen Time
- Social Media Usage
- Mood Score
- Anxiety Level
- Sleep Quality

### Prediction Module

The system will:

- Receive user inputs
- Preprocess input values
- Apply trained ML model
- Predict stress level
- Display prediction results

### Recommendation Module

Based on predicted stress level:

Low Stress:

- Continue healthy lifestyle

Medium Stress:

- Improve sleep schedule
- Reduce screen time

High Stress:

- Consult counselor
- Improve work-life balance
- Increase physical activity

### Dashboard Module

Display model comparison results.

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Training Time
- Confusion Matrix
- ROC-AUC

---

## 6. Non-Functional Requirements

- System should be easy to use.
- Response time should be less than 3 seconds.
- Interface should be user-friendly.
- System should work on desktop browsers.
- Models must run locally.
- No external APIs are allowed.

---

## 7. Machine Learning Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine

---

## 8. Data Preprocessing

- Remove missing values
- Handle categorical values
- Apply label encoding
- Apply feature scaling
- Split dataset into training and testing data
- Use 80% training data and 20% testing data

---

## 9. Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Training Time

---

## 10. System Output

Example:

Stress Level: HIGH

Risk Score: 82%

Recommendation:

- Improve sleep duration
- Reduce screen time
- Exercise regularly
- Take study breaks

---

## 11. Web Pages

### Home Page

- Project introduction
- Project objective
- Dataset information

### Prediction Page

- User input form
- Predict button
- Prediction result
- Risk score
- Recommendation

### Dashboard Page

- Model comparison table
- Accuracy chart
- Precision chart
- Recall chart
- F1 Score chart
- Training Time chart
- Confusion Matrix

### About Page

- Project details
- Algorithms used
- Developer information

---

## 12. Updated Technology Stack Without Streamlit

Frontend:

- HTML
- CSS
- JavaScript
- Bootstrap

Backend:

- Python Flask

Machine Learning:

- Scikit-Learn

Visualization:

- Matplotlib
- Seaborn
- Chart.js

Data Processing:

- Pandas
- NumPy

Model Saving:

- Joblib

---

## 13. Updated Project Folder Structure Without Streamlit

```text
MentalStressDetection/
|
|-- app.py
|-- train_model.py
|-- stress_dataset.csv
|-- model.pkl
|-- scaler.pkl
|-- requirements.txt
|-- README.md
|
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- prediction.html
|   |-- dashboard.html
|   |-- about.html
|
|-- static/
|   |-- css/
|   |   |-- style.css
|   |
|   |-- js/
|   |   |-- main.js
|   |   |-- charts.js
|   |
|   |-- images/
|
|-- models/
|   |-- model.pkl
|   |-- scaler.pkl
|   |-- encoder.pkl
|
|-- reports/
|   |-- model_metrics.csv
|   |-- confusion_matrix.png
```

---

## 14. Expected Outcome

The system will predict student stress levels with high accuracy and provide useful recommendations.

The project will satisfy all ML Lab requirements:

- Web-based application
- User input
- Machine learning algorithms
- Model comparison dashboard
- No external API
- Real-world problem
- Custom frontend without Streamlit

---

## 15. Why Flask Instead of Streamlit

Flask is suitable for this project because it allows a proper web application structure with separate HTML, CSS, JavaScript, and backend Python files.

Compared with Streamlit, Flask gives more control over page design, routing, forms, dashboard layout, and project folder organization.

The machine learning part will still run locally in Python, and the frontend will communicate with the Flask backend through form submission or local routes.
