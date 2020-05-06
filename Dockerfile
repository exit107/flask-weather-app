FROM python:3.6

MAINTAINER David Brown "dave.brown@exit107.com"

RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY src /src/

EXPOSE 5000

WORKDIR /src

ENTRYPOINT ["./gunicorn.sh"]
