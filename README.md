<div align="center">

<img src="assets/hero.svg" width="100%" alt="Network Security MLOps"/>

<h3>🛡️ Network Security • Machine Learning • MLOps</h3>

<p>
<a href="#-project-overview">Overview</a> •
<a href="#-architecture">Architecture</a> •
<a href="#-ml-pipeline">ML Pipeline</a> •
<a href="#-explainable-ai">XAI</a> •
<a href="#-deployment">Deployment</a> •
<a href="#-setup">Setup</a>
</p>

<p>
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/SHAP-XAI-8B5CF6?style=flat-square"/>
<img src="https://img.shields.io/badge/MLflow-Tracking-0194E2?style=flat-square&logo=mlflow&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-API-009688?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-Container-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS-ECR%20%7C%20S3-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white"/>
</p>

<p><b>Build. Break. Explain. Deploy. Repeat. 🚀</b></p>

</div>

---

# 🌌 Project Overview

**Network Security MLOps** is an end-to-end machine learning project for network security detection.

The project is designed around the complete ML lifecycle rather than stopping at model training:

```text
Data
  ↓
Ingestion
  ↓
Validation
  ↓
Transformation
  ↓
Model Training
  ↓
Evaluation
  ↓
SHAP Explainability
  ↓
Model Artifacts
  ↓
Docker
  ↓
AWS ECR / S3
  ↓
GitHub Actions
  ↓
Self-Hosted Runner
  ↓
FastAPI
  ↓
Prediction
```

The main goal is to build a system that is **reproducible, explainable, containerized, and deployable**.

---

# ✨ Features

| Feature | Implementation |
|---|---|
| 📥 Data Ingestion | Automated dataset ingestion |
| 🔍 Data Validation | Schema validation + drift detection |
| ⚙️ Data Transformation | Preprocessing pipeline |
| 🤖 Model Training | Multiple classification algorithms |
| 🏆 Model Selection | Best model based on F1 score |
| 📊 Model Evaluation | Precision, Recall, F1 |
| 🧠 Explainable AI | SHAP |
| 🧪 Experiment Tracking | MLflow + DagsHub |
| 💾 Model Artifacts | `model.pkl` + `preprocessor.pkl` |
| ☁️ Artifact Storage | AWS S3 |
| 🐳 Containerization | Docker |
| 📦 Image Registry | AWS ECR |
| ⚙️ CI/CD | GitHub Actions |
| 🖥️ Deployment | Self-hosted GitHub runner |
| 🌐 API | FastAPI + Uvicorn |
| 🗄️ Database | MongoDB Atlas |

---

# 🏗️ Architecture

<img src="assets/architecture.svg" width="100%" alt="Network Security MLOps deployment architecture"/>

### Deployment Flow

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ├── Continuous Integration
   │
   ▼
Docker Build
   │
   ▼
AWS ECR
   │
   ▼
Self-Hosted Runner
   │
   ▼
Docker Container
   │
   ▼
FastAPI
   │
   ▼
ML Model
   │
   ▼
Prediction
```

---

# 🧠 ML Pipeline

<img src="assets/ml-pipeline.svg" width="100%" alt="Machine learning pipeline"/>

## 1. Data Ingestion

The pipeline loads the network security dataset and creates the required training and testing artifacts.

## 2. Data Validation

The incoming data is validated against the expected schema.

The pipeline also supports data drift detection to identify changes in the data distribution.

## 3. Data Transformation

Features are processed using the preprocessing pipeline.

The fitted preprocessing object is stored as:

```text
preprocessor.pkl
```

## 4. Model Training

The project evaluates several classification algorithms:

```text
Random Forest
Decision Tree
Gradient Boosting
Logistic Regression
AdaBoost
```

Hyperparameter search is used for selected models.

## 5. Model Evaluation

The models are evaluated using:

```text
Precision
Recall
F1 Score
```

The best model is selected based on the evaluation score.

## 6. Model Packaging

The final deployment object contains:

```text
final_model/
├── model.pkl
└── preprocessor.pkl
```

---

# 🧠 Explainable AI

A security model should answer more than:

> **"Is this traffic malicious?"**

It should also help answer:

> **"Which features influenced the prediction?"**

SHAP is used to inspect model behavior.

```text
Network Data
     ↓
ML Model
     ↓
