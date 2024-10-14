FROM python:3.11 AS base

WORKDIR /home/atcloud
ENV PYTHONPATH="/home/atcloud"

RUN pip install poetry==1.8.3

COPY --chown=myuser:myuser poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY --chown=myuser:myuser malloy_mre malloy_mre


FROM base AS app
CMD ["python3", "-m", "malloy_mre"]