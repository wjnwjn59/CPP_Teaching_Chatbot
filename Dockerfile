FROM ubuntu:20.04
ENTRYPOINT []
COPY requirements.txt /app/
WORKDIR /app
RUN apt-get update && apt-get install -y apt-utils curl python3 python3-pip && python3 -m pip install --upgrade pip && pip3 install rasa==2.0.0
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh 