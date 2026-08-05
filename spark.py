from pyspark import SparkContext
from datetime import datetime

# Create SparkContext
sc = SparkContext("local[*]", "learning")

# BASIC INFO
print("Basic Info")
print(f"Type: {type(sc)}")
print(f"App Name: {sc.appName}")
print(f"Master: {sc.master}")
print(f"Version: {sc.version}")

# STARTUP INFO 
print("\nStartup Info")
print(f"Start Time (raw): {sc.startTime}")
readable_time = datetime.fromtimestamp(sc.startTime / 1000)
print(f"Start Time (readable): {readable_time}")

#  RESOURCE INFO 
print("\nResource Info")
print(f"Default Parallelism: {sc.defaultParallelism}")
print(f"Default Min Partitions: {sc.defaultMinPartitions}")

# USER & SYSTEM INFO 
print("\nUser & System Info")
print(f"Spark User: {sc.sparkUser}")
print(f"Spark Home: {sc.sparkHome}")
print(f"Application ID: {sc.applicationId}")

# UI & STATUS 

print("\nUI & Status")
print(f"UI Web URL: {sc.uiWebUrl}")

# Clean up
sc.stop()
