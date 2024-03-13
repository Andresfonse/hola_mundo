FROM python:3.9-slim

WORKDIR /app

COPY hola_mundo.py .

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["python", "hola_mundo.py"]
