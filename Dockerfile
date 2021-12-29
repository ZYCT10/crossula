FROM ubuntu:latest
LABEL author="Fiatum Group"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 20002
ENV authKey="75abe41cf49bba6c865482a07368d845"
ENV clientId="a2c660dd-13a5-4760-9ce1-385471918067"
ENTRYPOINT ["python3", "app.py"]