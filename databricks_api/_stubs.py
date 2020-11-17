from pathlib import Path

from databricks_api.databricks import DatabricksAPI
from databricks_api.databricks import _get_services


def _write_stubs():
    parent_dir = Path(__file__).parent
    path = Path(parent_dir, "databricks").with_suffix(".pyi")
    with open(path, "w") as stub_file:
        stub_file.write("from databricks_cli.sdk import ApiClient\n")
        stub_file.write("from databricks_cli.sdk.service import *\n\n")
        stub_file.write(f"class {DatabricksAPI.__name__}:\n")
        stub_file.write("    def __init__(self, **kwargs):\n")
        stub_file.write("        self.client: ApiClient = ...\n")
        stub_file.write(
            "\n".join(
                f"        self.{camel_name}: {service_name} = ..."
                for service_name, camel_name, service in _get_services()
            )
        )
        stub_file.write("\n")


if __name__ == "__main__":
    _write_stubs()
