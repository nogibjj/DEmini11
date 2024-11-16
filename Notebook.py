# Databricks notebook source
!pip install -r requirements.txt

# COMMAND ----------

# MAGIC  %restart_python 

# COMMAND ----------


dbutils.fs.ls("dbfs:/FileStore")


# COMMAND ----------

!pip install python-dotenv


# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/FileStore/tables")


# COMMAND ----------

# MAGIC %pip install python-dotenv
# MAGIC

# COMMAND ----------

from dotenv import load_dotenv
import os

load_dotenv()
server_h = os.getenv("SERVER_HOSTNAME")
access_token = os.getenv("ACCESS_TOKEN")

print("Server hostname:", server_h)
print("Access token:", access_token)


# COMMAND ----------


import requests

server_h = "<your-databricks-workspace-url>"
access_token = "<your-access-token>"
url = f"https://{server_h}/api/2.0/jobs/run-now"

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

try:
    response = requests.get(f"https://{server_h}/api/2.0/clusters/list", headers=headers)
    print(response.status_code, response.text)
except requests.ConnectionError as e:
    print("Connection error:", e)


# COMMAND ----------

dbutils.fs.put("dbfs:/FileStore/.env", """
SERVER_HOSTNAME = "dbc-c95fb6bf-a65d.cloud.databricks.com"
ACCESS_TOKEN = "dapi265dbf9df531b4323b162d622cb136e1"
HTTP_PATH = "/sql/1.0/warehouses/2d6f41451e6394c0"
JOB_ID = "1004965230252512"
""", overwrite=True)


# COMMAND ----------

!git config --global user.name "Samantha"
!git config --global user.email "samantha@example.com"



# COMMAND ----------

!git add .
!git commit -m "first commit from DBricks"
!git push origin main
