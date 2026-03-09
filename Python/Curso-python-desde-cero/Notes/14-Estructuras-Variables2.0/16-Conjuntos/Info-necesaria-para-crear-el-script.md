
# 🧩 1. `matplotlib` — la base para graficar en Python

`matplotlib` es una librería de visualización de datos.
Permite crear gráficos de líneas, barras, dispersión, tortas, etc.
Su módulo más usado es `matplotlib.pyplot`.

### Ejemplo básico:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 15]

plt.plot(x, y)
plt.title("Gráfico simple")
plt.show()
```

📌 **Claves de este módulo:**

* `plt.plot()` → genera el gráfico.
* `plt.title()` → agrega título.
* `plt.show()` → muestra la ventana con la figura.
* `plt.figure()` → crea una nueva figura (puedes tener varias a la vez).

💡 Cuando hagamos los diagramas de Venn, usaremos estas funciones para **crear y mostrar la figura base**.

---

# 🧮 2. `matplotlib_venn` — para crear los diagramas de Venn

Es un *submódulo externo* que extiende `matplotlib` y permite dibujar fácilmente diagramas de Venn de **2 o 3 conjuntos**.

Se importa así:

```python
from matplotlib_venn import venn2, venn3
```

---

## 🔹 Función `venn2(subsets, set_labels=None)`

Dibuja un **diagrama de 2 conjuntos**.

**Parámetros:**

* `subsets`: los conjuntos o tamaños de las áreas.
  Ejemplo:

  ```python
  venn2(subsets=(set_A, set_B))
  ```
* `set_labels`: nombres de los conjuntos.
  Ejemplo:

  ```python
  venn2(subsets=(A, B), set_labels=('A', 'B'))
  ```

---

## 🔹 Función `venn3(subsets, set_labels=None)`

Para **3 conjuntos (A, B, C)**.
Ejemplo:

```python
venn3(subsets=(A, B, C), set_labels=('A', 'B', 'C'))
```

📌 Puedes pasar directamente conjuntos de Python (`set()`) y la librería calculará las intersecciones automáticamente.

---

# 🎨 3. `plt.show()` — visualizar la figura

Una vez creas tu diagrama (con `venn2` o `venn3`), llamas a:

```python
plt.show()
```

Esto abre la ventana con el diagrama de Venn renderizado.

---

# 💡 4. Conceptos que combinaremos

Usaremos todo lo que ya dominas:

* **Entrada de datos (`input()`)** para que el usuario escriba los conjuntos.
* **Conversión de texto a listas o sets**.
* **Operaciones de conjuntos (`|`, `&`, `-`, `^`)**.
* **Visualización con `venn3`**.

---

# 🧠 5. Ejemplo conceptual de lo que haremos

Vamos a hacer un script que:

1. Pida al usuario los elementos de tres conjuntos A, B y C.
2. Convierta esas entradas en sets.
3. Muestre en pantalla:

   * Unión, intersección y diferencia.
   * Y **dibuje el diagrama de Venn correspondiente**.

---

# 🧩 6. Ejemplo rápido (sin interacción todavía)

```python
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

A = {1, 2, 3, 4}
B = {3, 4, 5}
C = {4, 5, 6}

venn3([A, B, C], ('A', 'B', 'C'))
plt.title("Diagrama de Venn de 3 conjuntos")
plt.show()
```

✅ Con eso ya tendrías una visualización gráfica con los colores y las áreas automáticas.

---
