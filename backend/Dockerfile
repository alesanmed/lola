FROM python:3.9.6-slim-buster

RUN apt-get update
RUN apt-get install -y ffmpeg

RUN apt-get clean autoclean
RUN apt-get autoremove --yes
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /lola-back

ADD requirements.txt /lola-back

RUN pip install -r requirements.txt

ADD . /lola-back

EXPOSE $PORT

ENV FLASK_APP=lola-backend
ENV FLASK_ENV=production

CMD gunicorn --bind 0.0.0.0:$PORT --access-logfile - --log-level debug lola-backend.wsgi:app
