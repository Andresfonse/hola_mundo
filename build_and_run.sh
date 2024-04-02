#!/bin/bash

# Clonar el repositorio desde GitHub
git clone https://github.com/Andresfonse/hola_mundo.git

# Navegar al directorio del proyecto
cd /

# Construir la imagen Docker
docker build -t tilinrunning .

# Ejecutar el contenedor Docker
docker run -d -p 6336:6336 tilinrunning
