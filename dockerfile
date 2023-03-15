FROM python:3.10.4-slim-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]