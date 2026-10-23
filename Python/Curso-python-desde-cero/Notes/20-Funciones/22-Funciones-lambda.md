
# ⚡ Funciones `lambda`

Las funciones `lambda` son una forma de crear **funciones anónimas** (sin nombre).

Son similares a las **arrow functions (`=>`) en JavaScript**.

Se utilizan cuando necesitamos **funciones pequeñas y rápidas**, generalmente para operaciones simples.

---

## 📘 Características

* Se definen en **una sola línea**.
* Se crean con la palabra reservada `lambda`.
* Solo pueden contener **una expresión**.
* No utilizan `return` (la expresión se devuelve automáticamente).
* Pueden asignarse a una variable para reutilizarlas.

---

## 🧱 Sintaxis

```python
lambda argumentos: expresion
```

* `argumentos` → parámetros que recibe la función
* `:` → separa los argumentos de la expresión
* `expresion` → operación que se evaluará y devolverá

---

## 🔁 Función equivalente

```python
# Función normal
def multiplicar_por_dos(x):
    return x * 2

# Función lambda equivalente
duplicar_argumento = lambda x: x * 2
```

Uso:

```python
multiplicar_por_dos(5)   # 10
duplicar_argumento(5)    # 10
```

📌 En este caso ambas funciones hacen exactamente lo mismo.

---

## 📊 Uso con `sorted()`

`sorted()` es una función que **ordena elementos de un iterable**.

### Argumentos principales

| argumento | descripción                                     |
| --------- | ----------------------------------------------- |
| iterable  | estructura a ordenar                            |
| key       | función usada para decidir el criterio de orden |
| reverse   | indica si el orden es descendente               |

Ejemplo:

```python
lista = [(1, 'a'), (3, 'c'), (2, 'b')]

lista_ordenada = sorted(lista, key=lambda elemento: elemento[1])

print(lista_ordenada)
```

Salida

```
[(1, 'a'), (2, 'b'), (3, 'c')]
```

📌 Explicación

Cada elemento de la lista es una **tupla**:

```
(1, 'a')
(3, 'c')
(2, 'b')
```

La lambda:

```
lambda elemento: elemento[1]
```

dice:

> usa el **segundo valor de cada tupla** como criterio de orden.

---

## 🔍 Uso con `filter()`

`filter()` permite **filtrar elementos de un iterable** usando una condición.

Sintaxis:

```python
filter(funcion, iterable)
```

* `funcion` → debe devolver `True` o `False`
* `iterable` → lista, tupla, etc.

Ejemplo:

```python
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
```

Salida

```
[2, 4, 6]
```

📌 Explicación

La lambda:

```
lambda x: x % 2 == 0
```

significa:

> devuelve `True` si el número es par.

`filter()` conserva solo los valores que cumplen la condición.

---

## 🗺️ Uso con `map()`

`map()` se usa para **aplicar una función a cada elemento de un iterable**.

Sintaxis:

```python
map(funcion, iterable)
```

Ejemplo:

```python
numeros = [1, 2, 3, 4]

cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)
```

Salida

```
[1, 4, 9, 16]
```

📌 Explicación

La lambda:

```
lambda x: x**2
```

eleva cada número al cuadrado.

`map()` aplica esa función a **cada elemento de la lista**.

---

## 🧩 Ejercicio Platzi (explicación paso a paso)

```python
def mi_funcion(n):
    return lambda a: a * n
```

Esta función **devuelve otra función**.

Es lo que se llama una **función de orden superior**.

---

### Paso 1

```python
duplicador = mi_funcion(2)
```

Aquí ocurre lo siguiente:

```
mi_funcion(2)
```

retorna:

```
lambda a: a * 2
```

Por lo tanto:

```
duplicador = lambda a: a * 2
```

Ahora `duplicador` **es una función**.

---

### Paso 2

```python
triplicador = mi_funcion(3)
```

Esto retorna:

```
lambda a: a * 3
```

Entonces:

```
triplicador = lambda a: a * 3
```

---

### Paso 3

Uso de las funciones:

```python
print(duplicador(5))   # 10
print(triplicador(5))  # 15
```

Porque realmente se ejecuta:

```
5 * 2
5 * 3
```

---

## 🧠 Forma mental de entenderlo

Es como **crear fábricas de funciones**.

```
mi_funcion(2) → crea función que multiplica por 2
mi_funcion(3) → crea función que multiplica por 3
```

Entonces:

```
duplicador = función que multiplica por 2
triplicador = función que multiplica por 3
```

---

## 💡 ¿Cuándo usar `lambda`?

Es recomendable usar `lambda` cuando:

✔ la función es pequeña  
✔ solo se usará una vez  
✔ se necesita dentro de `map`, `filter`, `sorted`, etc.

No es recomendable cuando:

* la función tiene lógica compleja
* se necesita reutilizar varias veces
* el código pierde legibilidad

---

## 🧠 Resumen

* `lambda` crea funciones **anónimas y cortas**.
* Solo pueden tener **una expresión**.
* Se usan mucho con `map()`, `filter()` y `sorted()`.
* Pueden asignarse a variables.
* Permiten crear **funciones dinámicas** como en el ejemplo del duplicador y triplicador.

---
