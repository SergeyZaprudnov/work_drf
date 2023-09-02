FROM python:3

WORKDIR / my_code

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver"]