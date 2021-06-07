FROM python:3.8-slim-buster

WORKDIR /app

COPY simple.py simple.py

CMD [ "python3", "-u", "simple.py" ]
