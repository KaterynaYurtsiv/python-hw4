# Python Homework4 – MySQL Docker

## Description

This project demonstrates how to run MySQL 8.0 in Docker, automatically initialize a database, import the Titanic dataset from a CSV file, and read the data using Python.

The project includes the following functionality:

- run MySQL in Docker
- automatically create database and table
- import Titanic dataset from CSV
- handle NULL values correctly
- connect to MySQL using SQLAlchemy
- read data as pandas DataFrame
- retry connection if database is not ready

## Technologies

- Python 3.x
- MySQL 8.0
- Docker Compose
- pandas
- SQLAlchemy
- mysql-connector-python

## How to run locally

Start Docker container:

```bash
docker compose up -d

## Install dependencies:

pip install pandas sqlalchemy mysql-connector-python

## Run Python script:

python main.py

## Expected Result

The program outputs the Titanic dataset as a pandas DataFrame with:

- 891 rows
- 12 columns

## Author
Kateryna Yurtsiv
