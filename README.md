# Kafka Fraud Detection System

A real-time data pipeline built with Python and Apache Kafka to simulate and process financial transactions, identifying potential fraudulent activity.

## 🚀 Project Overview

This project implements a producer-consumer architecture:
1.  **Transaction Producer**: Simulates real-time financial transactions and sends them to a Kafka topic.
2.  **Fraud Consumer**: Listens to the transaction stream, applies fraud detection rules, and persists data into a local SQLite database.

## 🛠️ Tech Stack

*   **Language**: Python 3.11+
*   **Message Broker**: Apache Kafka
*   **Database**: SQLite
*   **Package Manager**: [uv](https://github.com/astral-sh/uv)
*   **Kafka Library**: `kafka-python-ng` (Compatible with Python 3.11+)

## 📁 Project Structure

*   `transaction_producer.py`: Generates and sends mock transaction data.
*   `fraud_consumer.py`: Consumes Kafka messages and saves them to the database.
*   `fraud_rules.py`: Contains logic for identifying suspicious transactions.
*   `fraud_db.db`: SQLite database for storing processed transactions.

## ⚙️ Getting Started

### 1. Prerequisites
*   [Apache Kafka](https://kafka.apache.org/downloads) installed and running locally.
*   `uv` installed for dependency management.

### 2. Installation
Clone the repository and install dependencies using `uv`:

```bash
uv sync
```