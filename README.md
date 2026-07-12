# 🛒 Walmart Data Engineering Pipeline using Apache Airflow, dbt & PostgreSQL

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-red)
![dbt](https://img.shields.io/badge/dbt-Core-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)

## 📌 Project Overview

This project demonstrates an end-to-end modern Data Engineering pipeline that automates data transformation using **Apache Airflow**, **dbt**, **PostgreSQL**, and **Docker**. The pipeline follows analytics engineering best practices by orchestrating data validation, transformation, testing, and reporting through a scalable and modular architecture.

Apache Airflow acts as the orchestration engine, executing dbt commands in sequence to build a reliable transformation workflow. dbt manages SQL-based transformations using layered models (Silver Technical, Silver Business, and Gold) while ensuring data quality through built-in tests and reusable macros.

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

## 📈 Future Enhancements

- CI/CD with GitHub Actions
- Incremental dbt models
- Great Expectations integration
- dbt Documentation Hosting
- Databricks deployment
- Cloud object storage integration

---

## 👨‍💻 Author

**Sachin Kumar Pal**

Data Engineer | Apache Airflow | dbt | PostgreSQL | Python | SQL

---
⭐ If you found this project useful, consider giving it a star!
