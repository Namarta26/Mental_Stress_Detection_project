from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

from ml_utils import FEATURE_COLUMNS, get_recommendations, risk_score, stress_level_from_score


BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"
METRICS_PATH = REPORTS_DIR / "model_metrics.csv"

app = Flask(__name__)


def parse_form_data(form):
    values = {
        "age": float(form.get("age", 0)),
        "gender": 2,
        "cgpa": float(form.get("cgpa", 0)),
        "study_hours": float(form.get("study_hours", 0)),
        "sleep_hours": float(form.get("sleep_hours", 0)),
        "academic_pressure": float(form.get("academic_pressure", 0)),
        "financial_stress": float(form.get("financial_stress", 0)),
        "study_satisfaction": 5.0,
        "exercise_hours": 1.0,
        "screen_time": 6.0,
        "social_media_usage": 2.0,
        "mood_score": 5.0,
        "anxiety_level": float(form.get("academic_pressure", 5)),
        "sleep_quality": min(10.0, max(1.0, float(form.get("sleep_hours", 6)))),
    }

    return pd.DataFrame([values], columns=FEATURE_COLUMNS)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None

    if request.method == "POST":
        input_df = parse_form_data(request.form)
        score = risk_score(input_df.iloc[0], "Low")
        predicted_stress = stress_level_from_score(score)
        result = {
            "stress_level": predicted_stress,
            "risk_score": score,
            "recommendations": get_recommendations(predicted_stress),
        }

    return render_template("prediction.html", result=result)


@app.route("/dashboard")
def dashboard():
    metrics = []
    confusion_matrix = []
    confusion_labels = []

    if METRICS_PATH.exists():
        metrics = pd.read_csv(METRICS_PATH).to_dict(orient="records")

    confusion_path = REPORTS_DIR / "confusion_matrix.csv"
    if confusion_path.exists():
        confusion_df = pd.read_csv(confusion_path, index_col=0)
        confusion_labels = list(confusion_df.columns)
        confusion_matrix = confusion_df.values.tolist()

    return render_template(
        "dashboard.html",
        metrics=metrics,
        confusion_labels=confusion_labels,
        confusion_matrix=confusion_matrix,
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
