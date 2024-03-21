#!/bin/bash

# Clonar el repositorio desde GitHub
git clone https://github.com/tu_usuario/tu_repositorio.git /ruta/a/tu/proyecto

# Navegar al directorio del proyecto
cd /ruta/a/tu/proyecto

# Construir la imagen Docker
docker build -t tilinrunning .

# Ejecutar el contenedor Docker
docker run -d -p 8080:8080 tilinrunning
