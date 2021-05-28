# FROM python:3.8.9-slim-buster
FROM plawler92/pyodbc38:2.0.0

RUN mkdir /checks
COPY . /app
WORKDIR /app
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

RUN pytest --ignore tests/infra

RUN chmod +x "./gunicorn.sh"
ENTRYPOINT ["./gunicorn.sh"]