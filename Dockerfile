FROM nikolaik/python-nodejs:python3.9-nodejs14

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
