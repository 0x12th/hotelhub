sources = src tests

.PHONY: lint  ## Lint python source files
lint:
	pdm run ruff $(sources)

.PHONY: mypy
mypy:
	pdm run mypy $(sources)

.PHONY: format  ## Auto-format python source files
format:
	pdm run black $(sources)
	pdm run ruff --fix $(sources)

.PHONY: codespell  ## Use Codespell to do spellchecking
codespell:
	pre-commit run codespell --all-files

.PHONY: tests
tests:
	pdm run pytest tests/

.PHONY: docker-dev up
docker-dev up:
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: dev run
dev run:
	docker-compose -f docker-compose.dev.yml up -d && pdm dev
