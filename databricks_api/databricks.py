import re
from pathlib import Path

import databricks_cli.sdk.service as services
from databricks_cli.sdk import ApiClient

___all__ = ["DatabricksAPI"]


def camel_to_snake(name):
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def _get_services():
    for service_name, service in services.__dict__.items():
        if "Service" in service_name:
            camel_name = camel_to_snake(service_name.replace("Service", ""))
            yield service_name, camel_name, service


class DatabricksAPI:
    def __init__(self, **kwargs):
        if "host" in kwargs:
            if not kwargs["host"].startswith("https://"):
                kwargs["host"] = "https://" + kwargs["host"]

        self.client = ApiClient(**kwargs)

        for _, camel_name, service in _get_services():
            setattr(self, camel_name, service(self.client))


def _write_stubs():
    parent_dir = Path(__file__).parent
    path = Path(parent_dir, "databricks").with_suffix(".pyi")
    with open(path, "w") as stub_file:
        stub_file.write("from databricks_cli.sdk import ApiClient\n")
        stub_file.write("from databricks_cli.sdk.service import *\n\n")
        stub_file.write(f"class {DatabricksAPI.__name__}:\n")
        stub_file.write("\tdef __init__(self, **kwargs):\n")
        stub_file.write("\t\tself.client: ApiClient = ...\n")
        stub_file.write("\n".join(
            f"\t\tself.{camel_name}: {service_name} = ..." for service_name, camel_name, service in _get_services()
        ))


if __name__ == "__main__":
    _write_stubs()
