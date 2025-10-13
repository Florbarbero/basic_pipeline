# Dockerfile - Ubuntu + Python + Biopython
FROM ubuntu:24.04

# Evitar preguntas interactivas al instalar paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar repositorios e instalar Python3 y pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto dentro del contenedor
COPY requirements.txt .
COPY script.py .
COPY sample.fasta .

# Instalar dependencias de Python (forzando instalación con pip)
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Comando por defecto al ejecutar el contenedor
CMD ["python3", "script.py"]
