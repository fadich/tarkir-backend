FROM python:3.9

ENV TR_API_SERVER_PORT 5000

WORKDIR /tarkir-tools

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN pip install -e .

EXPOSE ${TR_API_SERVER_PORT}
