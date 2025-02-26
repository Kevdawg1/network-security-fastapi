FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN apt update -y && apt install -y awscli -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python", "app.py"]