FROM python:3.12

RUN pip install fluvio

COPY app.py app.py

CMD ["python", "./app.py"]