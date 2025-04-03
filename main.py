from flask import Flask, render_template, request
import joblib
import numpy as np
from pymongo import MongoClient
import certifi

app = Flask(__name__)

# Load trained model, encoders, and scaler
model = joblib.load("Credit_Card_fraud_model.pkl")
label_encoders = joblib.load("Label_encoders.pkl")
scaler = joblib.load("scaler_transform.pkl")

# Connect to MongoDB
MONGO_URI = "mongodb+srv://user123:<Nishant12>@nishant1.lgiw2.mongodb.net/?retryWrites=true&w=majority&appName=Nishant1"
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client["credit_fraud"]  # Database name
collection = db["fraud_transactions"]  # Collection name

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            # Get user inputs from form
            merchant = request.form["merchant"]
            category = request.form["category"]
            amt = float(request.form["amt"])
            gender = request.form["gender"]
            state = request.form["state"]
            job = request.form["job"]
            transaction_hour = int(request.form["transaction_hour"])
            day_of_week = request.form["day_of_week"]
            transaction_month = int(request.form["transaction_month"])
            age = int(request.form["age"])

            # Encode categorical variables
            merchant_enc = label_encoders["merchant"].transform([merchant])[0]
            category_enc = label_encoders["category"].transform([category])[0]
            gender_enc = label_encoders["gender"].transform([gender])[0]
            state_enc = label_encoders["state"].transform([state])[0]
            job_enc = label_encoders["job"].transform([job])[0]
            day_of_week_enc = label_encoders["day_of_week"].transform([day_of_week])[0]

            # Prepare input data
            input_data = np.array([[merchant_enc, category_enc, amt, gender_enc, state_enc, job_enc, 
                                    transaction_hour, day_of_week_enc, transaction_month, age]])

            # Normalize numeric data
            input_data = scaler.transform(input_data)

            # Make prediction
            result = model.predict(input_data)
            prediction = "🚨 FRAUD ALERT!" if result[0] == 1 else "✅ Safe Transaction"

            # Store transaction details in MongoDB
            transaction_record = {
                "merchant": merchant,
                "category": category,
                "amount": amt,
                "gender": gender,
                "state": state,
                "job": job,
                "transaction_hour": transaction_hour,
                "day_of_week": day_of_week,
                "transaction_month": transaction_month,
                "age": age,
                "prediction": prediction
            }
            collection.insert_one(transaction_record)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
