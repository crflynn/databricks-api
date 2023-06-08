Changelog
---------
0.9.0: 2023-06-08
~~~~~~~~~~~~~~~~~

* add deprecation warning

0.8.0: 2022-06-17
~~~~~~~~~~~~~~~~~

* free the dependency constraint on ``databricks-cli``
* remove clutter from ``__version__`` module
* add ``__cli_version__`` variable referencing the ``databricks-cli`` version
* fix ``__all__`` variable in ``databricks`` module

0.7.0: 2021-11-21
~~~~~~~~~~~~~~~~~

* upgrade to cli 0.16.2

0.6.0: 2020-11-26
~~~~~~~~~~~~~~~~~
* add stub file for `DatabricksAPI`
* remove `camel_to_snake` from `__all__`

0.5.0: 2020-09-23
~~~~~~~~~~~~~~~~~

* Update to databricks-cli 0.12.0, which adds support for policy, token, and delta_pipeline APIs

0.4.0: 2020-04-01
~~~~~~~~~~~~~~~~~

* Update to databricks-cli 0.10.0, which adds back the init_script args in the cluster API

0.3.0: 2019-08-28
~~~~~~~~~~~~~~~~~

* Update to databricks-cli 0.9.0, adding instance pool functionality
* Fix package metadata access

0.2.0: 2019-08-17
~~~~~~~~~~~~~~~~~

* Update with restricted databricks-cli versions to prevent future breaking on major/minor updates to cli

0.1.0: 2018-10-10
~~~~~~~~~~~~~~~~~

* First release
