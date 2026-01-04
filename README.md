# 🚀 End-to-End MLOps Pipeline: Develop to Deploy (Assignment 2)

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-blue?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-SageMaker%20%7C%20EC2-orange?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-Astro-red?style=for-the-badge&logo=apache-airflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-Data%20Versioning-purple?style=for-the-badge&logo=dvc&logoColor=white)

## 📖 Project Overview
This project demonstrates a complete **Machine Learning Operations (MLOps) pipeline** designed to automate the lifecycle of an ML model from development to production deployment.

The system integrates **Data Version Control (DVC)** for dataset management, **Docker** for containerization, **Apache Airflow** for workflow orchestration, and **AWS** for scalable cloud deployment.

It implements **two distinct deployment strategies**:
1.  **Containerized Deployment:** Hosting a FastAPI inference server on **AWS EC2**.
2.  **Serverless Deployment:** A scalable architecture using **AWS SageMaker, Lambda, and API Gateway**.

---

## 🏗️ Architecture & Workflow

The pipeline follows these core stages:

1.  **Data Ingestion:** Raw data is tracked via **DVC** and stored in **AWS S3** (`s3://bucket-name`).
2.  **Orchestration (ETL):** **Apache Airflow (Astro)** manages the Extract, Transform, and Load (ETL) tasks via DAGs.
3.  **Training:** Models are trained using **SageMaker Estimators** (Serverless) or locally via Docker.
4.  **Deployment:**
    * **Method A (IaaS):** Docker container running FastAPI deployed on EC2.
    * **Method B (Serverless):** SageMaker Endpoint connected via AWS Lambda & API Gateway.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.9 | Core programming language. |
| **Versioning** | Git & DVC | Code and Data Version Control. |
| **Containerization** | Docker | Packaging the application and dependencies. |
| **Orchestration** | Apache Airflow | Managing ETL DAGs (via Astro CLI). |
| **Cloud Compute** | AWS EC2 | Hosting the Dockerized API. |
| **Model Training** | AWS SageMaker | Managed training jobs on the cloud. |
| **Serverless** | AWS Lambda | Connecting API Gateway to SageMaker Endpoints. |
| **API** | FastAPI | RESTful interface for model inference. |

---

## 📂 Project Structure

```bash
├── .github/workflows/   # CI/CD Pipelines (GitHub Actions)
├── airflow/             # Airflow Configuration (Astro)
│   ├── dags/            # ETL Python DAGs
│   └── Dockerfile       # Airflow image config
├── app/                 # Main Application Source
│   ├── main.py          # FastAPI Endpoints
│   └── model.pkl        # Serialized Model (Locally trained)
├── data/                # Local data storage (DVC tracked)
├── .dvc/                # DVC Configuration
├── Dockerfile           # Docker configuration for API
├── dvc.yaml             # DVC Pipeline stages
├── requirements.txt     # Python Dependencies
└── README.md            # Project Documentation
