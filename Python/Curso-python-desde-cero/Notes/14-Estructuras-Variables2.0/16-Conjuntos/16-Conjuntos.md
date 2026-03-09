
# 🟢 **Conjuntos en Python (`set`)**

## 📘 **¿Qué es un conjunto?**

Un **conjunto** es una colección **no ordenada** y **sin elementos duplicados**.
Está inspirado directamente en la **teoría de conjuntos** de las matemáticas.

```python
conjunto = {"Python", "Java", "C++"}
```

📌 **Características clave:**

* No tiene índices → no puedes acceder con `conjunto[0]`.
* No mantiene orden → los elementos pueden aparecer en distinto orden cada vez.
* No permite valores repetidos.
* Solo puede contener **elementos inmutables** (como `int`, `str`, `tuple`, `frozenset`).

---

## 🧩 **Formas de crear conjuntos**

### 1. Con llaves `{}`

```python
conjunto = {"dato1", "dato2", "dato3"}
```

### 2. Con la función `set()`

Útil cuando partes de un iterable:

```python
conjunto = set(["dato1", "dato2", "dato3"])
```

> ❗Si pasas un string a `set("Python")`, obtendrás un conjunto de caracteres únicos:
> `{'P', 'y', 't', 'h', 'o', 'n'}`

---

## 🔒 **Elementos inmutables dentro de un set**

Si quieres incluir una estructura modificable (como otro conjunto), debes usar `frozenset()`.

```python
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}  # ✅ válido
```

> 🔹 `frozenset` es una versión **inmutable** de un set (no se puede modificar).

---

## ⚙️ **Métodos y operaciones comunes**

| Operación            | Método / Símbolo                      | Descripción                                       |
| -------------------- | ------------------------------------- | ------------------------------------------------- |
| Unión                | `A.union(B)` ó `A \| B`               | Elementos que están en A o en B                   |
| Intersección         | `A.intersection(B)` ó `A & B`         | Elementos comunes a A y B                         |
| Diferencia           | `A.difference(B)` ó `A - B`           | Elementos en A pero no en B                       |
| Diferencia simétrica | `A.symmetric_difference(B)` ó `A ^ B` | Elementos que están en A o en B, pero no en ambos |
| Subconjunto          | `A.issubset(B)` ó `A <= B`            | A está contenido en B                             |
| Superconjunto        | `A.issuperset(B)` ó `A >= B`          | B está contenido en A                             |
| Disjuntos            | `A.isdisjoint(B)`                     | A y B no tienen elementos en común                |

---

## 🧮 **Ejemplo práctico**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Unión:", A | B)
print("Intersección:", A & B)
print("Diferencia:", A - B)
print("Dif. Simétrica:", A ^ B)
```

📤 **Salida:**

```py
Unión: {1, 2, 3, 4, 5, 6}
Intersección: {3, 4}
Diferencia: {1, 2}
Dif. Simétrica: {1, 2, 5, 6}
```

---

## 🧠 **Visualización conceptual (tipo diagrama de Venn)**

Para visualizar las relaciones:

```py
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

```py
   A ∪ B = {1, 2, 3, 4, 5, 6}   → Todo lo que pertenece a A o B
   A ∩ B = {3, 4}               → Elementos comunes
   A - B = {1, 2}               → Elementos solo en A
   B - A = {5, 6}               → Elementos solo en B
   A △ B = {1, 2, 5, 6}         → Elementos diferentes entre A y B
```

📍 Esto corresponde exactamente a las áreas del diagrama de Venn de dos conjuntos.

---

## 🔁 **Comparaciones entre conjuntos**

### Subconjunto y superconjunto

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True
```

### Conjuntos disjuntos

```python
X = {10, 20, 30}
Y = {40, 50}
print(X.isdisjoint(Y))  # True
```

---

## 🧹 **Modificar conjuntos**

### Agregar elementos

```python
A = {1, 2, 3}
A.add(4)
print(A)  # {1, 2, 3, 4}
```

### Eliminar elementos

```python
A.remove(2)   # Elimina 2, lanza error si no existe
A.discard(10) # Elimina 10 si existe, no lanza error
A.pop()       # Elimina un elemento aleatorio
A.clear()     # Vacía el conjunto
```

---

## ⚠️ **Atención a estos puntos**

| Situación            | Explicación                                 |
| -------------------- | ------------------------------------------- |
| 🔸 No hay índices    | No se puede acceder con `A[0]`.             |
| 🔸 No hay duplicados | Si agregas un elemento repetido, se ignora. |
| 🔸 No es ordenado    | El orden de impresión puede cambiar.        |

---

## 🔄 **Conversión entre tipos**

```python
lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista)
print(conjunto)  # {1, 2, 3, 4, 5}

# De set a lista
lista_unica = list(conjunto)
print(lista_unica)
```

💡 *Útil para eliminar duplicados de una lista.*

---

## 🧠 **Resumen**

| Concepto             | Símbolo           | Descripción                |                    |
| -------------------- | ----------------- | -------------------------- | ------------------ |
| Unión                | `A                | B`                         | Elementos en A o B |
| Intersección         | `A & B`           | Elementos comunes          |                    |
| Diferencia           | `A - B`           | Solo en A                  |                    |
| Diferencia simétrica | `A ^ B`           | En A o B, pero no en ambos |                    |
| Subconjunto          | `A <= B`          | A está dentro de B         |                    |
| Disjuntos            | `A.isdisjoint(B)` | Sin elementos comunes      |                    |

---

## 💬 **Conclusión**

Los **sets** en Python son una herramienta poderosa para:

* Eliminar duplicados.
* Hacer operaciones matemáticas de conjuntos.
* Comparar colecciones de datos rápidamente.

Y si vienes de **matemáticas discretas**, los vas a amar: cada propiedad que aprendiste allí está viva aquí, lista para ser usada en código. ⚡

---
