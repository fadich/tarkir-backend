FROM python:3.9

ENV TK_API_SERVER_PORT 5000

WORKDIR /tarkir-tools

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE ${TK_API_SERVER_PORT}

CMD ["./entrypoint.sh"]
