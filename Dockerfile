# Dockerfile, Image, Container 
FROM python:latest 

ADD main.py .

RUN pip install os discord responses dotenv

CMD [ "python", "./main.py"]