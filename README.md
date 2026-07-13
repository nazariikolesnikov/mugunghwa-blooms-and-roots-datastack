# Online-Shop "Mugunghwa Blooms & Roots" Data Stack

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?logo=snowflake&logoColor=white)
![DBT](https://img.shields.io/badge/dbt-FF694B?logo=dbt&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apacheairflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=white)
![Debezium](https://img.shields.io/badge/Debezium-EF3B2D?logo=apache&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-000000?logo=githubactions&logoColor=white)

## Description

## 🏗️ Architecture  
<img width="5647" height="3107" alt="Architecture" src="" />

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
