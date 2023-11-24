sources = src tests

.PHONY: lint
lint:
	pdm run ruff $(sources)

.PHONY: fix
fix:
	pdm run ruff --fix $(sources)

.PHONY: format
format:
	pdm run ruff format $(sources)

.PHONY: mypy
mypy:
	pdm run mypy $(sources)

.PHONY: codespell
codespell:
	pre-commit run codespell --all-files

.PHONY: tests
tests:
	pdm run pytest tests/

.PHONY: docker-compose-dev
docker-compose-dev:
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: dev-run
dev-run:
	docker-compose -f docker-compose.dev.yml up -d && pdm start
