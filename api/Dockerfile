FROM python:3.9

RUN mkdir /code

COPY . /code

WORKDIR /code

ENV FLASK_APP=/code/api/app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install -r requirements.txt

CMD ["flask", "run"]
