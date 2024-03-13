#!/bin/bash

# Construye la imagen Docker
docker build -t hola-mundo .

# Ejecuta el contenedor a partir de la imagen construida
docker run hola-mundo
