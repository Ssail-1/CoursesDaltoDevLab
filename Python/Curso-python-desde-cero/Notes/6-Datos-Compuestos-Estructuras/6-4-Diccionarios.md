
# Diccionarios en Python (`dict`)

## 📘 ¿Qué es un diccionario?

* Es una **colección desordenada** que almacena datos en pares **clave → valor**.
* Cada clave debe ser **única**.
* Los valores pueden ser de **cualquier tipo** (strings, números, listas, otros diccionarios…).
* Se define con **llaves `{}`**.

```python
persona = {
    "nombre": "Luis",
    "edad": 21,
    "pais": "México"
}
```

---

## 🔑 **Acceder a los valores**

```python
print(persona["nombre"])     # Luis
print(persona.get("edad"))   # 21
```

> [!important]
> ⚠️ Si la clave no existe, `[]` lanza error, pero `get()` devuelve `None`.

---

## 🧱 **Agregar, modificar y eliminar elementos**

```python
# Agregar
persona["profesion"] = "Desarrollador"

# Modificar
persona["edad"] = 25

# Eliminar
persona.pop("pais")     # elimina una clave específica
del persona["nombre"]   # otra forma de eliminar
persona.clear()         # vacía el diccionario
```

---

## 📏 **Funciones y métodos útiles**

| Método / función   | Descripción                              | Ejemplo                  |
| ------------------ | ---------------------------------------- | ------------------------ |
| `len(dic)`         | Número de pares clave-valor.             | `len(persona)`           |
| `dic.keys()`       | Devuelve todas las claves.               | `persona.keys()`         |
| `dic.values()`     | Devuelve todos los valores.              | `persona.values()`       |
| `dic.items()`      | Devuelve lista de tuplas (clave, valor). | `persona.items()`        |
| `dic.get("clave")` | Obtiene el valor o `None`.               | `persona.get("nombre")`  |
| `dic.pop("clave")` | Elimina un elemento.                     | `persona.pop("edad")`    |
| `dic.copy()`       | Copia el diccionario.                    | `copia = persona.copy()` |

---

## 🔄 **Recorrer un diccionario**

```python
for clave in persona:
    print(clave, ":", persona[clave])

# o más limpio:
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

## 🧩 **Diccionarios anidados**

Puedes tener diccionarios dentro de otros:

```python
usuarios = {
    "ssail": {"nombre": "Luis", "rol": "admin"},
    "noa": {"nombre": "Noa", "rol": "asistente"}
}

print(usuarios["ssail"]["rol"])  # admin
```

---

## 🧠 **Resumen**

* Estructura clave-valor, equivalente a **HashMap** en Java o **objeto JSON** en JavaScript.
* Claves únicas, valores modificables.
* Acceso rápido a la información mediante claves.
* Soporta anidación, iteración y métodos de copia, unión y actualización.

---

## 💬 **Comparación con otras estructuras**

| Lenguaje           | Estructura equivalente | Ejemplo                   |
| ------------------ | ---------------------- | ------------------------- |
| **Python**         | `dict`                 | `{"clave": "valor"}`      |
| **JavaScript**     | `Object` / `JSON`      | `{ clave: "valor" }`      |
| **Java**           | `HashMap`              | `HashMap<String, String>` |
| **Bases de datos** | Clave primaria (ID)    | `id -> fila`              |

---
---

## 🧩 Refuezo Diccionarios (`dict`)**

* (contenido base igual que antes: qué son, cómo se crean, cómo acceder y modificar…)*

---

### `keys()`

Devuelve un objeto de tipo `dict_keys` con todas las **claves** del diccionario.
También puede usarse para **iterar** sobre las claves.

```python
diccionario = {"nombre": "Luis", "edad": 25, "pais": "México"}
claves = diccionario.keys()

print(claves)           # dict_keys(['nombre', 'edad', 'pais'])
for clave in claves:
    print(clave)        # Recorre las claves
```

---

### `items()`

Devuelve los elementos como **tuplas (clave, valor)** dentro de un objeto `dict_items`.
Se usa frecuentemente para **recorrer diccionarios** de manera más legible.

```python
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
# dict_items([('nombre', 'Luis'), ('edad', 25), ('pais', 'México')])

for clave, valor in diccionario.items():
    print(f"{clave} → {valor}")
```

---

### `clear()`

Elimina **todos los elementos** del diccionario, dejándolo vacío.

```python
diccionario.clear()
print(diccionario)  # {}
```

---

💡 **Consejo:**
Puedes comprobar qué otros métodos tiene un diccionario con:

```python
print(dir(dict))
```

Así verás todos los disponibles (como `update()`, `fromkeys()`, etc.), incluso algunos que todavía no hemos usado.

---
