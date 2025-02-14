FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install -y awscli -y

RUN apt -get update && pip install -r requirements.txt
CMD ["python", "app.py"]