Prediction
     ↓
SHAP
     ↓
Feature Contributions
```

### SHAP Analysis

The project can analyze:

- Global feature importance
- Feature contribution
- Prediction direction
- Positive and negative feature impact

This improves model transparency and helps understand why a network-security prediction was made.

---

# 📊 Model Evaluation

The main metrics are:

### Precision

Measures the proportion of predicted positive cases that are actually positive.

### Recall

Measures how many actual positive cases are detected.

### F1 Score

Balances Precision and Recall.

The model-selection process is:

```text
Train Models
     ↓
Evaluate Models
     ↓
Compare F1 Scores
     ↓
Select Best Model
     ↓
Save Model
```

---

# 🧪 MLflow + DagsHub

Experiments are tracked using MLflow with DagsHub integration.

Tracked metrics include:

```text
F1 Score
Precision
Recall
```

This allows training runs to be compared and model experiments to be tracked.

---

# 💾 Model Artifacts

The deployment model is stored as:

```text
final_model/
├── model.pkl
└── preprocessor.pkl
```

### `model.pkl`

Contains the trained ML model/prediction object.

### `preprocessor.pkl`

Contains the fitted preprocessing pipeline.

Keeping these artifacts together ensures that prediction uses the same preprocessing logic used during training.

---

# ☁️ AWS

## AWS S3

Model and artifact storage:

```text
S3 Bucket
└── final_model/
    ├── model.pkl
    └── preprocessor.pkl
```

## AWS ECR

Docker images are pushed to Amazon ECR.

```text
Docker Build
     ↓
AWS ECR
     ↓
Docker Pull
     ↓
Deployment
```

---

# 🐳 Docker

Build the image:

```bash
docker build -t networksecurity:test .
```

Run locally:

```bash
docker run --env-file .env -p 8000:8000 networksecurity:test
```

Check the container:

```bash
docker ps
```

Check logs:

```bash
docker logs networksecurity
```

Remove a stopped container:

```bash
docker rm networksecurity
```

---

# ⚙️ CI/CD Pipeline

The project uses GitHub Actions to automate build and deployment.

```text
                    Git Push
                       │
                       ▼
              ┌─────────────────┐
              │ GitHub Actions  │
              └────────┬────────┘
                       │
                       ▼
                 ┌───────────┐
                 │    CI     │
                 │ Test/Build│
                 └─────┬─────┘
                       │
                       ▼
                 ┌───────────┐
                 │  AWS ECR  │
                 │ Push Image│
                 └─────┬─────┘
                       │
                       ▼
             ┌──────────────────┐
             │ Self-Hosted      │
             │ GitHub Runner    │
             └────────┬─────────┘
                      │
                      ▼
                 Pull Image
                      │
                      ▼
              Stop Old Container
                      │
                      ▼
               Start New Container
                      │
                      ▼
                  FastAPI 🚀
```

---

# 🖥️ Self-Hosted Runner

A Windows self-hosted GitHub Actions runner is used for the deployment stage.

The runner executes Docker commands on the deployment machine.

```text
GitHub
   ↓
GitHub Actions
   ↓
Windows Self-Hosted Runner
   ↓
Docker
   ↓
FastAPI
```

This was also used to learn practical deployment issues involving:

- Windows PowerShell
- Docker
- AWS IAM
- ECR authentication
- GitHub Actions
- Environment variables
- Container debugging

---

# 🌐 FastAPI

The ML model is exposed through FastAPI.

## `GET /`

Redirects to Swagger documentation.

```text
/
 ↓
/docs
```

## `GET /train`

Triggers the training pipeline.

The training pipeline is imported inside the endpoint so training dependencies such as DagsHub are not initialized during normal API startup.

## `POST /predict`

Accepts a CSV file and generates predictions.

```text
CSV
 ↓
Load Model
 ↓
Preprocess
 ↓
Predict
 ↓
predicted_column
 ↓
Output CSV
```

Output:

```text
prediction_output/output.csv
```

---

# 🔌 API Usage

Start FastAPI:

```bash
python app.py
```

Open Swagger:

```text
http://localhost:8000/docs
```

### Prediction

```text
POST /predict
```

Workflow:

```text
Try it out
   ↓
Choose CSV
   ↓
Execute
   ↓
