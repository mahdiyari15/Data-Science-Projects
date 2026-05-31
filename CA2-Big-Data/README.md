# Real-Time Payment Data Pipeline

A robust, scalable data engineering pipeline designed to ingest, validate, and process streaming financial transactions in real-time. This project leverages Apache Kafka for event streaming, PySpark for stream processing, and MongoDB for batch aggregation and historical reporting.

## 📖 Overview

This system is built to handle live transaction data, identifying anomalies and potential fraud (such as time-warping or invalid financial totals) before they enter the analytics stream. It features a dual-processing architecture:

1. **Real-Time Stream Processing**: For live dashboarding and immediate transaction insights.
2. **Batch Processing**: For daily aggregations, merchant summaries, and commission analysis.

## Features

* **Real-Time Anomaly Detection**: A custom Kafka consumer (`consumer.py`) acts as a gatekeeper, validating timestamps, device info, and financial consistency, routing bad data to an error log topic.
* **Stream Analytics**: PySpark Structured Streaming parses JSON events and computes live metrics.
* **Historical Aggregation**: Batch jobs aggregate daily metrics and store the results in MongoDB.
* **Data Visualization**: Matplotlib-based notebooks to visualize user transaction frequencies and behaviors.

##  Architecture

1. **Ingestion**: Transaction events are produced to the `darooghe.transactions` Kafka topic.
2. **Validation**: The Gatekeeper consumer validates events and splits the stream into valid data and `darooghe.error_logs`.
3. **Stream Processing**: PySpark reads the valid stream, computes real-time insights, and pushes them to `transaction_insights`.
4. **Batch Processing**: PySpark reads accumulated data, calculates daily summaries, and writes to MongoDB.

## Prerequisites

Ensure you have the following installed on your machine:

* **Java 8 or 11** (Required for Apache Spark and Kafka)
* **Apache Kafka** (Running in KRaft mode)
* **Apache Spark** (PySpark)
* **MongoDB** (Running locally on `localhost:27017`)
* **Python 3.8+** Install the required Python packages:

```bash
pip install kafka-python pyspark pymongo matplotlib

```

##  Getting Started

### 1. Start Infrastructure

Start your MongoDB service. Then, start Kafka.

### 2. Run the Gatekeeper

Intercept and filter live transactions by running the validation script:

```bash
python consumer.py

```

### 3. Start the Data Producer

*(Run your external producer script here to start feeding JSON events into the Kafka topic).*

### 4. Run Real-Time Analytics

Open Jupyter Notebook and run the streaming pipelines:

* **`real_time_processing.ipynb`**: Initializes the PySpark streaming job.
* **`consume_realtime_topics.ipynb`**: Consumes and displays the live generated insights.

### 5. Run Batch Processing & Visualization

Once sufficient data is ingested, process the historical data:

* **`batch_proccessing.ipynb`**: Groups data by day/merchant and writes the aggregations to MongoDB.
* **`plots.ipynb`**: Generates bar charts and visualizations of user transaction frequencies.


