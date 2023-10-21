FROM python:3.11-slim-buster AS builder


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

RUN pip install -U pip setuptools wheel
RUN pip install pdm

WORKDIR /hotelhub

COPY pyproject.toml pdm.lock /hotelhub/
COPY src/ /hotelhub/src

RUN mkdir __pypackages__ && pdm sync --prod --no-editable

FROM python:3.11-slim-buster

ENV PYTHONPATH=/hotelhub/pkgs
COPY --from=builder /hotelhub/__pypackages__/3.11/lib /hotelhub/pkgs

COPY --from=builder /hotelhub/__pypackages__/3.11/bin/* /bin/
COPY --from=builder /hotelhub/src/ /hotelhub/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
