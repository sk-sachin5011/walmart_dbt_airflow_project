# 🛒 Walmart Data Engineering Pipeline using Apache Airflow, dbt & PostgreSQL

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-red)
![dbt](https://img.shields.io/badge/dbt-Core-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)

## 📌 Project Overview

## 📌 Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using **Apache Airflow**, **dbt**, **PostgreSQL**, and **Docker**. It automates the complete ELT workflow—from loading and validating raw data to transforming it into business-ready analytical models.

Apache Airflow orchestrates the pipeline by executing dbt operations such as seeding, model execution, and data quality testing. dbt applies modular SQL transformations using a layered architecture (Silver Technical, Silver Business, and Gold), while PostgreSQL stores the transformed datasets. The entire solution is containerized using Docker, providing a reproducible and scalable local development environment.

The project follows modern Analytics Engineering practices, emphasizing modularity, automated testing, reusable macros, and maintainable SQL models to deliver reliable, analytics-ready data for downstream reporting and business intelligence.

---

## 🏗️ Architecture

```text
                    +-------------------+
                    |   Source Tables   |
                    |    PostgreSQL     |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Apache Airflow    |
                    | DAG Orchestration |
                    +---------+---------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
     dbt Seed            dbt Run             dbt Test
                              |
                              v
          +-----------------------------------------+
          |      dbt Transformation Layers          |
          |-----------------------------------------|
          | Silver Technical                        |
          | Silver Business                         |
          | Gold (Business Ready Models)            |
          +-------------------+---------------------+
                              |
                              v
                    Analytics / Reporting
```

---

## ⚙️ Tech Stack

- Python 3.11
- Apache Airflow
- dbt Core
- PostgreSQL
- Docker & Docker Compose
- SQL
- Jinja Macros

---

## 📂 Project Structure

```
.
├── airflow/
│   └── dags/
├── walmart_de/
│   ├── models/
│   ├── macros/
│   ├── seeds/
│   ├── tests/
│   └── dbt_project.yml
├── docker-compose.yml
└── README.md
```

---

## 🚀 Pipeline Workflow

The Airflow DAG orchestrates the complete ELT workflow by executing:

1. Clean previous dbt artifacts
2. Load seed data
3. Execute dbt models
4. Run data quality tests
5. Generate production-ready analytical tables

This layered approach separates raw transformations from business logic, making the pipeline scalable, maintainable, and easy to extend.

---

## ✨ Key Features

- End-to-end automated ELT pipeline
- Modular dbt project structure
- Layered data modeling approach
- Automated data quality testing
- Dockerized local development
- Reusable Jinja macros
- Airflow-based orchestration
- Production-ready project organization

---

## ▶️ Getting Started

```bash
git clone <repository-url>
cd walmart_dbt_airflow_project

docker compose up -d

# Run Airflow

# Execute dbt
dbt seed
dbt run
dbt test
```

---

## 👨‍💻 Author

**Sachin Kumar Pal**

Data Engineer | Apache Airflow | dbt | PostgreSQL | Python | SQL

---
⭐ If you found this project useful, consider giving it a star!
