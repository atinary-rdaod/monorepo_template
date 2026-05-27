# Container image for the algorithm. Demonstrates packaging the ML workspace
# as a deployable artefact — not wired to anything in the template.
ARG DOCKER_HUB_MIRROR=""
FROM ${DOCKER_HUB_MIRROR}python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.7.6 /uv /uvx /bin/

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app

COPY ml /app/ml
COPY util /app/util

RUN --mount=type=cache,target=/root/.cache/uv \
    uv venv /opt/venv && \
    cd /app/ml && uv sync --no-dev --no-editable

CMD ["python", "-c", "import algorithm; print('algorithm package available — wire it up to your runtime of choice')"]
