# Databricks notebook source

import pyspark
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType,StructField, StringType

spark = SparkSession.builder.appName('spark_copy_data').getOrCreate()

# COMMAND ----------

dbutils.fs.mkdirs('dbfs:/FileStore/transient/departments/countries')
dbutils.fs.mkdirs('dbfs:/FileStore/transient/departments/regions')
dbutils.fs.mkdirs('dbfs:/FileStore/transient/departments/jobs')
dbutils.fs.mkdirs('dbfs:/FileStore/transient/departments/employees')
dbutils.fs.mkdirs('dbfs:/FileStore/transient/departments/locations')
dbutils.fs.mkdirs('dbfs:/FileStore/transient/departments/departments')

# COMMAND ----------

def download_Copy_File(folder : str,file : str) :
    url = ' https://raw.githubusercontent.com/jader-lima/pyspark_introducao/main/datalake/transient/departments/{}/{} -P /tmp/'.format(folder,file)
    ! wget $url
    origin = "file:/tmp/{}".format(file)
    sink = "/FileStore/transient/departments/{}/{}".format(folder,file)
    dbutils.fs.cp(origin, sink)
    !rm /tmp/$file

# COMMAND ----------

download_Copy_File('countries','countries.csv')

# COMMAND ----------

download_Copy_File('departments','departments.csv')

# COMMAND ----------

download_Copy_File('dependents','dependents.csv')

# COMMAND ----------

download_Copy_File('employees','employees.csv')

# COMMAND ----------

download_Copy_File('jobs','jobs.csv')

# COMMAND ----------

download_Copy_File('locations','locations.csv')

# COMMAND ----------

download_Copy_File('regions','regions.csv')

# COMMAND ----------

print(dbutils.fs.ls('dbfs:/FileStore/transient/departments/departments'))
print(dbutils.fs.ls('dbfs:/FileStore/transient/departments/dependents'))
print(dbutils.fs.ls('dbfs:/FileStore/transient/departments/employees'))
print(dbutils.fs.ls('dbfs:/FileStore/transient/departments/jobs'))
print(dbutils.fs.ls('dbfs:/FileStore/transient/departments/locations'))
print(dbutils.fs.ls('dbfs:/FileStore/transient/departments/regions'))

# COMMAND ----------


