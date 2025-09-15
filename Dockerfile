FROM python:3.9-slim

WORKDIR /app
COPY . /app

# Install minimal build tools needed for Poetry dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "main:app"]
