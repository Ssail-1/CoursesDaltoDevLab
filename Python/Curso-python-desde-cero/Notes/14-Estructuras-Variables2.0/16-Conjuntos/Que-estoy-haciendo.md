
## 🧭 Objetivo

Crear un **entorno virtual limpio** solo para probar y ejecutar el ejemplo del diagrama de Venn,
sin afectar otros proyectos ni entorno global.

---

## 📂 Estructura

1. Creamos estructura que contendra entorno
2. Creamos carpeta que tendra la **demostración en diagramas de venn python**.

```py
16-Conjuntos/
│
├── venn_demo/
│   ├── venv/    ← entorno virtual (se creará aquí)
│   ├── venn_diagram.py    ← script que haremos
│
└── 16-Conjuntos.md
```

---

## ⚙️ Pasos en VM (Ubuntu)

Desde la terminal, dentro del proyecto:

```bash
cd ~/GitHubDir/CoursesDaltoDevLab/Notes/Estructuras-Variables2.0/16-Conjuntos
mkdir venn_demo
cd venn_demo
```

### 1️⃣ Crear entorno virtual

```zsh
python -m venv EntornoDiagramasVenn
```

Esto creará una carpeta llamada `EntornoDiagramasVenn` (será el entorno aislado).

---

### 2️⃣ Activar el entorno

```bash
source EntornoDiagramasVenn/bin/activate
```

Verás algo como:

```
(venv) tuUser@NombreDeTuHostOVM:~/GitHubDir/...
```

✅ Eso significa que ya estás dentro del entorno virtual.

---

### 3️⃣ Instalar dependencias necesarias

```zsh
pip install matplotlib matplotlib-venn
```

Puedes comprobar que se instalaron correctamente con:

```zsh
pip list
```

---

### 4️⃣ Crear el archivo del script

```zsh
touch conjuntosDiagramasVenn.py
```

Aqui realizaremos el codigo donde mostraremos como funcionan los conjuntos en diagramas de Venn.

---
