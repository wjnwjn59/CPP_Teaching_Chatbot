FROM nvidia/cuda:10.1-devel-ubuntu18.04
FROM tensorflow/tensorflow:2.3.2-gpu

WORKDIR /app

COPY . .

RUN pip3 install rasa[full]==2.2.2

EXPOSE 5005

