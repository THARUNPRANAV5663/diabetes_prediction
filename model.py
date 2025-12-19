import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model():
    # Load dataset
    data = pd.read_csv("https://raw.githubusercontent.com/raveendran2862/dataset/refs/heads/main/diabetes.csv")

    # Features and target
    X = data[[
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
    ]]
    y = data["Outcome"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Print accuracy for quick check
    print("Training accuracy:", model.score(X_train, y_train))
    print("Test accuracy:", model.score(X_test, y_test))

    # Save model and scaler in 'models/' folder
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    print("Model and scaler saved in 'models/' folder.")

if __name__ == "__main__":
    train_and_save_model()