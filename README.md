<<<<<<< HEAD
# Credit-Risk-Prediction-ML-XGBoost- 
---
**Link:** https://anindasau-credit-risk-prediction-ml-xgboost--app-tqisxh.streamlit.app/
=======
# 🏦 Banker's AI: Credit Risk Prediction System

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=Streamlit\&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-232F3E?style=for-the-badge\&logo=XGBoost\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)

An end-to-end **Machine Learning solution** designed to predict the likelihood of loan default. This system leverages a high-performance **XGBoost** model to analyze applicant profiles and provide instant risk assessments with high precision.

---

## 📖 Table of Contents

* [🎯 Project Overview](#-project-overview)
* [📂 Project Structure](#-project-structure)
* [🛠️ Installation & Setup](#️-installation--setup)
* [📊 Model & Data](#-model--data)
* [🛡️ Usage Instructions](#️-usage-instructions)
* [🤝 Contributing](#-contributing)

---

## 🎯 Project Overview

Credit risk assessment is a critical process for financial institutions to minimize losses. This project automates that assessment by using a **Gradient Boosting pipeline** to classify applicants into:

* **Low Risk (Approved)**
* **High Risk (Rejected)**

### Key Features

* **Interactive UI:** Dual-column input form for applicant data.
* **Risk Probability Scoring:** Returns a percentage probability of default.
* **Smart Preprocessing:** Automatic categorical encoding and numerical scaling.
* **Real-time Prediction:** Optimized XGBoost model for near-instant results.

---

## 📂 Project Structure

```text
Credit_risk_analysis/
├── Creditvenv/           # Virtual Environment
├── models/               # Serialized ML Artifacts
│   ├── xgb_model.pkl     # Trained XGBoost Classifier
│   ├── scaler.pkl        # StandardScaler for numerical features
│   ├── encoder.pkl       # OrdinalEncoder for categorical data
│   └── features.pkl      # List of 11 feature names in order
├── app.py                # Streamlit Web Application
├── requirements.txt      # Project Dependencies
└── README.md             # Project Documentation
```

---

## 🛠️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/credit-risk-prediction.git
cd credit-risk-prediction
```

### 2. Create & Activate Virtual Environment

```bash
# Create the environment
python -m venv Creditvenv

# Activate on Windows
.\Creditvenv\Scripts\activate

# Activate on Mac/Linux
source Creditvenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📊 Model & Data

The model analyzes **11 features** to predict credit risk:

* **Demographics:** Age, Income, Home Ownership
* **Employment:** Years of Employment
* **Loan Details:** Amount, Intent, Interest Rate, Grade
* **History:** Credit history length, Previous default records

**Performance Metrics:** Optimized for **high AUC-ROC and Recall** to ensure "High Risk" individuals are correctly flagged, protecting lender capital.

---

## 🛡️ Usage Instructions

1. Open the app in your browser (default: [http://localhost:8501](http://localhost:8501))
2. Enter Applicant Information in the left and right input columns
3. Click **"Analyze Credit Risk"**
4. Review Prediction Results:

   * ✅ **Low Risk:** High probability of repayment
   * 🚩 **High Risk:** High probability of default

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a **Pull Request** or raise **Issues** for suggestions and improvements.
>>>>>>> 60d2b1b (Initial commit: Add README for Banker's AI project)
