FROM python:3.10.5-slim-buster as base

# This flag is important to output python logs correctly in docker!
ENV PYTHONUNBUFFERED 1
# Flag to optimize container size a bit by removing runtime python cache
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code

COPY . .

RUN apt-get update && apt-get install -y curl

RUN pip3 install -r requirements.txt

CMD  python app.py