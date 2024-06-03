FROM python:3.12-slim
ENV POETRY_VIRTUALENVS=false

WORKDIR /app/
COPY ./backend .

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

CMD poetry run python manage.py runserver 0.0.0.0:8000