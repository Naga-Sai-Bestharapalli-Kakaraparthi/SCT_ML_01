# Containerized Housing Data ETL Pipeline

## Overview
This repository contains an automated ETL (Extract, Transform, Load) pipeline built using Python and Pandas. It processes raw housing datasets, cleans missing values and invalid records, standardizes column schemas, and exports structured output files.

## Tech Stack
* **Language:** Python 3.9
* **Data Processing:** Pandas, NumPy
* **Containerization:** Docker

## Pipeline Architecture
1. **Extract:** Ingests raw CSV data from the source directory.
2. **Transform:** Cleans null values, removes duplicates, and standardizes schema headers.
3. **Load:** Exports cleaned data into structured format for downstream analysis.

## How to Run with Docker

1. **Build the Docker Image:**
   `docker build -t housing-etl-pipeline .`

2. **Run the Container:**
   `docker run --rm housing-etl-pipeline`
