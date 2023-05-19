import inspect

from databricks_api import DatabricksAPI
import databricks_cli


db = DatabricksAPI(host="localhost", token="token")


intro = """databricks-api
==============

**Please switch to the `official Databricks SDK for Python<https://github.com/databricks/databricks-sdk-py>` by running the following command:**

.. code-block:: bash

    pip install databricks-sdk


|pypi| |pyversions|

.. |pypi| image:: https://img.shields.io/pypi/v/databricks-api.svg
    :target: https://pypi.python.org/pypi/databricks-api

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/databricks-api.svg
    :target: https://pypi.python.org/pypi/databricks-api

*[This documentation is auto-generated]*

This package provides a simplified interface for the Databricks REST API.
The interface is autogenerated on instantiation using the underlying client
library used in the official ``databricks-cli`` python package.

Install using

.. code-block:: bash

    pip install databricks-api
    

The docs here describe the interface for version **{version}** of
the ``databricks-cli`` package for API version **{api_version}**.

The ``databricks-api`` package contains a ``DatabricksAPI`` class which provides
instance attributes for the ``databricks-cli`` ``ApiClient``, as well as each of
the available service instances. The attributes of a ``DatabricksAPI`` instance are:

""".format(
    version=databricks_cli.version.version, api_version=databricks_cli.sdk.version.API_VERSION
)

attrs = []

for k, v in db.__dict__.items():
    attrs.append("* DatabricksAPI." + k + " *<" + v.__class__.__module__ + "." + v.__class__.__name__ + ">*\n")

signature = str(inspect.signature(databricks_cli.sdk.ApiClient))
signature = "(\n        " + ",\n        ".join(signature[1:-1].split(", ")) + "\n    )"

middle = """
To instantiate the client, provide the databricks host and either a token or
user and password. Also shown is the full signature of the
underlying ``ApiClient.__init__``

.. code-block:: python

    from databricks_api import DatabricksAPI

    # Provide a host and token
    db = DatabricksAPI(
        host="example.cloud.databricks.com",
        token="dpapi123..."
    )

    # OR a host and user and password
    db = DatabricksAPI(
        host="example.cloud.databricks.com",
        user="me@example.com",
        password="password"
    )

    # Full __init__ signature
    {instantiate}

Refer to the `official documentation <https://docs.databricks.com/api/index.html>`_
on the functionality and required arguments of each method below.

Each of the service instance attributes provides the following public methods:

""".format(
    instantiate="db = DatabricksAPI" + signature
)

services = []
for k, v in db.__dict__.items():
    if k == "client":
        continue
    print(k, v)
    h = "DatabricksAPI." + k
    services.append(h + "\n")
    services.append("-" * len(h) + "\n\n")
    services.append(".. code-block:: python\n\n")
    methods = inspect.getmembers(v, predicate=inspect.ismethod)
    print(methods)
    for method in methods:
        print(method)
        if not method[0].startswith("_"):
            signature = str(inspect.signature(method[1]))
            if "," in signature:
                signature = "(\n        " + ",\n        ".join(signature[1:-1].split(", ")) + ",\n    )"
            services.append("    db." + k + "." + method[0] + signature + "\n\n")
    services.append("\n")


with open("README.rst", "w") as f:
    f.write(intro)
    for a in attrs:
        f.write(a)
    f.write(middle)
    for s in services:
        f.write(s)
