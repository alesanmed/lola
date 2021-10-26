FROM python:3.9.6-slim-buster

WORKDIR /lola-dashboard

ADD requirements.txt /lola-dashboard

RUN pip install -r requirements.txt

ADD . /lola-dashboard

EXPOSE $PORT

CMD streamlit run --browser.serverAddress $SERVER_ADDRESS --browser.serverPort 443 --server.port $PORT --server.address 0.0.0.0 --server.headless true app/main.py
