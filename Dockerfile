FROM python:3.9-slim

WORKDIR /app

COPY hola_mundo.py .

EXPOSE 9000

CMD ["python", "hola_mundo.py"]
