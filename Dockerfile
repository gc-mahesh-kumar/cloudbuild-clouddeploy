#FROM python:3.12.3-alpine
#FROM python:3.14.0b1-alpine3.22
FROM python:3.14.0b3-alpine3.22

# App
WORKDIR /app
COPY main.py ./

#Requirments.txt
RUN pip3 install Flask

ENTRYPOINT ["python3", "main.py"]