Prediction Table
```

---

# 📁 Project Structure

```text
Network-security/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── assets/
│   ├── hero.svg
│   ├── architecture.svg
│   └── ml-pipeline.svg
│
├── Artifacts/
│   └── <timestamp>/
│       ├── data_ingestion/
│       ├── data_validation/
│       ├── data_transformation/
│       └── model_trainer/
│
├── final_model/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── config/
│   ├── constant/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
│
├── prediction_output/
│
├── templates/
│   └── table.html
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── .dockerignore
├── .gitignore
└── README.md
```

---

# 🧰 Tech Stack

## Programming

- Python 3.11

## Machine Learning

- NumPy
- Pandas
- Scikit-learn
- SHAP

## MLOps

- MLflow
- DagsHub
- GitHub Actions

## Cloud

- AWS S3
- AWS ECR
- AWS IAM

## Deployment

- Docker
- FastAPI
- Uvicorn

## Database

- MongoDB Atlas

## Development

- Git
- GitHub
- VS Code

---

# 🚀 Setup

## 1. Clone

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Network-security
```

## 2. Create Virtual Environment

Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```cmd
pip install -r requirements.txt
```

## 4. Environment Variables

Create a `.env` file:

```env
MONGODB_URL_KEY=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_aws_region
```

Do not commit `.env`.

## 5. Run Training

```cmd
python main.py
```

## 6. Start API

```cmd
python app.py
```

Open:

```text
http://localhost:8000/docs
```

---

# 🔐 Security

Never commit secrets to GitHub.

Avoid storing the following directly in source code:

```text
AWS Access Keys
AWS Secret Keys
MongoDB Passwords
DagsHub Tokens
.env files
```

Recommended practices:

- Use GitHub Secrets for CI/CD credentials.
- Use least-privilege IAM policies.
- Rotate credentials if exposed.
- Do not print connection strings.
- Restrict MongoDB access.
- Add API authentication before public deployment.
- Use HTTPS for production.

---

# 🧩 Real-World Debugging

This project involved several real deployment challenges:

```text
AWS IAM Permission Error
        ↓
ECR Authentication
        ↓
Docker Reference Error
        ↓
PowerShell Syntax Issue
        ↓
Self-Hosted Runner Setup
        ↓
Docker Container Crash
        ↓
DagsHub OAuth During Startup
        ↓
Environment Variable Handling
        ↓
Successful Deployment 🚀
```

The biggest lesson:

> **MLOps is not only about making the model work. It's about making the entire system work reliably.**

---

# 📈 Current Status

```text
Data Ingestion             ✅
Data Validation            ✅
Data Transformation        ✅
Model Training             ✅
Model Evaluation           ✅
MLflow Tracking            ✅
DagsHub Integration        ✅
SHAP Explainability        ✅
Model Artifacts            ✅
AWS S3                     ✅
FastAPI                    ✅
Docker                     ✅
AWS ECR                    ✅
GitHub Actions CI          ✅
GitHub Actions CD          ✅
Self-Hosted Runner         ✅
Automated Deployment       ✅
```

---

# 🗺️ Roadmap

```text
              CURRENT
                 │
                 ▼
        ┌─────────────────┐
        │   ML Pipeline   │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │    SHAP XAI     │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ Docker + ECR    │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ GitHub CI / CD  │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │   Deployment    │
        └────────┬────────┘
                 │
              NEXT 🚀
                 │
                 ▼
        AWS EC2 / ECS
                 │
                 ▼
        API Authentication
                 │
                 ▼
        Model Monitoring
                 │
                 ▼
        Automated Retraining
                 │
                 ▼
        Production
        Observability
```

---

# 🎯 Learning Goal

This project is part of a **90 Days Learn in Public** journey.

The objective is to understand:

```text
Machine Learning
       +
Explainable AI
       +
MLOps
       +
Cloud
       +
DevOps
```

The focus is on the complete lifecycle:

> **Build → Evaluate → Explain → Package → Deploy → Monitor**

---

# ⭐ Project Philosophy

```text
Train it.
Break it.
Debug it.
Explain it.
Containerize it.
Deploy it.
Automate it.
Repeat. 🚀
```

---

<div align="center">

### 🛡️ Network Security MLOps

**Machine Learning × Explainable AI × MLOps × Cloud**

<br/>

⭐ If you find this project useful, consider giving the repository a star.

</div>
