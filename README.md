# 🔐 Phishing URL Detection System

An end-to-end Machine Learning pipeline that detects phishing URLs using network-based and URL-based features.
The system includes automated data ingestion, validation, model training, experiment tracking, and REST API deployment.

---

## 🚀 Tech Stack

* Python
* FastAPI
* MongoDB
* Scikit-learn
* MLflow
* Pandas & NumPy

---

## 📌 Project Overview

Phishing attacks are one of the most common cybersecurity threats. This project builds a production-ready ML pipeline to classify URLs as **phishing or legitimate**.

The system includes:

* Automated ETL pipeline
* Data validation & drift detection
* Model training & evaluation
* Experiment tracking
* REST API for predictions

---

## 🏗 Architecture

```
Data Source
    ↓
MongoDB Ingestion
    ↓
Data Validation (Schema + Drift Detection)
    ↓
Feature Engineering
    ↓
Model Training (Multiple ML models)
    ↓
MLflow Experiment Tracking
    ↓
FastAPI Deployment
```

---

## 🔍 Key Features

### ✅ 1. ETL Pipeline

* Automated data ingestion into MongoDB
* Train-test splitting
* Artifact management for reproducibility

### ✅ 2. Data Validation

* Schema validation
* Missing value checks
* Data drift detection using **Kolmogorov–Smirnov (KS) statistical test**

### ✅ 3. Model Training

* Multiple classification models trained using Scikit-learn
* Performance evaluation using standard metrics (Accuracy, Precision, Recall, F1-score)

### ✅ 4. Experiment Tracking

* Logged experiments, parameters, and metrics using MLflow
* Versioned model artifacts for reproducibility

### ✅ 5. REST API Deployment

* FastAPI-based prediction endpoint
* JSON request-response structure
* Production-ready API design

---

## 🛠 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/siddhant-vars/networksecurity.git
cd networksecurity
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file:

```
MONGODB_URI=your_mongodb_connection_string
```

---

### 5️⃣ Run Training Pipeline

```bash
python main.py
```

---

### 6️⃣ Start FastAPI Server

```bash
uvicorn app:app --reload
```

API available at:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Model Workflow

* Feature extraction from URLs
* Data preprocessing
* Model comparison
* Best model selection
* Model serialization
* Deployment via API endpoint

---


## 🧠 Key Learnings

* Building modular ML pipelines
* Data validation & drift detection
* Statistical testing (KS test)
* Experiment tracking with MLflow
* Deploying ML models using FastAPI
* Designing production-ready ML systems

---

## 📌 Future Improvements

* Docker containerization
* CI/CD pipeline integration
* Real-time monitoring & logging
* Cloud deployment
* Model retraining automation

---

## 👨‍💻 Author

**Siddhant Varshney**
Machine Learning & Backend Developer

GitHub:
[https://github.com/siddhant-vars](https://github.com/siddhant-vars)

---


