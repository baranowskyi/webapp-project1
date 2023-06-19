FROM python:3.11-alpine3.18

COPY requirements.txt /temp/requirements.txt 

RUN python -m venv .venv
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /temp/requirements.txt

COPY webapp /webapp
WORKDIR /webapp

RUN adduser -D webapp-user
USER webapp-user

EXPOSE 8000