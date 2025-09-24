# Basic Pipeline - Bioinformatics

Este repositorio contiene un pipeline básico en Python para trabajar con archivos FASTA como parte de la práctica del curso **Diseño de Pipelines Bioinformáticos Escalables, Automatización, Contenedores y Nube**.

---

## 📂 Estructura del proyecto

bio-nf-core/
└── workflows/
└── basic_pipeline/
├── script.py # Script en Python que analiza archivos FASTA
├── sample.fasta # Archivo de ejemplo en formato FASTA
└── README.md # Documentación del proyecto


---

## 🚀 Requisitos

- Python 3.8 o superior  
- Librería [Biopython](https://biopython.org/)

Instalar Biopython:

```bash
pip install biopython

python script.py

📊 Ejemplo de salida
✅ Archivo encontrado: G:\Mi unidad\Esp. Bioinformática\13- Diseño de Pipelines Bioinformáticos Escalables Automatización, Contenedores y Nube\bio-nf-core\workflows\basic_pipeline\sample.fasta

===== Resultados =====
Número de secuencias: 3
Longitud promedio: 14.67 nucleótidos