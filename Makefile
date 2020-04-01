VERSION := ${shell poetry run python -c "import databricks_api; print(databricks_api.__version__)"}

.PHONY: setup
setup:
	brew install asdf ghr || True
	asdf install
	poetry install

.PHONY: build
build:
	poetry build

.PHONY: publish
publish: build
	poetry publish

.PHONY: release
release: publish
	@echo sha: $(shell git rev-parse HEAD)
	@echo version: $(VERSION)
	ghr -t $(GITHUB_TOKEN) -u crflynn -r databricks-api -c $(shell git rev-parse HEAD) -delete $(VERSION) -replace dist/*-$(VERSION)*

.PHONY: update
update:
	poetry update databricks_cli
	poetry run python generate_docs.py
