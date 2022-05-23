FROM nikolaik/python-nodejs:python3.9-nodejs14

WORKDIR /app

COPY requirements.txt requirements.txt
COPY infrastructure/package-lock.json infrastructure/package-lock.json
COPY infrastructure/package.json infrastructure/package.json

RUN pip3 install -r requirements.txt
RUN cd infrastructure/ && npm i && npm install -g aws-cdk
