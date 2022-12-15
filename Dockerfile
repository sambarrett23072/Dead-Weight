# Dockerfile, Image, Container 
FROM python:latest 

ADD main.py .

RUN pip install discord responses

CMD [ "python", "./main.py"]