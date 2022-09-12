FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN pip3 install -U pip
COPY . /aditya/
WORKDIR /aditya/
RUN pip3 install -r requirements.txt
CMD python3 -m bot
