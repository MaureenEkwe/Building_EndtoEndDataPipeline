## README: Real-Time Streaming End to End Data Processing Pipeline 

### Course
CISC 5950 – Big Data Computing
Created By: Maureen Ekwebelm & Andre Chuabio

---

## Project Description

This project implements Streaming Data Processing and while Spark Streaming was introduced conceptually in class, this project focuses on applying Spark Streaming APIs in a **cluster-based environment**, rather than a local-only setup.

The implementation follows the provided online tutorial and combines course concepts such as **window-based real-time data processing**, **Spark Streaming APIs**, and **distributed system orchestration**. All components were configured to run within a clustered environment using Docker.

---

## Project Objective

The goals of this project were to:
- Build a real-time streaming data processing pipeline
- Apply Apache Spark Streaming APIs for continuous data ingestion and processing
- Run the system in a cluster environment (not local mode)
- Integrate multiple distributed system components
- Reinforce concepts learned in class related to streaming and big data systems

---

## System Architecture

The real-time data pipeline consists of the following components:

- **Apache Kafka**: Used as the real-time data ingestion layer for streaming messages.
- **Apache Spark (Spark Streaming / Structured Streaming)**: Consumes and processes streaming data from Kafka using Spark Streaming APIs.
- **Docker & Docker Compose**: Used to orchestrate the cluster environment, including Kafka and Spark services.

This architecture simulates a realistic streaming workflow where data is continuously produced, streamed, and processed in near real time.

---

## Project Structure

- README.md  
- docker-compose.yml  
- kafka_producer.py  
- kafka_stream.py  
- spark_job.py  
- spark_stream.py  

---

## File Descriptions

- **README.md**  
  Project documentation and usage instructions.

- **docker-compose.yml**  
  Defines and orchestrates the cluster environment for Kafka and Spark services.

- **kafka_producer.py**  
  Simulates real-time data generation and publishes messages to Kafka topics.

- **kafka_stream.py**  
  Handles Kafka streaming logic and topic interaction.

- **spark_stream.py**  
  Implements Spark Streaming / Structured Streaming logic to consume Kafka data and perform real-time processing.

- **spark_job.py**  
  Contains Spark job configuration and processing logic executed within the cluster.

---

## Running the Pipeline

1. Start the cluster environment using Docker Compose.
2. Launch the Kafka producer to generate streaming data.
3. Submit the Spark streaming job to the Spark cluster.
4. Observe real-time data processing through Spark Streaming logs.

---

## Notes

All components were configured to run in a clustered environment rather than local mode.

The project code and configuration were adapted from the provided tutorial and extended to work within a distributed cluster setup.

---

## Technologies Used

- Apache Spark (Spark Streaming / Structured Streaming)
- Apache Kafka
- Docker & Docker Compose
- Python

