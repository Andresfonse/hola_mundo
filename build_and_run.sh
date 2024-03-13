#!/bin/bash

# Verifica si el contenedor Docker ya existe y lo elimina si es así
if [ "$(docker ps -q -f name=hola-mundo-container)" ]; then
    docker stop hola-mundo-container
    docker rm hola-mundo-container
fi

# Construye la imagen Docker
docker build -t hola-mundo .

# Ejecuta el contenedor a partir de la imagen construida en el puerto 9000
docker run -d -p 5000:5000 --name hola-mundo-container hola-mundo
