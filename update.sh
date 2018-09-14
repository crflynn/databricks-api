#!/usr/bin/env bash

pipenv update databricks_cli
pipenv run python generate_docs.py
