# syntax=docker/dockerfile:1.2
FROM python:3.12-slim

# -- suppress DL3002 for ARGs carrying secrets --
# hadolint ignore=DL3002
ARG COLVERT_PYPI_USER
# hadolint ignore=DL3002
ARG COLVERT_PYPI_PASSWORD

WORKDIR /app

# Copy only lockfiles first to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install dependencies using Poetry
# Inline the HTTP-basic creds for a single RUN, so they never persist in layers
RUN \
    POETRY_HTTP_BASIC_COLVERT_USERNAME="$COLVERT_PYPI_USER" \
    POETRY_HTTP_BASIC_COLVERT_PASSWORD="$COLVERT_PYPI_PASSWORD" \
    poetry install --no-interaction --no-ansi --only main

# Now copy the application code
COPY . .

# Create a non-root user and switch to it
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Use the poetry script we defined
CMD ["poetry", "run", "main"]
