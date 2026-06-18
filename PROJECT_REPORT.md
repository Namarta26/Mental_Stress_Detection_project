# Smart Mental Stress Detection and Risk Prediction System

## Project Report

## 1. Introduction

Mental stress among students is a common problem caused by academic pressure, lack of sleep, financial concerns, long study hours, and lifestyle imbalance. If stress is not identified early, it can affect academic performance, physical health, emotional stability, and daily productivity.

This project presents a Flask-based web application that predicts a student's stress level and displays a risk score with practical recommendations. The system also includes a machine learning training workflow that compares multiple algorithms and stores model performance results for dashboard visualization.

## 2. Project Objective

The main objective of this project is to develop a smart mental stress detection system that can:

- Collect important student-related information through a web form.
- Analyze academic, lifestyle, and wellness factors.
- Predict stress level as Low, Medium, or High.
- Generate a stress risk score.
- Provide useful recommendations based on the predicted stress level.
- Compare machine learning models using standard evaluation metrics.
- Display model performance through a web dashboard.

## 3. Problem Statement

Students often face stress due to academic workload, pressure to perform, poor sleep habits, financial stress, excessive screen time, and lack of physical activity. Many students do not recognize their stress level until it becomes serious.

The problem addressed by this project is the need for a simple, local, and user-friendly web system that can estimate student stress level early and present the result in an understandable way.

## 4. Scope of the Project

This project focuses on student mental stress prediction using a Flask web application and machine learning concepts. The current system includes:

- A home page introducing the project.
- A prediction page for user input and stress result display.
- A dashboard page for model comparison and confusion matrix display.
- A training script for preprocessing the dataset, training models, and saving reports.
- Local model and report storage using `joblib` and CSV files.

The system is intended for academic and demonstration purposes. It should not be used as a medical diagnosis tool.

## 5. Technology Stack

| Layer | Technology Used |
|---|---|
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Backend | Python Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Storage | Joblib |
| Reports | CSV files |
| Development Environment | Python virtual environment |

## 6. Dataset Description

The project is based on a student mental health and depression-related dataset adapted for stress prediction.

| Item | Description |
|---|---|
| Dataset | Student Depression Dataset |
| Source | Kaggle |
| Target Variable | `stress_level` |
| Target Classes | Low, Medium, High |

The training script checks for the dataset using these possible file names:

- `stress_dataset.csv`
- `Stress_ dataset.csv`
- `Stress_ Dataset.csv`

## 7. Input Features

The system uses the following feature columns:

| Feature | Description |
|---|---|
| `age` | Age of the student |
| `gender` | Encoded gender value |
| `cgpa` | Academic CGPA |
| `study_hours` | Daily study hours |
| `sleep_hours` | Daily sleep hours |
| `academic_pressure` | Academic pressure score |
| `financial_stress` | Financial stress score |
| `study_satisfaction` | Satisfaction with study |
| `exercise_hours` | Daily exercise duration |
| `screen_time` | Daily screen time |
| `social_media_usage` | Social media usage level |
| `mood_score` | Mood score |
| `anxiety_level` | Anxiety level |
| `sleep_quality` | Quality of sleep |

The current prediction form accepts the most important fields from the user and assigns default values for additional features required by the model structure.

## 8. System Architecture

The project follows a simple web-based architecture:

1. The user opens the Flask web application.
2. The user enters student details on the prediction page.
3. The backend receives the form data.
4. The input values are converted into the required feature format.
5. The system calculates the stress risk score.
6. The predicted stress level and recommendations are displayed to the user.
7. The dashboard reads saved CSV report files and displays model performance.

## 9. Module Description

### 9.1 Home Module

The home page introduces the project, explains the purpose of stress prediction, and provides navigation to the prediction and dashboard pages.

### 9.2 Prediction Module

The prediction page collects user inputs such as age, CGPA, study hours, sleep hours, academic pressure, and financial stress. After form submission, the system calculates a risk score and classifies the student into one of the stress categories.

### 9.3 Recommendation Module

The recommendation module provides suggestions according to the predicted stress level.

| Stress Level | Recommendation Type |
|---|---|
| Low | Maintain healthy lifestyle and balanced routine |
| Medium | Improve sleep, reduce screen time, and include breaks |
| High | Seek support, reduce overload, and prioritize health |

### 9.4 Dashboard Module

The dashboard displays:

- Model comparison table
- Accuracy
- Precision
- Recall
- F1 score
- ROC-AUC score
- Training time
- Confusion matrix

### 9.5 Training Module

The `train_model.py` script performs dataset loading, preprocessing, model training, evaluation, and report generation.

## 10. Data Preprocessing

The preprocessing workflow includes:

