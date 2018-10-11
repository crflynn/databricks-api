import re

from databricks_cli.sdk import ApiClient
import databricks_cli.sdk.service as services


def camel_to_snake(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


class DatabricksAPI(object):
    def __init__(self, **kwargs):
        if "host" in kwargs:
            if not kwargs["host"].startswith("https://"):
                kwargs["host"] = "https://" + kwargs["host"]

        self.client = ApiClient(**kwargs)

        for service_name, service in services.__dict__.items():
            if "Service" in service_name:
                name = camel_to_snake(service_name.replace("Service", ""))
                setattr(self, name, service(self.client))
