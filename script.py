# script.py - versión de prueba con prints de debug
from Bio import SeqIO
import os

# Ruta al archivo FASTA (relativa al script)
fasta_file = "sample.fasta"

# Debug: verificar que Python puede acceder al archivo
if os.path.exists(fasta_file):
    print("✅ Archivo encontrado:", fasta_file)
else:
    print("❌ Archivo NO encontrado:", fasta_file)
    exit(1)  # Salir si no encuentra el archivo

# Contador de secuencias y suma de longitudes
count = 0
total_length = 0

# Procesar cada secuencia del FASTA
for record in SeqIO.parse(fasta_file, "fasta"):
    print(f"Procesando: {record.id}, longitud: {len(record.seq)}")  # Debug
    count += 1
    total_length += len(record.seq)

# Calcular longitud promedio
if count > 0:
    avg_length = total_length / count
else:
    avg_length = 0

# Mostrar resultados finales
print("\n===== Resultados =====")
print(f"Número de secuencias: {count}")
print(f"Longitud promedio: {avg_length:.2f} nucleótidos")
