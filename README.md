<div align="center">

# HotelHub — hotel booking service

| CI/CD | [![Build and Push Image](https://github.com/0x12th/hotelhub/actions/workflows/push-image.yml/badge.svg)](https://github.com/0x12th/hotelhub/actions/workflows/push-image.yml) [![Lints](https://github.com/0x12th/hotelhub/actions/workflows/lints.yml/badge.svg)](https://github.com/0x12th/hotelhub/actions/workflows/lints.yml) |
|:---:|:---:|
| Activity | ![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/0x12th/hotelhub?&logo=github&logoColor=969da4&labelColor=30353b&color=39A7FF) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/0x12th/hotelhub/master?&logo=github&logoColor=969da4&labelColor=30353b&color=39A7FF) |
| Meta | [![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet?labelColor=30353b&color=39A7FF)](https://pdm-project.org) [![code style - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json?&logo=ruff&logoColor=969da4&labelColor=30353b&color=39A7FF)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-202235.svg?logo=python&labelColor=30353b&color=39A7FF&logoColor=969da4)](https://github.com/python/mypy) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg?labelColor=30353b&color=39A7FF)](https://spdx.org/licenses/) |

</div>

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
