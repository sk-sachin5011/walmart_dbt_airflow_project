# 🛒 Walmart Data Engineering Pipeline using Databricks, Apache Airflow & dbt

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-EF3E42?logo=databricks)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-017CEE?logo=apache-airflow)
![dbt](https://img.shields.io/badge/dbt-Core-FF694B?logo=dbt)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Storage-00ADD8)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)

---

# 📌 Project Overview

This project demonstrates an end-to-end modern Data Engineering pipeline built using **Databricks**, **Delta Lake**, **Apache Airflow**, **dbt**, and **Docker**. The pipeline automates Change Data Capture (CDC) ingestion, data transformation, orchestration, and dimensional modeling by following modern Lakehouse and Analytics Engineering best practices.

Raw Walmart transactional data is ingested into Databricks through a CDC pipeline and stored as Delta tables using the **Medallion Architecture (Bronze → Silver → Gold)**. dbt then consumes the curated Gold layer to implement the **One Big Table (OBT)** approach before building analytics-ready **Fact** and **Dimension** models. Apache Airflow orchestrates the complete workflow by executing dbt seed, run, and test commands, ensuring a reliable, scalable, and automated ELT pipeline.

---

# 🎯 Project Objective

The primary objective of this project is to build a scalable and production-ready Data Engineering solution that transforms raw Walmart transactional data into trusted analytical datasets.

The project demonstrates the integration of Databricks for CDC ingestion, Delta Lake for scalable storage, dbt for SQL-based transformations and dimensional modeling, and Apache Airflow for workflow orchestration. By leveraging the Medallion Architecture together with the One Big Table (OBT) approach, the pipeline produces optimized Fact and Dimension tables that support reporting, dashboarding, and business analytics while ensuring data quality, maintainability, and scalability.

---

# 🏗️ Solution Architecture

```text
                           Walmart Source Data
                                    │
                                    ▼
                    +-------------------------------+
                    |         Databricks            |
                    |     CDC Data Ingestion        |
                    +---------------+---------------+
                                    │
                                    ▼
                    +-------------------------------+
                    |      Bronze Delta Tables      |
                    |        (Raw Data)             |
                    +---------------+---------------+
                                    │
                                    ▼
                    +-------------------------------+
                    |      Silver Delta Tables      |
                    |   Cleansed & Standardized     |
                    +---------------+---------------+
                                    │
                                    ▼
                    +-------------------------------+
                    |       Gold Delta Tables       |
                    |  Business Ready Datasets      |
                    +---------------+---------------+
                                    │
                                    ▼
                    +-------------------------------+
                    |              dbt              |
                    |    OBT → Fact & Dimensions    |
                    +---------------+---------------+
                                    │
               +--------------------+--------------------+
               |                                         |
               ▼                                         ▼
         dbt Tests                               dbt Documentation
               │
               ▼
                    +-------------------------------+
                    |      Apache Airflow           |
                    | Pipeline Orchestration        |
                    +---------------+---------------+
                                    │
                                    ▼
                      Dashboards • Reporting • Analytics
```

---

# 🚀 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python, SQL |
| Data Ingestion | Databricks |
| Storage | Delta Lake |
| Data Modeling | dbt Core |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker & Docker Compose |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
walmart_dbt_airflow_project
│
├── airflow/
│   └── dags/
│       └── orchestrate.py
│
├── walmart_de/
│   ├── models/
│   │   ├── silver_technical/
│   │   ├── silver_business/
│   │   ├── gold/
│   │   └── marts/
│   │
│   ├── macros/
│   ├── seeds/
│   ├── tests/
│   ├── snapshots/
│   └── dbt_project.yml
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🔄 Pipeline Workflow

The pipeline follows a modern ELT architecture consisting of the following stages:

1. **CDC Ingestion**
   - Databricks ingests Walmart transactional data using Change Data Capture (CDC).

2. **Medallion Architecture**
   - Raw data is stored in Bronze Delta tables.
   - Cleansing and standardization are performed in Silver.
   - Business-ready datasets are produced in Gold.

3. **Analytics Engineering**
   - dbt consumes Gold Delta tables.
   - Builds an **One Big Table (OBT)**.
   - Creates analytics-ready Fact and Dimension models.

4. **Pipeline Orchestration**
   - Apache Airflow orchestrates the complete dbt workflow.
   - Executes:
     - dbt Run
     - dbt Test

5. **Data Quality**
   - dbt tests validate data integrity, uniqueness, relationships, and completeness before publishing analytical models.

---

# 📊 Data Modeling Approach

The project follows modern Analytics Engineering principles.

### Silver Technical Layer
- Cleans raw source data
- Standardizes formats
- Removes invalid records
- Applies technical transformations

### Silver Business Layer
- Implements business rules
- Calculates derived attributes
- Creates reusable business entities

### Gold Layer
- Produces curated business-ready datasets
- Serves as the input for dimensional modeling

### OBT (One Big Table)
- Combines curated business entities into a consolidated analytical dataset.

### Fact & Dimension Models
Using dbt, the OBT is transformed into dimensional models consisting of:

- Fact Tables
- Dimension Tables

These models are optimized for analytical queries, reporting, and dashboarding.

---

# ✅ Key Features

- End-to-end ELT pipeline
- CDC-based data ingestion using Databricks
- Medallion Architecture (Bronze, Silver, Gold)
- Delta Lake storage
- Modern Analytics Engineering using dbt
- One Big Table (OBT) implementation
- Fact & Dimension data modeling
- Automated orchestration using Apache Airflow
- Modular dbt project architecture
- Reusable dbt macros
- Automated data quality testing
- Dockerized development environment
- Production-ready project structure

---

# ▶️ Getting Started

### Clone Repository

```bash
git clone https://github.com/sk-sachin5011/walmart_dbt_airflow_project.git

cd walmart_dbt_airflow_project
```

### Start the Environment

```bash
docker compose up -d
```

### Execute dbt

```bash

dbt run

dbt test
```

### Start Airflow

Open Airflow UI:

```
http://localhost:8080
```

Trigger the **orchestrate** DAG to execute the complete pipeline.

---

# ✅ Data Quality

The project uses dbt tests to validate:

- Primary Key uniqueness
- Referential integrity
- Accepted values
- Null checks
- Data consistency
- Business rule validation

This ensures that only trusted datasets are promoted for analytical consumption.

---

# 📈 Business Value

This project demonstrates how a modern Lakehouse architecture can automate data ingestion, transformation, orchestration, and dimensional modeling using industry-standard Data Engineering tools.

The resulting analytical models provide a reliable foundation for business intelligence, reporting, KPI tracking, and advanced analytics while maintaining scalability, modularity, and data quality.

---

# 👨‍💻 Author

**Sachin Kumar Pal**

**Data Engineer**

**Skills:** Databricks • Apache Airflow • dbt • Delta Lake • Python • SQL • Docker • Git

If you found this project helpful, consider giving it a ⭐ on GitHub.
