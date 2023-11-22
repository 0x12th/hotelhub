
# HotelHub — hotel booking service

[![Create and publish a Docker image](https://github.com/0x12th/hotelhub/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/0x12th/hotelhub/actions/workflows/docker-publish.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/0x12th/hotelhub)

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

#### DB, CACHE
`POSTGRES_DSN`
`REDIS_DSN`

#### JWT
`SECRET_KEY`
`ALGORITHM`
`ACCESS_TOKEN_EXPIRE_MINUTES`


## Deployment
To deploy this project run

```bash
  docker-compose -f docker-compose.dev.yml up -d && pdm start
```
