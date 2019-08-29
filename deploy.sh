#!/usr/bin/env bash
set -e
export VERSION=$(poetry run python -c "import databricks_api; print(databricks_api.__version__)")
poetry build
poetry run twine upload dist/databricks_api-${VERSION}*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags