
# 🧩 **Listas en Python (`list`)**

## 📘 ¿Qué es una lista?

* Es una **colección ordenada y modificable** de elementos.
* Puede contener **diferentes tipos de datos** (enteros, cadenas, booleanos, etc.).
* Es el equivalente a un **array** en otros lenguajes.
* Los elementos están **indexados desde 0** hasta *n – 1*.

---

## 🧱 **Declaración y definición**

```python
# Lista con distintos tipos de datos
name_list = ["elemento 0", 5, True, 'item 3']

# Crear una lista vacía
lista_vacia = list()
```

---

## 🎯 **Acceder a los elementos**

```python
posicion = 2
print(name_list[posicion])  # True

# Acceso directo
print(name_list[0])   # "elemento 0"
print(name_list[-1])  # "item 3" → índice negativo accede desde el final
```

---

## 🔁 **Modificar elementos**

```python
name_list[1] = 10
print(name_list)  # ['elemento 0', 10, True, 'item 3']
```

---

## ➕ **Agregar elementos**

### `append()`

Agrega **un elemento** al final de la lista.

```python
lista = ["A", "B"]
lista.append("C")
print(lista)  # ['A', 'B', 'C']
```

### `insert()`

Agrega un elemento en un **índice específico**.

```python
lista.insert(1, "X")
print(lista)  # ['A', 'X', 'B', 'C']
```

### `extend()`

Agrega **múltiples elementos** (otra lista o iterable).

```python
lista.extend(["D", "E", "F"])
print(lista)  # ['A', 'X', 'B', 'C', 'D', 'E', 'F']
```

💡 `append()` agrega un solo valor; `extend()` agrega cada elemento de la lista pasada.

---

## ➖ **Eliminar elementos**

### `pop()`

Elimina un elemento por **índice** y lo **devuelve**.

* Si no se indica índice, elimina el **último elemento**.
* Si se usa un índice negativo, elimina desde el final.

```python
elemento = lista.pop(0)  # Elimina el primero
print(elemento)  # 'A'
```

### `remove()`

Elimina un elemento por **valor**.

```python
lista.remove("B")
```

> ⚠️ Lanza un error si el valor no existe.

### `clear()`

Elimina **todos los elementos** de la lista.

```python
lista.clear()
```

---

## 📏 **Ordenar y reordenar**

### `sort()`

Ordena la lista en **orden ascendente**.
Solo funciona si los elementos son **comparables** (por ejemplo, todos números o todos strings).

```python
numeros = [5, 1, 7, 3]
numeros.sort()
print(numeros)  # [1, 3, 5, 7]
```

### `sort(reverse=True)`

Ordena la lista en **orden descendente**.

```python
numeros.sort(reverse=True)
print(numeros)  # [7, 5, 3, 1]
```

### `reverse()`

Invierte el orden actual de la lista, **sin ordenarla**.

```python
numeros.reverse()
print(numeros)  # [1, 3, 5, 7] → pasa a [7, 5, 3, 1]
```

---

## 📊 **Funciones y métodos útiles**

| Método / función | Descripción                         | Ejemplo                 |
| ---------------- | ----------------------------------- | ----------------------- |
| `len(lista)`     | Devuelve el número de elementos.    | `len(lista)`            |
| `lista.count(x)` | Cuenta cuántas veces aparece *x*.   | `lista.count(2)`        |
| `lista.index(x)` | Devuelve la posición del valor *x*. | `lista.index('item 3')` |
| `lista.copy()`   | Devuelve una copia de la lista.     | `copia = lista.copy()`  |

---

## 🧮 **Concatenar y combinar listas**

```python
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c)  # [1, 2, 3, 4, 5]
```

O usando `extend()`:

```python
a.extend(b)
print(a)  # [1, 2, 3, 4, 5]
```

---

## 🧩 **Listas anidadas**

```python
lista_anidada = [[1, 2], [3, 4]]
print(lista_anidada[1][0])  # 3
```

---

## 💡 **Comprensiones de listas**

Forma compacta de generar listas con bucles y condiciones.

```python
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]
```

También se pueden usar condiciones:

```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

## 🧠 **Resumen general**

* `append()`, `insert()`, `extend()` → agregar elementos.
* `pop()`, `remove()`, `clear()` → eliminar elementos.
* `sort()` y `reverse()` → ordenar o invertir.
* `count()`, `index()`, `len()` → obtener información.
* Las listas son **mutables**, **ordenadas** y pueden contener **tipos mixtos**.
* Permiten **anidación** y **comprensiones** para crear listas dinámicas.
* Soportan **índices positivos y negativos**.
* Se pueden **anidar, ordenar, copiar y recorrer** fácilmente.

---
