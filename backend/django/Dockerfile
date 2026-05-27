# Multi-stage build for the Django monolith image. Mirrors the production
# setup used in the talk's source codebase.
ARG DOCKER_HUB_MIRROR=""
FROM ${DOCKER_HUB_MIRROR}python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:0.7.6 /uv /uvx /bin/

WORKDIR /app
ENV UV_LINK_MODE=copy

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the django project plus its editable workspace dependencies.
# Order matters: dependency manifests first so `uv sync` is cached.
COPY django /app
COPY ml /ml
COPY util /util

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --no-editable

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
