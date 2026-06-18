import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "age",
    "gender",
    "cgpa",
    "study_hours",
    "sleep_hours",
    "academic_pressure",
    "financial_stress",
    "study_satisfaction",
    "exercise_hours",
    "screen_time",
    "social_media_usage",
    "mood_score",
    "anxiety_level",
    "sleep_quality",
]


def build_demo_model():
    rows = [
        [19, 0, 8.8, 4, 8, 2, 1, 8, 1, 4, 1, 8, 2, 8],
        [21, 1, 7.2, 7, 6, 5, 4, 5, 0.5, 7, 3, 5, 5, 5],
        [23, 0, 6.1, 9, 4, 9, 8, 2, 0, 10, 5, 2, 9, 2],
        [20, 2, 8.0, 5, 7, 3, 2, 7, 1.5, 5, 2, 7, 3, 7],
        [22, 1, 6.8, 8, 5, 7, 6, 4, 0.3, 8, 4, 4, 7, 4],
        [18, 0, 9.1, 3, 8, 1, 1, 9, 2, 3, 1, 9, 1, 9],
    ]
    labels = ["Low", "Medium", "High", "Low", "High", "Low"]

    x = pd.DataFrame(rows, columns=FEATURE_COLUMNS)
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(x_scaled, labels)

    return model, scaler


def risk_score(input_row, stress_level):
    score = 0

    score += input_row["academic_pressure"] * 4
    score += input_row["financial_stress"] * 3
    score += max(0, 6 - input_row["sleep_hours"]) * 6
    score += max(0, input_row["study_hours"] - 8) * 3
    score += max(0, 7 - input_row["cgpa"]) * 4
    score -= max(0, input_row["sleep_hours"] - 7) * 2

    if stress_level == "Medium":
        score = max(score, 45)
    elif stress_level == "High":
        score = max(score, 70)

    return int(np.clip(score, 0, 100))


def stress_level_from_score(score):
    if score < 35:
        return "Low"

    if score < 70:
        return "Medium"

    return "High"


def get_recommendations(stress_level):
    recommendations = {
        "Low": [
            "Continue your healthy lifestyle.",
            "Maintain a consistent sleep schedule.",
            "Keep balancing study, exercise, and rest.",
        ],
        "Medium": [
            "Improve your sleep schedule.",
            "Reduce screen time and social media usage.",
            "Take short study breaks and include light exercise.",
        ],
        "High": [
            "Consider speaking with a counselor or trusted mentor.",
            "Improve work-life balance and reduce overload.",
            "Increase physical activity and prioritize sleep.",
        ],
    }

    return recommendations.get(stress_level, recommendations["Medium"])
