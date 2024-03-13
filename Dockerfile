# Dockerfile

# Utiliza la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo hola_mundo.py al directorio de trabajo en el contenedor
COPY hola_mundo.py .

# Ejecuta el script hola_mundo.py cuando el contenedor se inicie
CMD ["python", "hola_mundo.py"]
