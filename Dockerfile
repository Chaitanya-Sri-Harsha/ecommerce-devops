FROM python:3.9-slim
WORKDIR /ecommerce
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
CMD ["python", "main.py"]
