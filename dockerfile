FROM python:3.7-slim

RUN pip install pipenv

WORKDIR /app

COPY ./src ./src/
COPY app.py .
COPY Pipfile .
COPY logging.yaml .

RUN pipenv install --skip-lock --deploy --system

ENV PYTHONPATH=/usr/local/lib/python3.6/
ENV PYTHONPATH=/app

EXPOSE 5001

CMD [ "python", "app.py" ]
