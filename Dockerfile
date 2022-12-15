# Dockerfile, Image, Container 
FROM python:3.11.0-slim

ADD . /app

RUN pip install discord responses python-dotenv

CMD [ "python", "./app/main.py"]