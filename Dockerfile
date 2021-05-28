FROM python:3.8.9-slim-buster
# FROM plawler92/pyodbc38:2.0.0

RUN apt-get update && apt-get install --no-install-recommends -y \
  g++ \
  unixodbc-dev \
  gnupg \ 
  curl

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

#Debian 10
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

RUN mkdir /checks
COPY . /app
WORKDIR /app
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

RUN chmod +x "./gunicorn.sh"
ENTRYPOINT ["./gunicorn.sh"]
#ENTRYPOINT [""]