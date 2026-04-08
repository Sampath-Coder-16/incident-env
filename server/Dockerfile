FROM python:3.9

WORKDIR /app

COPY server/requirements.txt .
RUN pip install -r requirements.txt

COPY server/ .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]