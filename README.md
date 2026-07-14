# Online-Shop "Mugunghwa Blooms & Roots" Data Stack

## Description

## Technologies
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Snowflake](https://img.shields.io/badge/snowflake-%2329B5E8.svg?style=for-the-badge&logo=snowflake&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 🏗️ Architecture  
<img width="5647" height="3107" alt="Architecture" src="https://github.com/nazariikolesnikov/mugunghwa-blooms-and-roots-datastack/blob/main/architecture/architecture.png" />

## 📂 Repository Structure
```text
magunghwa-blooms-and-roots-datastack/
├── .github/workflows/             # CI/CD pipelines (ci.yml, cd.yml)
├── online_shop_dbt/                # DBT project
│   ├── models/
│   │   ├── staging/               # Staging models
│   │   ├── marts/                 # Facts & dimensions
│   │   └── sources.yml
│   ├── snapshots/                 # SCD2 snapshots
│   └── dbt_project.yml
├── consumer
│   └── kafka_to_minio.py
├── data-generator/                # Faker-based data simulator
│   └── faker_generator.py
├── docker/                        # Airflow DAGs, plugins
│   ├── dags/                      # DAGs (minio_to_snowflake, scd_snapshots)
├── kafka-debezium/                # Kafka connectors & CDC logic
│   └── generate_and_post_connector.py
├── postgres/                      # Postgres schema (OLTP DDL & seeds)
│   └── schema.sql
├── .gitignore
├── docker-compose.yml             # Containerized infra
├── dockerfile-airflow.dockerfile
├── requirements.txt
└── README.md
