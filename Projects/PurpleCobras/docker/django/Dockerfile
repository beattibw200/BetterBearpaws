# Base image
FROM python:latest
# update pip
ENV PYTHONUNBUFFERED=1
RUN pip3 install --upgrade pip & \
  pip3 install django mysqlclient
ENV MYSQL_MAJOR 8.0
RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys 8C718D3B5072E1F5 & \
  echo "deb http://repo.mysql.com/apt/debian/ buster mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list & apt-get update & \
  apt-get -y --no-install-recommends install default-libmysqlclient-dev
WORKDIR /src
