FROM python:3.9

WORKDIR /app

# Copiar el script Python y el archivo HTML al directorio de trabajo del contenedor
COPY hola_mundo.py .
COPY hola_mundo.html .

# Comando para ejecutar el script Python y servir el archivo HTML
CMD ["python", "hola_mundo.py"]
