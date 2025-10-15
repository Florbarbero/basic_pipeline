🧬 README.md — Basic Pipeline (versión Docker)
# 🧬 Basic Pipeline - Bioinformatics (Docker version)

Este proyecto implementa un **pipeline básico en Python** para procesar archivos FASTA, ejecutado dentro de un **contenedor Docker**.  
Forma parte del curso **Diseño de Pipelines Bioinformáticos Escalables, Automatización, Contenedores y Nube**.

---

## 📁 Estructura del proyecto



C:\docker\basic_pipeline
│
├── Dockerfile # Define cómo se construye la imagen del contenedor
├── script.py # Script principal en Python
├── sample.fasta # Archivo FASTA de ejemplo
└── README.md # Este archivo


---

## 🐳 1. Construcción de la imagen Docker

Desde una terminal PowerShell ubicada en la carpeta del proyecto (`C:\docker\basic_pipeline`), ejecutar:

```bash
docker build -t basic-pipeline .

🔍 Explicación del comando:

docker build: crea una imagen a partir de un archivo Dockerfile.

-t basic-pipeline: asigna el nombre (tag) basic-pipeline a la imagen.

. indica que el contexto de construcción es la carpeta actual (donde está el Dockerfile).

📦 2. Estructura del Dockerfile

Ejemplo de Dockerfile usado:

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


🧠 3. Ejecutar el contenedor

Para correr el análisis dentro de Docker y montar el sistema de archivos local, ejecutar:

docker run --rm -v "C:\docker\basic_pipeline":/app basic-pipeline

🧩 Explicación del comando:

docker run: ejecuta un contenedor basado en una imagen.

--rm: elimina el contenedor automáticamente al finalizar (para no dejar residuos).

-v "C:\docker\basic_pipeline":/app → monta tu carpeta local en la ruta /app dentro del contenedor.
Esto permite acceder al script.py y sample.fasta sin copiarlos dentro de la imagen.

basic-pipeline → es el nombre de la imagen creada con el paso anterior.

🧪 4. Ejemplo de salida
✅ Archivo encontrado: sample.fasta
Procesando: seq1, longitud: 10
Procesando: seq2, longitud: 15
Procesando: seq3, longitud: 19

===== Resultados =====
Número de secuencias: 3
Longitud promedio: 14.67 nucleótidos

🧬 5. Explicación del script en Python (script.py)
from Bio import SeqIO
import os

# Archivo FASTA de entrada
fasta_file = "sample.fasta"

# Verifica que el archivo exista
if os.path.exists(fasta_file):
    print("✅ Archivo encontrado:", fasta_file)
else:
    print("❌ Archivo NO encontrado:", fasta_file)
    exit(1)

# Inicializa contadores
count = 0
total_length = 0

# Recorre las secuencias del archivo FASTA
for record in SeqIO.parse(fasta_file, "fasta"):
    print(f"Procesando: {record.id}, longitud: {len(record.seq)}")
    count += 1
    total_length += len(record.seq)

# Calcula la longitud promedio
avg_length = total_length / count if count > 0 else 0

# Muestra los resultados
print("\n===== Resultados =====")
print(f"Número de secuencias: {count}")
print(f"Longitud promedio: {avg_length:.2f} nucleótidos")

🔍 Qué hace:

Usa Biopython para leer el archivo FASTA.

Verifica si el archivo existe.

Recorre cada secuencia y calcula su longitud.

Muestra el número total de secuencias y la longitud promedio.

🧾 6. Resumen del flujo completo

Se construye la imagen con docker build -t basic-pipeline .

Se ejecuta el contenedor con docker run --rm -v "C:\docker\basic_pipeline":/app basic-pipeline

El contenedor corre el script en Python dentro de /app.

El script lee sample.fasta, procesa las secuencias y muestra resultados.

El contenedor se elimina automáticamente al terminar (--rm).