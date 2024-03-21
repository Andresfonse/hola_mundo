FROM python:3.9

WORKDIR /app

# Instalación de git
RUN apt-get update && apt-get install -y git

# Clonar el repositorio desde GitHub
RUN git clone https://github.com/tu_usuario/tu_repositorio.git .


# Comando para ejecutar la aplicación
CMD ["python", "hola_mundo.py"]
