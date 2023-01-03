FROM python:3.8

RUN pip install bs4

RUN pip install requests

RUN pip install lxml

COPY bayutblog.csv /app/

COPY app.py /app/

CMD ["python", "/app/app.py"]
