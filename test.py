import os

from databricks_api.databricks import DatabricksAPI

TOKEN = os.environ["DATABRICKS_TOKEN"]
HOST = os.environ["DATABRICKS_HOST"]


def test_databricks_api():
    db = DatabricksAPI(host=HOST, token=TOKEN)
    print(db.__dict__)
