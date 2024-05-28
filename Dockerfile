FROM python:3.10.11

WORKDIR /app

ENV PYTHONPATH=/app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY backend/pyproject.toml ./poetry.lock* .

RUN poetry install
RUN pip install --upgrade pip

COPY ./backend .

ENTRYPOINT ["/app/entrypoint"]
