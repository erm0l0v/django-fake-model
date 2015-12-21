FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements-test.txt /usr/src/app/requirements-test.txt
RUN pip install -r requirements-test.txt

COPY . /usr/src/app

ENV TOX_ENV ${TOX_ENV:-py35-dj19-sqlite-unittest}
RUN tox -e $TOX_ENV --notest

CMD coverage run --source django_fake_model runtests.py
