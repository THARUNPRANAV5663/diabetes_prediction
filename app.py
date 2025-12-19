from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        pregnancies = int(request.form["pregnancies"])
        glucose = float(request.form["glucose"])
        bloodpressure = float(request.form["bloodpressure"])
        skin = float(request.form["skin"])
        insulin = float(request.form["insulin"])
        bmi = float(request.form["bmi"])
        pedigree = float(request.form["pedigree"])
        age = int(request.form["age"])

        input_data = np.array([[pregnancies, glucose, bloodpressure,
                                skin, insulin, bmi, pedigree, age]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        result = "You have diabetes ⚠️" if prediction == 1 else "You do not have diabetes 👍"
        color = "red" if prediction == 1 else "green"

        return render_template("index.html", prediction_text=result, color=color)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}", color="orange")

if __name__ == "__main__":
    app.run(debug=True)