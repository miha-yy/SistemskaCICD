FROM python:3.7

ADD . /sistemska

WORKDIR /sistemska

RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]