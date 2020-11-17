import re

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
