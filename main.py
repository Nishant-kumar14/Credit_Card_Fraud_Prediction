from flask import Flask, render_template, request
import joblib
import numpy as np
import pymongo
from datetime import datetime

app = Flask(__name__)

# Load trained model, encoders, and scaler
model = joblib.load("Credit_Card_fraud_model.pkl")
label_encoders = joblib.load("Label_encoders.pkl")
scaler = joblib.load("scaler_transform.pkl")

# Connect to MongoDB using your connection URL
MONGO_URI = "mongodb+srv://nishant23102003:Nishant12@nishant777.twv6d.mongodb.net/?retryWrites=true&w=majority&appName=Nishant777&tls=true&tlsAllowInvalidCertificates=true"  # Replace this with your MongoDB URL
client = pymongo.MongoClient(MONGO_URI)
db = client["Credit_Card"]  # Database name
collection = db["Prediction"]  # Collection name

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
                "timestamp": datetime.now(),
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
                "prediction": prediction,
                "encoded_values": {
                    "merchant_enc": int(merchant_enc),
                    "category_enc": int(category_enc),
                    "gender_enc": int(gender_enc),
                    "state_enc": int(state_enc),
                    "job_enc": int(job_enc),
                    "day_of_week_enc": int(day_of_week_enc)
                }
            }

            collection.insert_one(transaction_record)  # Insert into MongoDB
        
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
