FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get -y install apt-utils libpq-dev python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000


