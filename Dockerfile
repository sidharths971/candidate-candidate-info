FROM ubuntu
RUN apt-get -y update \
    && apt-get -y install python3 \
    && apt-get -y install python3-pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["app.py"]

