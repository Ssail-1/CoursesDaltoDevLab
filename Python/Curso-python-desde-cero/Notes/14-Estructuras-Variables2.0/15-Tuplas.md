
# 🟣 **Tuplas en Python (`tuple`)**

---

## 📘 **¿Qué es una tupla?**

Una **tupla** es una colección **inmutable y ordenada** de elementos.
A diferencia de las listas, **no se pueden modificar**, es decir: no puedes añadir, eliminar ni cambiar sus elementos después de creada.

```python
tupla = ("Python", "Java", "C++")
print(tupla[0])  # Python
```

📍 Se utilizan cuando quieres garantizar que los datos **no cambien** durante la ejecución.

---

## 🧩 **Formas de crear tuplas**

### 1. Con paréntesis

```python
tupla = ("dato1", "dato2", "dato3")
```

### 2. Sin paréntesis (empaquetado implícito)

Si separas elementos por comas, Python los empaqueta automáticamente en una tupla:

```python
tupla = "dato1", "dato2", "dato3"
```

### 3. Una tupla con un solo elemento

Debes agregar **una coma** al final:

```python
tupla = ("dato1",)   # ✅ Tupla
no_tupla = ("dato1") # ❌ String
```

### 4. Con la función `tuple()`

Puedes convertir cualquier iterable (lista, string, etc.) en una tupla:

```python
lista = ["a", "b", "c"]
tupla = tuple(lista)
print(tupla)  # ('a', 'b', 'c')
```

---

## 🔁 **Acceso a elementos**

Las tuplas se comportan igual que las listas para acceder por índice:

```python
colores = ("rojo", "verde", "azul")
print(colores[0])   # rojo
print(colores[-1])  # azul
```

> [!note]
> Y puedes usar **slicing**:

```python
print(colores[0:2])  # ('rojo', 'verde')
```

---

## ⚙️ **Desempaquetado (repaso rápido)**

Puedes asignar sus elementos directamente a variables:

```python
persona = ("Luis", 25, "México")
nombre, edad, pais = persona
print(nombre, edad, pais)
```

💡 Muy útil cuando una función devuelve múltiples valores.

---

## 🧮 **Operaciones comunes con tuplas**

| Operación   | Ejemplo            | Resultado                  |
| ----------- | ------------------ | -------------------------- |
| Concatenar  | `(1, 2) + (3, 4)`  | `(1, 2, 3, 4)`             |
| Repetir     | `("A",) * 3`       | `('A', 'A', 'A')`          |
| Pertenencia | `'A' in ('A','B')` | `True`                     |
| Longitud    | `len(tupla)`       | `Número de elementos`      |
| Conteo      | `tupla.count("x")` | Veces que aparece un valor |
| Índice      | `tupla.index("x")` | Posición del valor         |

---

## 🧱 **Inmutabilidad y uso en colecciones**

Las tuplas **no se pueden modificar**, pero sí puedes:

* Crear una **nueva tupla** basada en otra.
* Usarlas como **clave en un diccionario** (porque son inmutables).

```python
coordenadas = (10, 20)
dic = {coordenadas: "Punto A"}
print(dic[(10, 20)])  # Punto A
```

---

## 🧩 **Anidación y conversión**

Tuplas pueden contener otras colecciones:

```python
datos = ("Luis", (25, "México"))
print(datos[1][1])  # México
```

Y puedes convertir entre lista ↔ tupla:

```python
tupla = ("a", "b", "c")
lista = list(tupla)
lista.append("d")
tupla = tuple(lista)
print(tupla)  # ('a', 'b', 'c', 'd')
```

---

## ⚠️ **Errores comunes**

| Error                                                        | Causa                         | Solución                                      |
| ------------------------------------------------------------ | ----------------------------- | --------------------------------------------- |
| `TypeError: 'tuple' object does not support item assignment` | Intentar modificar una tupla. | Convierte a lista, modifica y vuelve a tupla. |
| Olvidar la coma en una tupla de un solo elemento             | `("dato1")` → es un string.   | `("dato1",)`                                  |

---

## 🔄 **Comparación: Tupla vs Lista**

| Característica                            | Tupla (`tuple`)  | Lista (`list`)  |
| ----------------------------------------- | ---------------- | --------------- |
| Mutabilidad                               | ❌ Inmutable      | ✅ Mutable       |
| Sintaxis                                  | `()`             | `[]`            |
| Velocidad                                 | ⚡ Más rápida     | 🐢 Más lenta    |
| Uso típico                                | Datos constantes | Datos variables |
| Hashable (puede ser clave en diccionario) | ✅ Sí             | ❌ No            |

---

## 🧠 **Resumen**

* Las tuplas son **listas inmutables** y ordenadas.
* Ideales para **datos constantes o de configuración**.
* Soportan operaciones básicas como concatenar o contar.
* Pueden usarse como claves en diccionarios.
* Perfectas para **devolver múltiples valores** desde funciones.

---

## 🧩 **Ejemplo práctico**

```python
def obtener_datos():
    nombre = "Luis"
    edad = 25
    pais = "México"
    return nombre, edad, pais  # Devuelve una tupla

datos = obtener_datos()
print(datos)            # ('Luis', 25, 'México')

nombre, edad, pais = datos
print(f"{nombre} tiene {edad} años y vive en {pais}.")
```

---

💬 **Conclusión:**
Las tuplas son pequeñas estructuras ligeras y rápidas, ideales para representar conjuntos de datos que **no deben modificarse**, y uno de los tipos más usados en Python junto con listas y diccionarios.

---
