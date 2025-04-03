# Credit Card Fraud Detection

![image](https://github.com/user-attachments/assets/41305954-5885-4a2c-a53a-a8361d541448)

## 📌 Project Overview
This project is a **Credit Card Fraud Detection System** built using **Flask, Machine Learning, and MongoDB**. It predicts whether a transaction is fraudulent or safe based on user input. The model is trained on transaction data and deployed as a web application.

## 🚀 Features
- **Web Interface**: Users can enter transaction details via a user-friendly UI.
- **Machine Learning Model**: Predicts fraud based on transaction data.
- **Data Preprocessing**: Uses `LabelEncoder` for categorical features and `StandardScaler` for normalization.
- **MongoDB Integration**: Stores transaction data for future analysis.

## 🛠️ Technologies Used
- **Python** (Flask, NumPy, Pandas, Scikit-learn)
- **Machine Learning** (Logistic Regression, Decision Trees, etc.)
- **MongoDB** (Database for storing transactions)
- **HTML, CSS** (Frontend UI)
- **Joblib** (Model saving/loading)

## 📁 Project Structure
```
credit_card_fraud_detection/
│-- static/
│   ├── styles.css  # Styling for the UI
│-- templates/
│   ├── index.html  # Frontend UI for input and output
│-- Credit_Card_fraud_model.pkl  # Trained ML model
│-- Label_encoders.pkl  # Encoders for categorical features
│-- scaler_transform.pkl  # Scaler for feature normalization
│-- main.py  # Flask application (API + Prediction + Database Integration)
│-- README.md  # Project documentation
```

## 🔧 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask application:**
   ```bash
   python main.py
   ```
5. **Access the web app:** Open `http://127.0.0.1:5000/` in your browser.

## 📊 How It Works
1. User inputs transaction details in the form.
2. The data is preprocessed (encoding + scaling).
3. The trained ML model predicts whether the transaction is fraudulent or safe.
4. The result is displayed on the UI.
5. The transaction data is stored in MongoDB.

## 🛡️ MongoDB Setup
1. **Install MongoDB and create an Atlas cluster.**
2. **Replace `MONGO_URI` in `main.py` with your connection string:**
   ```python
   MONGO_URI = "mongodb+srv://<username>:<password>@yourcluster.mongodb.net/?retryWrites=true&w=majority"
   ```
3. **Ensure `certifi` is installed for SSL connection:**
   ```bash
   pip install certifi
   ```

## 📷 Screenshots
| Home Page | Prediction Result |
|-----------|------------------|
| ![Screenshot 2025-04-03 215224](https://github.com/user-attachments/assets/b2aa36b9-efed-4ea3-a0c9-ee03ece5f05a) | Predict |
| ![Screenshot 2025-04-03 215318](https://github.com/user-attachments/assets/58d6b58d-352a-4d0e-bb54-7fec051452a1) | Fraud |
| ![Screenshot 2025-04-03 215621](https://github.com/user-attachments/assets/011a0962-8fa9-492f-ae65-31381279f692) | Safe |


## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

## 📜 License
This project is open-source and available under the **MIT License**.

---
🔗 **Connect with me:** [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

