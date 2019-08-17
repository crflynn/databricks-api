#!/usr/bin/env bash

poetry update databricks_cli
poetry run python generate_docs.py
