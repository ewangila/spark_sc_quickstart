# PySpark Context Inspector

Minimal script that creates a SparkContext and prints core runtime properties, resource allocation, and system information.

## Features
- Initialize a local SparkContext
- Display app name, master, version
- Show start time, parallelism, and partitions
- Print Spark user, home, application ID, and UI URL

## Tech Stack
- Python 3, PySpark

## Installation
```bash
pip install -r requirements.txt
```
## Usage
```bash
python spark.py
```
## Sample Output
```
Basic Info
Type: <class 'pyspark.context.SparkContext'>
App Name: learning
Master: local[*]
Version: 3.x.x

Startup Info
Start Time (raw): ...
Start Time (readable): ...

Resource Info
Default Parallelism: ...
Default Min Partitions: ...

User & System Info
Spark User: ...
Spark Home: ...
Application ID: ...
```
## Project Structure
```
├── spark.py
├── requirements.txt
├── LICENCE
└── README.md
```
UI & Status
UI Web URL: ...
