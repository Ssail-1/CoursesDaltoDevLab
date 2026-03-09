
# **Conjuntos (`set`)**

## 📘 ¿Qué es un conjunto?

* Es una **colección no ordenada** y **sin elementos duplicados**.
* Se define con **llaves `{}`** o con el constructor `set()`.
* No permite acceder por índice (no hay posiciones como en listas o tuplas).
* Es útil para **eliminar duplicados, hacer operaciones matemáticas** (unión, intersección, diferencia) o comprobar pertenencia rápida.

---

## 🧱 **Declaración y definición**

```python
# Conjunto con elementos únicos
mi_set = {1, 2, 3, 4}

# También puedes crear un conjunto vacío así:
mi_set_vacio = set()
```

> [!IMPORTANT]
> ⚠️ `{}` por sí solo crea un **diccionario**, no un conjunto.

---

## 🎯 **Propiedades importantes**

* Los elementos **no tienen orden** → no puedes hacer `mi_set[0]`.
* No se pueden repetir → los duplicados se eliminan automáticamente.
* Los elementos deben ser **inmutables** (por ejemplo, puedes guardar una tupla, pero no una lista).

```python
duplicados = {1, 2, 2, 3, 3, 4}
print(duplicados)  # {1, 2, 3, 4}
```

---

## ⚙️ **Operaciones básicas**

```python
numeros = {1, 2, 3}
numeros.add(4)       # Agregar un elemento
numeros.remove(2)    # Eliminar un elemento
numeros.discard(5)   # Elimina sin error si no existe
numeros.clear()      # Vacía el conjunto
```

---

## 🔢 **Funciones útiles**

| Función / método | Descripción                                     | Ejemplo                  |
| ---------------- | ----------------------------------------------- | ------------------------ |
| `len(set)`       | Número de elementos.                            | `len(numeros)`           |
| `x in set`       | Comprueba si un valor pertenece.                | `3 in numeros`           |
| `set.add(x)`     | Agrega un elemento.                             | `numeros.add(5)`         |
| `set.remove(x)`  | Elimina un elemento (lanza error si no existe). | `numeros.remove(2)`      |
| `set.discard(x)` | Elimina un elemento (sin error).                | `numeros.discard(2)`     |
| `set.pop()`      | Elimina y devuelve un elemento aleatorio.       | `numeros.pop()`          |
| `set.copy()`     | Crea una copia del conjunto.                    | `copia = numeros.copy()` |

---

## 🧮 **Operaciones entre conjuntos (teoría de conjuntos)**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unión (todos los elementos)
print(a | b)   # {1, 2, 3, 4, 5, 6}

# Intersección (comunes)
print(a & b)   # {3, 4}

# Diferencia (solo en a)
print(a - b)   # {1, 2}

# Diferencia simétrica (no comunes)
print(a ^ b)   # {1, 2, 5, 6}
```

---

## 🧠 **Resumen**

* No hay índices, ni orden, ni duplicados.
* Muy útil para **comparar, filtrar o validar datos únicos**.
* Soporta **operaciones matemáticas** de conjuntos.
* Es **mutable**, pero sus elementos deben ser **inmutables**.

---

## 🔄 **Comparación con estructuras clásicas (Java y Estructura de Datos)**

| Concepto clásico       | Equivalente o relación en Python                   | Descripción breve                                                           |
| ---------------------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| **Pila (Stack)**       | `list` usando `append()` y `pop()`                 | LIFO (último en entrar, primero en salir).                                  |
| **Cola (Queue)**       | `collections.deque`                                | FIFO (primero en entrar, primero en salir).                                 |
| **Conjunto (Set)**     | `set` nativo de Python                             | Estructura sin duplicados, como un *HashSet* en Java.                       |
| **Mapa / Diccionario** | `dict`                                             | Pares clave-valor, similar a *HashMap* en Java.                             |
| **Lista Enlazada**     | No existe nativa, se puede implementar con clases. | Pero las listas (`list`) internamente se comportan como *arrays dinámicos*. |

> [!NOTE]
>💬 En Java tú **creas la estructura** (definiendo nodos, punteros, clases…),
en Python **ya están listas**, lo importante es que entender *qué comportamiento modelan*: pila, cola, conjunto, etc.
Así puedes trasladar ese conocimiento entre lenguajes sin confundir conceptos.

---
