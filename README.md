::: {align="center"}
`<img src="assets/hero.svg" alt="Network Security MLOps" width="100%"/>`{=html}

### 🛡️ Network Security • Machine Learning • MLOps

```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>`{=html}
`<img src="https://img.shields.io/badge/FastAPI-0.1%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>`{=html}
`<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>`{=html}
`<img src="https://img.shields.io/badge/AWS-ECR%20%7C%20S3-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>`{=html}
`<img src="https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white"/>`{=html}
`<img src="https://img.shields.io/badge/SHAP-Explainable%20AI-8B5CF6?style=for-the-badge"/>`{=html}
`<img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>`{=html}
```{=html}
</p>
```
```{=html}
<p>
```
`<b>`{=html}Build. Break. Explain. Deploy. Repeat. 🚀`</b>`{=html}
```{=html}
</p>
```
:::

------------------------------------------------------------------------

## 🌌 What is this?

**Network Security MLOps** is an end-to-end machine learning system for
network security detection.

The project goes beyond model training and connects the complete
lifecycle:

``` text
Data → Validation → Transformation → Training → Evaluation
                     ↓
                  SHAP XAI
                     ↓
               Model Artifact
                     ↓
              Docker + FastAPI
                     ↓
              AWS ECR + S3
                     ↓
              GitHub Actions
                     ↓
          Self-Hosted Deployment
```

The focus is to make the ML system **reproducible, explainable,
containerized, and deployable**.

------------------------------------------------------------------------

## ✨ Highlights

  Area                     Implementation
  ------------------------ ----------------------------------
  📥 Data                  Automated ingestion
  🔍 Validation            Schema + drift detection
  ⚙️ Transformation        Feature preprocessing
  🤖 ML                    Multiple classification models
  🏆 Selection             Best model based on evaluation
  📊 Metrics               Precision, Recall, F1
  🧠 XAI                   SHAP explainability
  🧪 Experiment Tracking   MLflow + DagsHub
  💾 Artifacts             `model.pkl` + `preprocessor.pkl`
  ☁️ Storage               AWS S3
  🐳 Containerization      Docker
  📦 Registry              AWS ECR
  ⚙️ CI/CD                 GitHub Actions
  🖥️ Deployment            Windows self-hosted runner
  🌐 API                   FastAPI

------------------------------------------------------------------------

## 🏗️ System Architecture

`<img src="assets/architecture.svg" alt="System Architecture" width="100%"/>`{=html}

``` text
GitHub
   │
   ▼
GitHub Actions
   │
   ├── Continuous Integration
   │      ├── Checkout
   │      ├── Install dependencies
   │      ├── Tests
   │      └── Docker build
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
Network Security ML Model
   │
   ▼
Prediction
```

------------------------------------------------------------------------

## 🧠 Machine Learning Pipeline

`<img src="assets/ml-pipeline.svg" alt="Machine Learning Pipeline" width="100%"/>`{=html}

### 1. Data Ingestion

The pipeline collects the dataset and creates train/test data artifacts.

### 2. Data Validation

The incoming data is checked against the expected schema and a drift
report is generated.

### 3. Data Transformation

Features are transformed using the preprocessing pipeline.

The preprocessor is saved as:

``` text
preprocessor.pkl
```

### 4. Model Training

The training pipeline evaluates:

-   Random Forest
-   Decision Tree
-   Gradient Boosting
-   Logistic Regression
-   AdaBoost

### 5. Model Evaluation

Models are evaluated using:

-   Precision
-   Recall
-   F1 Score

The best-performing model is selected automatically.

### 6. Explainable AI

SHAP is used to understand feature importance and prediction direction.

``` text
Prediction
    │
    ▼
SHAP Values
    │
    ├── Feature importance
    ├── Positive impact
    └── Negative impact
```

### 7. Model Artifact

The final deployment artifact contains:

``` text
final_model/
├── model.pkl
└── preprocessor.pkl
```

------------------------------------------------------------------------

## 📊 Model Evaluation

The primary model-selection metric is the **F1 Score**, while Precision
and Recall are also tracked.

``` text
                 Model
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    Precision    Recall     F1 Score
        │          │          │
        └──────────┼──────────┘
                   ▼
             Best Model
```

------------------------------------------------------------------------

## 🔎 Explainable AI with SHAP

A security model should not only say:

> **"Attack detected."**

It should also help answer:

> **"Which features influenced this prediction?"**

SHAP provides feature-level explanations that make model behavior easier
to inspect.

Example workflow:

``` text
Network Traffic
      ↓
ML Model
      ↓
Prediction
      ↓
SHAP Explainer
      ↓
Feature Contributions
```

------------------------------------------------------------------------

## 🧪 MLflow + DagsHub

Training experiments are tracked with MLflow.

Tracked metrics include:

``` text
F1 Score
Precision
Recall
```

This makes it easier to compare runs and understand how model changes
affect performance.

------------------------------------------------------------------------

## ☁️ AWS Storage

The project uses AWS S3 for model/artifact storage.

``` text
AWS S3
└── final_model/
    ├── model.pkl
    └── preprocessor.pkl
```

AWS ECR is used as the Docker image registry.

``` text
Docker Build
     ↓
AWS ECR
     ↓
Docker Pull
     ↓
Deployment
```

------------------------------------------------------------------------

## 🐳 Docker

Build the application image:

``` bash
docker build -t networksecurity:test .
```

Run locally:

``` bash
docker run --env-file .env -p 8000:8000 networksecurity:test
```

Check running containers:

