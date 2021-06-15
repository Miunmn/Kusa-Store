FROM python:latest

ADD ./app /home/app/
WORKDIR /home/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]