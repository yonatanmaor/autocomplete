FROM ubuntu:latest

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3.10 && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /app/src

EXPOSE 5000

CMD ["python3", "src/rest_modules/rest_main.py"]
