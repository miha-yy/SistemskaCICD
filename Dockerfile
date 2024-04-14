FROM python:3.7

ADD . /sysa

WORKDIR /sysa

RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]