FROM ubuntu:latest

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3.10 && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 download_nltk_requirements.py

ENV PYTHONPATH /app/src

EXPOSE 1188

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:1188", "wsgi:app"]
