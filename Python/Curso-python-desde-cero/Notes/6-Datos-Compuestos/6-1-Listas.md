
# **Listas en Python (`list`)**

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
```

* El tipo de dato es **`list`**.
* Se define con **corchetes `[]`**.
* Los elementos se separan por comas.

---

## 🎯 **Acceder a los elementos**

```python
posicion = 2
print(name_list[posicion])  # True
```

También puedes acceder directamente:

```python
print(name_list[0])   # "elemento 0"
print(name_list[-1])  # 'item 3' → índice negativo accede desde el final
```

---

## 🔁 **Modificar elementos**

```python
name_list[1] = 10
print(name_list)  # ['elemento 0', 10, True, 'item 3']
```

---

## ➕ **Agregar y eliminar elementos**

```python
# Agregar al final
name_list.append("nuevo")

# Insertar en una posición específica
name_list.insert(1, "insertado")

# Eliminar por valor
name_list.remove(True)

# Eliminar por posición
name_list.pop(0)     # Elimina el primer elemento
# o
del name_list[0]     # Otra forma de eliminar por índice

# Vaciar toda la lista
name_list.clear()
```

---

## 📏 **Funciones y métodos útiles**

| Método / función     | Descripción                                          | Ejemplo                         |
| -------------------- | ---------------------------------------------------- | ------------------------------- |
| `len(lista)`         | Devuelve la cantidad de elementos.                   | `len(name_list)`                |
| `lista.append(x)`    | Agrega un elemento al final.                         | `name_list.append(7)`           |
| `lista.insert(i, x)` | Inserta un elemento en la posición *i*.              | `name_list.insert(0, 'inicio')` |
| `lista.remove(x)`    | Elimina el primer elemento igual a *x*.              | `name_list.remove('item 3')`    |
| `lista.pop(i)`       | Elimina y devuelve el elemento en *i*.               | `name_list.pop(1)`              |
| `lista.sort()`       | Ordena la lista (solo si los datos son comparables). | `numeros.sort()`                |
| `lista.reverse()`    | Invierte el orden de los elementos.                  | `numeros.reverse()`             |
| `lista.count(x)`     | Cuenta cuántas veces aparece *x*.                    | `name_list.count('item 3')`     |
| `lista.index(x)`     | Devuelve la posición de *x*.                         | `name_list.index('item 3')`     |
| `lista.copy()`       | Crea una copia de la lista.                          | `copia = name_list.copy()`      |

---

## ⚙️ **Concatenar y combinar listas**

```python
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c)  # [1, 2, 3, 4, 5]
```

También puedes usar *extend*:

```python
a.extend(b)
print(a)  # [1, 2, 3, 4, 5]
```

---

## 🧮 **Listas anidadas**

```python
lista_anidada = [[1, 2], [3, 4]]
print(lista_anidada[1][0])  # 3
```

---

## 💡 **Comprensiones de listas**

Forma compacta de generar listas a partir de iteraciones:

```python
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]
```

---

## 🧠 **Resumen**

* Las listas son **mutables** (se pueden modificar).
* Pueden almacenar **tipos mixtos** de datos.
* Soportan **índices positivos y negativos**.
* Se pueden **anidar, ordenar, copiar y recorrer** fácilmente.

---

¿Quieres que el siguiente tema que preparemos sea **tuplas (`tuple`)** o prefieres que sigamos con **listas anidadas y comprensión de listas avanzada** (como condicionales dentro del `for`)?
Así voy adaptando el siguiente bloque de notas al ritmo del curso que estás siguiendo.
