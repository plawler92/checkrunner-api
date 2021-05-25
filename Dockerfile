# FROM python:3.8.9-slim-buster

# RUN apt-get update && apt-get install --no-install-recommends -y \
#   g++ \
#   unixodbc-dev \
#   && apt-get cleanLABEL Echo.TruckloadCapacity.ElasticsearchSync=true
FROM plawler92/pyodbc38:2.0.0

RUN mkdir /checks
COPY . /app
WORKDIR /app
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

# RUN chmod +x "./gunicorn.sh"
# ENTRYPOINT ["./gunicorn.sh"]
ENTRYPOINT [""]