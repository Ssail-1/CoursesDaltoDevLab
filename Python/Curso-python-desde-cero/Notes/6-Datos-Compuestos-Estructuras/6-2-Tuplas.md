
# 🧩 **Tuplas en Python (`tuple`)**

En proyectos reales las tuplas se usan para estructuras inmutables, retorno de funciones, y empaquetado/desempaquetado de datos.

## 📘 ¿Qué es una tupla?

* Es una **colección ordenada e inmutable** de elementos.
* Una vez creada, **no se puede modificar** (no se pueden agregar, eliminar ni cambiar elementos).
* Se usa para **mantener datos que no deben cambiar** durante la ejecución del programa.
* Se definen con **paréntesis `()`**.

---

## 🧱 **Declaración y definición**

```python
# Tupla con distintos tipos de datos
mi_tupla = ("Python", 3.14, True, 42)
```

* El tipo de dato es **`tuple`**.
* Se pueden incluir valores de distintos tipos.
* Si solo tiene **un elemento**, debe terminar con una **coma** para que Python la reconozca como tupla:

```python
una_tupla = (5,)   # ✅ tupla
no_es_tupla = (5)  # ❌ esto es un entero
```

---

## 🎯 **Acceder a los elementos**

Se accede igual que en las listas: con corchetes `[]` e índices.

```python
print(mi_tupla[0])   # Python
print(mi_tupla[-1])  # 42
```

---

## 🔄 **Desempaquetar una tupla**

Permite asignar los valores de una tupla a variables individuales.

```python
persona = ("Luis", 25, "México")
nombre, edad, pais = persona

print(nombre)  # Luis
print(edad)    # 21
print(pais)    # México
```

💡 También puedes usar el operador `*` para capturar varios valores:

```python
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]
```

---

## ⚙️ **Funciones y operaciones útiles**

| Operación / función | Descripción                              | Ejemplo                           |
| ------------------- | ---------------------------------------- | --------------------------------- |
| `len(tupla)`        | Devuelve la cantidad de elementos.       | `len(mi_tupla)`                   |
| `tupla.count(x)`    | Cuenta cuántas veces aparece *x*.        | `mi_tupla.count(True)`            |
| `tupla.index(x)`    | Devuelve la posición de *x*.             | `mi_tupla.index(42)`              |
| `x in tupla`        | Verifica si *x* está dentro de la tupla. | `"Python" in mi_tupla`            |
| `tupla + tupla2`    | Concatena dos tuplas.                    | `(1, 2) + (3, 4)`                 |
| `tupla * n`         | Repite la tupla *n* veces.               | `(1, 2) * 3 → (1, 2, 1, 2, 1, 2)` |

---

## 🧮 **Conversión entre lista y tupla**

Aunque una tupla no se puede modificar directamente, puedes **convertirla a lista**, modificarla y volver a convertirla:

```python
mi_tupla = (1, 2, 3)
lista = list(mi_tupla)
lista.append(4)
mi_tupla = tuple(lista)

print(mi_tupla)  # (1, 2, 3, 4)
```

---

## 💡 **Cuándo usar tuplas**

* Cuando necesitas **datos constantes** (por ejemplo, coordenadas, configuraciones, días de la semana…).
* Cuando quieres **mayor rendimiento**, ya que las tuplas consumen menos memoria y son más rápidas que las listas.
* Como **clave de diccionario**, ya que son inmutables (las listas no pueden usarse como clave).

---

## 🧠 **Resumen**

* Las tuplas son **inmutables** y **ordenadas**.
* Se definen con `()`, mientras que las listas usan `[]`.
* Son más ligeras y seguras para datos fijos.
* Soportan desempaquetado, comparación y operaciones básicas de conteo y búsqueda.

---
