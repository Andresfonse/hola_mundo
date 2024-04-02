# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo hola_mundo.py al directorio de trabajo en el contenedor
COPY hola_mundo.py /app

# Ejecuta el script cuando se inicie el contenedor
CMD ["python", "hola_mundo.py"]
