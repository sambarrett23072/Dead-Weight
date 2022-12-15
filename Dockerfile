# Dockerfile, Image, Container 
FROM python:latest 

ADD . /app

RUN pip install discord responses python-dotenv

CMD [ "python", "./app/main.py"]