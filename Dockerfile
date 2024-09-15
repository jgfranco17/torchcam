FROM python:3.10-alpine AS build-stage

# Set environment variables
ENV POETRY_VERSION=1.8.3
ENV PYTHONUNBUFFERED=1

RUN pip install poetry=="${POETRY_VERSION}"
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app

# Minimal copy to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /app
ENTRYPOINT ["poetry", "run", "torchcam"]

# Override the entrypoint to start a shell if no command is provided
CMD ["--help"]
