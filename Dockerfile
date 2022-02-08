FROM python:3.10
WORKDIR /application
COPY app.py .
COPY data/* ./data/
CMD python /application/app.py