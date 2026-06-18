# Smart Mental Stress Detection and Risk Prediction System

This is a Flask-based web application for predicting student stress levels without using Streamlit.
The frontend uses local HTML, CSS, and JavaScript files.

## Project Report

A detailed project report is available in [PROJECT_REPORT.md](PROJECT_REPORT.md).

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Machine Learning: Scikit-Learn
- Data Processing: Pandas, NumPy
- Visualization: local CSS charts, Matplotlib, Seaborn
- Model Saving: Joblib

## Project Structure

```text
MentalStressDetection/
|
|-- app.py
|-- train_model.py
|-- ml_utils.py
|-- stress_dataset.csv
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
|   |-- js/
|       |-- main.js
|       |-- main.js
|
|-- models/
|   |-- model.pkl
|   |-- scaler.pkl
|
|-- reports/
|   |-- model_metrics.csv
```

## Setup Steps

1. Create a virtual environment.

```bash
python -m venv venv
```

2. Activate the virtual environment.

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

Command Prompt:

```bash
venv\Scripts\activate
```

3. Install dependencies.

```bash
python -m pip install -r requirements.txt
```

4. Run the web app.

```bash
.\venv\Scripts\python.exe app.py
```

5. Open the app in your browser.

```text
http://127.0.0.1:5000
```

## Dataset Setup

Download the Student Depression Dataset from Kaggle:

```text
https://www.kaggle.com/datasets/hopesb/student-depression-dataset
```

Place the CSV file in the project root and rename it:

```text
stress_dataset.csv
```

The training script expects these columns:

- age
- gender
- cgpa
- study_hours
- sleep_hours
- academic_pressure
- financial_stress
- study_satisfaction
- exercise_hours
- screen_time
- social_media_usage
- mood_score
- anxiety_level
- sleep_quality
- stress_level

If your downloaded CSV uses different column names, rename them in the CSV or update `FEATURE_COLUMNS` in `ml_utils.py`.

## Train Machine Learning Models

After adding `stress_dataset.csv`, run:

```bash
.\venv\Scripts\python.exe train_model.py
```

This will:

- Preprocess the dataset
- Train Logistic Regression, Decision Tree, Random Forest, KNN, and SVM
- Save the best model to `models/model.pkl`
- Save the scaler to `models/scaler.pkl`
- Save comparison metrics to `reports/model_metrics.csv`

## Web Pages

- Home: Project introduction, objective, and dataset summary
- Prediction: Student input form, stress level, risk score, and recommendations
- Dashboard: Model comparison table and charts
- About: Project details and algorithms used

## Important Note

The app includes a small demo model so the prediction page can run before the real dataset is added. For final submission, add the real Kaggle dataset and run `python train_model.py`.

## Common Error Fix

If the traceback shows `Python314`, you are using the wrong Python interpreter. Use the project virtual environment instead:

```powershell
.\venv\Scripts\python.exe app.py
```

You can also run `run_app.bat` to start the web app with the correct interpreter automatically.
