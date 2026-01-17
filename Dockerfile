FROM python:3.12-alpine

WORKDIR /CreateFiles

COPY . .

CMD ["python", "Createfolders.py"]