- Normalizing column names.
- Handling alternative dataset column names.
- Creating required project features when missing.
- Dropping missing values.
- Encoding categorical columns using label encoding.
- Splitting the dataset into training and testing sets.
- Applying feature scaling using `StandardScaler`.

The dataset is split using an 80:20 train-test ratio with stratification.

## 11. Machine Learning Algorithms

The following algorithms are compared in the training script:

| Algorithm | Purpose |
|---|---|
| Logistic Regression | Baseline linear classification model |
| Decision Tree | Rule-based classification model |
| Random Forest | Ensemble model using multiple decision trees |
| K-Nearest Neighbors | Distance-based classification model |
| Support Vector Machine | Margin-based classification model |

## 12. Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 score
- ROC-AUC
- Training time
- Confusion matrix

These metrics help compare both prediction quality and training efficiency.

## 13. Experimental Results

The following results are stored in `reports/model_metrics.csv`:

| Algorithm | Accuracy | Precision | Recall | F1 Score | ROC-AUC | Training Time |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8620 | 0.8604 | 0.8620 | 0.8607 | 0.9393 | 0.4066 |
| Decision Tree | 0.8267 | 0.8257 | 0.8267 | 0.8261 | 0.8045 | 0.0883 |
| Random Forest | 0.8606 | 0.8597 | 0.8606 | 0.8600 | 0.9392 | 2.6149 |
| K-Nearest Neighbors | 0.8444 | 0.8423 | 0.8444 | 0.8429 | 0.9104 | 0.1970 |
| Support Vector Machine | 0.8738 | 0.8734 | 0.8738 | 0.8736 | 0.9450 | 71.2921 |

Based on the saved evaluation results, Support Vector Machine achieved the highest accuracy of 87.38% and the highest ROC-AUC score of 0.9450. However, it also required the longest training time.

## 14. Confusion Matrix

The confusion matrix saved in `reports/confusion_matrix.csv` is:

| Actual \ Predicted | Low | Medium | High |
|---|---:|---:|---:|
| Low | 38 | 9 | 0 |
| Medium | 6 | 1458 | 358 |
| High | 0 | 331 | 3380 |

The model performs strongly for the High and Medium classes. Some confusion exists between Medium and High stress levels, which is expected because these categories may share similar symptoms and feature values.

## 15. Result Interpretation

The project successfully predicts stress category and presents the result in a user-friendly format. The dashboard shows that all evaluated models perform reasonably well, with SVM giving the best overall result in the current experiment.

The risk score helps users understand the severity of their stress condition in percentage form. The recommendation section makes the output more useful by suggesting practical lifestyle improvements.

## 16. Project Folder Structure

```text
Mental_Stress_Detection_project/
|
|-- app.py
|-- train_model.py
|-- ml_utils.py
|-- requirements.txt
|-- README.md
|-- PROJECT_REPORT.md
|-- Stress_ dataset.csv
|
|-- models/
|   |-- model.pkl
|   |-- scaler.pkl
|
|-- reports/
|   |-- model_metrics.csv
|   |-- confusion_matrix.csv
|
|-- static/
|   |-- css/
|   |   |-- style.css
|   |-- js/
|       |-- main.js
|
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- prediction.html
|   |-- dashboard.html
```

## 17. How to Run the Project

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000
```

Train the machine learning models:

```bash
python train_model.py
```

## 18. Advantages

- Simple and user-friendly web interface.
- Runs locally without external APIs.
- Compares multiple machine learning algorithms.
- Provides stress level, risk score, and recommendations.
- Includes dashboard-based performance visualization.
- Uses common and easy-to-install Python libraries.

## 19. Limitations

- The application is for academic use and does not provide medical diagnosis.
- The prediction form currently uses a reduced set of user inputs and default values for some model features.
- Model performance depends on dataset quality and feature availability.
- More real-world validation is required before practical deployment.

## 20. Future Enhancements

- Add all feature inputs to the prediction form.
- Load and use the saved trained model directly during prediction.
- Add user authentication and prediction history.
- Add downloadable PDF reports for individual predictions.
- Improve visual charts using Chart.js or another charting library.
- Deploy the application on a cloud platform.
- Add more mental wellness indicators for better prediction accuracy.

## 21. Conclusion

The Smart Mental Stress Detection and Risk Prediction System is a useful machine learning-based web application for estimating student stress levels. It combines Flask, frontend web technologies, and scikit-learn to provide prediction, recommendations, and model performance analysis.

The project successfully demonstrates the complete flow of data collection, preprocessing, model training, evaluation, dashboard reporting, and user-facing prediction. With further improvements, it can become a stronger academic wellness support tool.
