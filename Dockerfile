# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster as base
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

FROM base as test
RUN python tests/test0.py


FROM base as goodToGO
CMD [ "uvicorn", "app:app", "--reload", "--host=0.0.0.0"]

