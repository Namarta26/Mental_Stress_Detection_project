from pathlib import Path
from time import perf_counter

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from ml_utils import FEATURE_COLUMNS


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATHS = [
    BASE_DIR / "stress_dataset.csv",
    BASE_DIR / "Stress_ dataset.csv",
    BASE_DIR / "Stress_ Dataset.csv",
]
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"


def normalize_columns(df):
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def parse_sleep_hours(value):
    text = str(value).lower().strip()
    numbers = []

    for part in text.replace("-", " ").split():
        try:
            numbers.append(float(part))
        except ValueError:
            continue

    if not numbers:
        return 6.0

    return sum(numbers) / len(numbers)


def add_project_features(df):
    df = df.copy()

    if "work/study_hours" in df.columns and "study_hours" not in df.columns:
        df["study_hours"] = df["work/study_hours"]

    if "sleep_duration" in df.columns and "sleep_hours" not in df.columns:
        df["sleep_hours"] = df["sleep_duration"].apply(parse_sleep_hours)

    defaults = {
        "exercise_hours": 1.0,
        "screen_time": 6.0,
        "social_media_usage": 2.0,
        "mood_score": 5.0,
        "anxiety_level": 5.0,
        "sleep_quality": 5.0,
    }

    for column, value in defaults.items():
        if column not in df.columns:
            df[column] = value

    if "stress_level" not in df.columns and "depression" in df.columns:
        risk = (
            df["academic_pressure"].fillna(0)
            + df["financial_stress"].fillna(0)
            + (10 - df["study_satisfaction"].fillna(5))
            + (8 - df["sleep_hours"].fillna(6))
            + (df["depression"].fillna(0) * 5)
        )

        df["stress_level"] = pd.cut(
            risk,
            bins=[-100, 8, 15, 100],
            labels=["Low", "Medium", "High"],
        ).astype(str)

    return df


def prepare_dataset():
    dataset_path = next((path for path in DATASET_PATHS if path.exists()), None)

    if dataset_path is None:
        raise FileNotFoundError(
            "Place your Kaggle dataset CSV at stress_dataset.csv, then run train_model.py again."
        )

    df = normalize_columns(pd.read_csv(dataset_path))
    df = add_project_features(df)
    df = df.dropna()

    target_candidates = ["stress_level", "stress", "stress_category"]
    target_column = next((col for col in target_candidates if col in df.columns), None)

    if target_column is None:
        raise ValueError("Dataset must contain a target column named stress_level.")

    missing_features = [col for col in FEATURE_COLUMNS if col not in df.columns]
    if missing_features:
        raise ValueError(f"Missing required feature columns: {missing_features}")

    for column in df.select_dtypes(include=["object"]).columns:
        if column == target_column:
            continue

        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column].astype(str))

    x = df[FEATURE_COLUMNS]
    y = df[target_column]
    return train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)


def calculate_roc_auc(model, x_test_scaled, y_test):
    if not hasattr(model, "predict_proba"):
        return "N/A"

    try:
        probabilities = model.predict_proba(x_test_scaled)
        return round(roc_auc_score(y_test, probabilities, multi_class="ovr", average="weighted"), 4)
    except ValueError:
        return "N/A"


def main():
    MODELS_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)

    x_train, x_test, y_train, y_test = prepare_dataset()

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    algorithms = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=150, random_state=42),
        "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
        "Support Vector Machine": SVC(probability=True, random_state=42),
    }

    results = []
    best_name = None
    best_model = None
    best_accuracy = -1
    best_predictions = None

    for name, model in algorithms.items():
        started_at = perf_counter()
        model.fit(x_train_scaled, y_train)
        training_time = perf_counter() - started_at

        predictions = model.predict(x_test_scaled)
        accuracy = accuracy_score(y_test, predictions)

        results.append(
            {
                "algorithm": name,
                "accuracy": round(accuracy, 4),
                "precision": round(precision_score(y_test, predictions, average="weighted", zero_division=0), 4),
                "recall": round(recall_score(y_test, predictions, average="weighted", zero_division=0), 4),
                "f1_score": round(f1_score(y_test, predictions, average="weighted", zero_division=0), 4),
                "roc_auc": calculate_roc_auc(model, x_test_scaled, y_test),
                "training_time": round(training_time, 4),
            }
        )

        if accuracy > best_accuracy:
            best_name = name
            best_model = model
            best_accuracy = accuracy
            best_predictions = predictions

    pd.DataFrame(results).to_csv(REPORTS_DIR / "model_metrics.csv", index=False)

    labels = ["Low", "Medium", "High"]
    matrix = confusion_matrix(y_test, best_predictions, labels=labels)
    pd.DataFrame(matrix, index=labels, columns=labels).to_csv(REPORTS_DIR / "confusion_matrix.csv")

    joblib.dump(best_model, MODELS_DIR / "model.pkl")
    joblib.dump(scaler, MODELS_DIR / "scaler.pkl")

    print(f"Best model: {best_name} with accuracy {best_accuracy:.4f}")


if __name__ == "__main__":
    main()
