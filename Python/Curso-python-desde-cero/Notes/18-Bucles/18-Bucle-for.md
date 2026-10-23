
# 🔁 Bucle `for`

En otros lenguajes los bucles `for` tienen otra estructura.
Python simplifica los `for`, usando `for in`.

* Se pueden iterar **listas, tuplas, conjuntos, diccionarios y cadenas**.

---

## 🧱 Estructura

```python
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for animal in animales:  # animal guardará cada elemento al recorrer la lista
    print(f"La variable es igual a: {animal}")

# Continúa con la siguiente instrucción cuando ya no existan más elementos
```

Salida

```python
Perro
Gato
Conejo
Pollito
```

---

## 🔗 Iterando varias listas del mismo tamaño con `zip()`

`zip()`:

* Recibe como parámetros las listas que va a recorrer.
* Une los elementos en **tuplas temporales**.

```python
numeros = [23, 43, 56, 64]
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for numero, animal in zip(numeros, animales):
    print(f"Hay {numero} {animal}")
```

---

## 🔢 Iterando en rangos con `range()`

`range(parametro1, parametro2)`

* `parametro1` → desde dónde comienza
* `parametro2` → hasta dónde llega (sin incluirlo)

`range(un_parametro)`

* Comienza desde **0** hasta `parametro - 1`.

```python
for num in range(5, 10):
    print(num)
# Salida -> 5, 6, 7, 8, 9

for num in range(4):
    print(num)
# Salida -> 0, 1, 2, 3
```

---

## 📍 Forma correcta de recorrer una lista por su índice

```python
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for num in enumerate(animales):
    # Convierte num en una tupla (indice, valor)
    # En la primera iteración num es igual a (0, "Perro")

    indice = num[0]
    valor = num[1]

    print(f"El indice es: {indice} y el valor es: {valor}")
```

* `num` se convierte en una tupla `(indice, item_de_lista)`

### ✨ Forma más elegante

```python
for i, valor in enumerate(animales):
    print(f"El indice es: {i} y el valor es: {valor}")
```

---

### 📦 Desempaquetado de `enumerate()`

Al desempaquetar se deben usar **dos variables**:

* `i` → índice
* `valor` → elemento de la lista

---

## 🔁 Usando `else` en el `for`

* El `else` siempre se ejecuta **cuando el ciclo termina normalmente**.
* Si existe un `break`, el `else` **no se ejecuta**.

```python
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for i, valor in enumerate(animales):
    print(f"El indice es: {i} y el valor es: {valor}")
else:
    print("El bucle terminó")
```

---

## 🧩 Recorrido de conjuntos

* Los conjuntos **no tienen índice**.
* Se pueden recorrer directamente o usando `enumerate()` si se desea numerarlos.

---

## 📚 Iterando diccionarios

### Iterando con `items()`

* `items()` devuelve **clave y valor**.
* Sin `items()`, el `for` solo recorre **las claves**.

```python
diccionario = {
    "Nombre": "Luis",
    "Apellido": "Sánchez",
    "Carrera": "Ing. Software"
}

for datos in diccionario.items():
    key = datos[0]     # clave
    value = datos[1]   # valor

    print(f"La clave es: {key} y el valor es: {value}")
```

---

## ⛔ `continue` y `break` en el `for`

### ⏭ `continue`

Se usa para **saltar una iteración**.

Todo lo que esté después de `continue` **no se ejecuta en esa vuelta**.

---

### ⛔ `break`

`break` **termina el ciclo inmediatamente**.

Además, si existe un `else`, **no se ejecutará**.

```python
frutas = ["manzana", "naranja", "ciruela", "durazno", "pera", "sandía", "banana"]

for fruta in frutas:

    if fruta == "manzana":
        continue  # Soy alérgico a la manzana

    print(f"Me voy a comer {fruta}")

    if fruta == "pera":
        print("Me dolió la panza, no puedo seguir comiendo...")
        break

else:
    print("Ya me acabé las frutas")
```

---

## 🔤 Iterar una cadena de texto

```python
cadena = "Hola Mundo"

for letra in cadena:
    print(letra)
```

Imprime cada carácter individualmente.

---

## ⚡ `for` en una sola línea (List Comprehension)

```python
lista_numeros = [1, 2, 3, 4, 5]

nueva_lista_numeros = [x * 2 for x in lista_numeros]

print(nueva_lista_numeros)
```

Salida:

```bash
[2, 4, 6, 8, 10]
```

---
