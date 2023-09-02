FROM python:3

WORKDIR /my_code

COPY ./requirements.txt /my_code/

RUN pip3 install -r requirements.txt

COPY . .