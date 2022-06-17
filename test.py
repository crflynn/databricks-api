import os

from databricks_api.databricks import DatabricksAPI

TOKEN = os.environ["DATABRICKS_TOKEN"]
HOST = os.environ["DATABRICKS_HOST"]


def test_databricks_api():
    db = DatabricksAPI(host=HOST, token=TOKEN)
    print(db.__dict__)


def test_cli_version():
    from databricks_api import __cli_version__
    from databricks_cli.version import version

    assert __cli_version__ == version