``` bash
docker ps
```

Check logs:

``` bash
docker logs networksecurity
```

------------------------------------------------------------------------

## ⚙️ CI/CD

Every push to `main` can trigger the deployment workflow.

``` text
                 Git Push
                    │
                    ▼
          ┌──────────────────┐
          │ GitHub Actions   │
          └────────┬─────────┘
                   │
                   ▼
                 CI
          ┌──────────────────┐
          │ Tests + Build    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │      AWS ECR     │
          │   Push Image     │
          └────────┬─────────┘
                   │
                   ▼
        Self-Hosted Runner
                   │
                   ▼
          Pull Latest Image
                   │
                   ▼
           Stop Old Container
                   │
                   ▼
            Start New Container
                   │
                   ▼
              🚀 LIVE API
```

------------------------------------------------------------------------

## 🖥️ Self-Hosted Runner

Deployment is executed through a Windows self-hosted GitHub Actions
runner.

Runner flow:

``` text
GitHub
  ↓
GitHub Actions
  ↓
Windows Runner
  ↓
Docker
  ↓
FastAPI
```

This also made the project a practical exercise in debugging Windows
PowerShell, Docker, AWS permissions, and CI/CD behavior.

------------------------------------------------------------------------

## 🌐 FastAPI

The application exposes the ML model through FastAPI.

### `GET /`

Redirects to the API documentation.

### `GET /train`

Triggers the training pipeline.

Training is imported lazily inside the route so DagsHub authentication
is not triggered during normal API startup.

### `POST /predict`

Accepts a CSV file and returns predictions.

``` text
CSV Upload
    ↓
Load Model
    ↓
Preprocess
    ↓
Predict
    ↓
Add predicted_column
    ↓
Prediction Output
```

Swagger UI:

``` text
http://localhost:8000/docs
```

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Network-security/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── Artifacts/
│   └── <timestamp>/
│       ├── data_ingestion/
│       ├── data_validation/
│       ├── data_transformation/
│       └── model_trainer/
│
├── assets/
│   ├── hero.svg
│   ├── architecture.svg
│   └── ml-pipeline.svg
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

------------------------------------------------------------------------

## 🛠️ Tech Stack

### Machine Learning

`Python` · `NumPy` · `Pandas` · `Scikit-learn` · `SHAP`

### MLOps

`MLflow` · `DagsHub` · `GitHub Actions`

### Cloud

`AWS S3` · `AWS ECR` · `AWS IAM`

### Deployment

`Docker` · `FastAPI` · `Uvicorn`

### Database

`MongoDB Atlas`

### Development

`Git` · `GitHub` · `VS Code`

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Clone

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Network-security
```

### 2. Create virtual environment

Windows:

``` cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

``` cmd
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env`:

``` env
MONGODB_URL_KEY=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_aws_region
```

**Never commit `.env` to GitHub.**

### 5. Run the training pipeline

``` cmd
python main.py
```

### 6. Start the API

``` cmd
python app.py
```

Open:

``` text
http://localhost:8000/docs
```

------------------------------------------------------------------------

## 🔮 Prediction Example

Using Swagger:

``` text
POST /predict
      ↓
Try it out
      ↓
Upload CSV
      ↓
Execute
```

The resulting dataframe contains:

``` text
predicted_column
```

and is saved to:

``` text
prediction_output/output.csv
```

------------------------------------------------------------------------

## 🔐 Security

For production use:

-   Never commit AWS credentials.
-   Never commit MongoDB credentials.
-   Store secrets in GitHub Secrets or an appropriate secret manager.
-   Use least-privilege IAM policies.
-   Rotate credentials if they are exposed.
-   Do not print connection strings in application logs.
-   Restrict MongoDB network access.
-   Add API authentication before exposing the service publicly.
-   Use HTTPS for public deployment.

------------------------------------------------------------------------

## 🧩 Real-World Debugging Lessons

This project wasn't just:

``` text
Train → Accuracy → Done
```

It involved real deployment problems such as:

``` text
AWS IAM permissions
        ↓
ECR authentication
        ↓
Docker reference errors
        ↓
Windows PowerShell syntax
        ↓
Self-hosted runner configuration
        ↓
Container crashes
        ↓
DagsHub OAuth during startup
        ↓
Environment variables
        ↓
Successful deployment 🚀
```

Every failure became part of the learning.

------------------------------------------------------------------------

## 📈 Current Status

``` text
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

------------------------------------------------------------------------

## 🗺️ Roadmap

``` text
✅ ML Pipeline
      ↓
✅ Explainable AI
      ↓
✅ Docker
      ↓
✅ AWS ECR / S3
      ↓
✅ GitHub Actions CI/CD
      ↓
✅ Automated Deployment
      ↓
🔜 AWS EC2 / ECS
      ↓
🔜 API Authentication
      ↓
🔜 Model Monitoring
      ↓
🔜 Automated Retraining
      ↓
🔜 Production Observability
```

------------------------------------------------------------------------

## 🎯 Learning Goal

This project is part of my **90 Days Learn in Public** journey.

The objective is to understand the complete ML lifecycle:

> **Build → Evaluate → Explain → Package → Deploy → Monitor**

rather than stopping at model training.

------------------------------------------------------------------------

## ⭐ If you find this useful

Give the repository a ⭐ and feel free to explore the implementation.

**Build. Break. Debug. Learn. Deploy. 🚀**

::: {align="center"}
### 🛡️ Network Security MLOps

**Machine Learning × Explainable AI × MLOps × Cloud**
:::
