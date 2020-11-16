VERSION := ${shell poetry run python -c "import databricks_api; print(databricks_api.__version__)"}

.PHONY: setup
setup:
	brew install asdf ghr || True
	asdf install
	poetry install

.PHONY: clean
clean:
	rm -rf dist/

.PHONY: build
build:
	poetry build

.PHONY: publish
publish: build
	poetry publish

.PHONY: release
release: clean publish
	@echo sha: $(shell git rev-parse HEAD)
	@echo version: $(VERSION)
	ghr -t $(GITHUB_TOKEN) -u crflynn -r databricks-api -n $(VERSION) -c $(shell git rev-parse HEAD) -delete $(VERSION) dist/

.PHONY: update
update:
	poetry update databricks_cli
	poetry run python generate_docs.py

stubs:
	poetry run python -m databricks_api.databricks