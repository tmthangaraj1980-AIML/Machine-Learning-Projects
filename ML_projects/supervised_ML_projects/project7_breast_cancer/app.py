from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("C_df.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = []

        for i in range(1, 16):   # 15 inputs
            features.append(float(request.form[f"f{i}"]))

        prediction = model.predict([features])[0]

        if prediction == 0:
            result = "🔴 Malignant (Cancer)"
        else:
            result = "🟢 Benign (Non-Cancer)"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)