FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Install PostgreSQL client libraries
RUN apt-get update \
  && apt-get -y install libpq-dev gcc \
  && pip install psycopg2

RUN pip install poetry && poetry install --no-root

COPY . .

CMD ["poetry", "run", "start"]
