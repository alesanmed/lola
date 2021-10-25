FROM python:3.9.6-slim-buster

WORKDIR /covid-dashboard

ADD requirements.txt /covid-dashboard

RUN pip install -r requirements.txt

ADD . /covid-dashboard

EXPOSE $PORT

CMD streamlit run --browser.serverAddress $SERVER_ADDRESS --browser.serverPort 443 --server.port $PORT --server.address 0.0.0.0 --server.headless true app/main.py
