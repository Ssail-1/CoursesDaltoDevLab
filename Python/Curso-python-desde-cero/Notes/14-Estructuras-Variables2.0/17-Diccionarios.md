
# 🟤 **Diccionarios en Python (`dict`)**

---

## 📘 **¿Qué es un diccionario?**

Un **diccionario** es una colección **desordenada y modificable** de elementos que almacenan información en **pares clave-valor**.

```python
persona = {
    "nombre": "Luis",
    "edad": 25,
    "profesion": "Desarrollador"
}
```

📌 Cada **clave (key)** debe ser única.
📌 Los **valores (values)** pueden ser de cualquier tipo: `str`, `int`, `list`, `dict`, etc.

---

## 🔑 **Acceder a los valores**

```python
print(persona["nombre"])   # Luis
print(persona.get("edad")) # 25
```

> ⚠️ Si usas `[]` con una clave inexistente, lanza un `KeyError`.  
> Con `get()` devuelve `None` (o un valor por defecto si lo indicas).

```python
print(persona.get("pais", "Desconocido"))  # Desconocido
```

---

## 🧱 **Agregar, modificar y eliminar elementos**

```python
# Agregar o modificar
persona["pais"] = "México"
persona["edad"] = 26

# Eliminar por clave
persona.pop("profesion")
del persona["pais"]

# Vaciar el diccionario
persona.clear()
```

---

## 🧩 **Crear diccionarios de diferentes maneras**

### Con `dict()`

```python
dic = dict(nombre="Luis", apellido="Sánchez")
```

### Con `fromkeys()`

Crea un diccionario con claves desde un iterable y valores por defecto.

```python
dic = dict.fromkeys(["nombre", "edad"], "Desconocido")
# {'nombre': 'Desconocido', 'edad': 'Desconocido'}
```

```py
diccionario = dict.fromkeys(["nombre", "apellido", "suscriptores"])

print(diccionario)
#Salida -> {'nombre': None, 'apellido': None, 'edad': None}

#------------OTRO EJEMPLO-------------
diccionario = dict.fromkeys("ABCDE")

print(diccionario)
#Salida -> {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}

#------------OTRO EJEMPLO--------------
diccionario = dict.fromkeys("ABCDE", "Hola")

print(diccionario)
#Salida -> {'A': 'Hola', 'B': 'Hola', 'C': 'Hola', 'D': 'Hola', 'E': 'Hola'}
```

### Con tuplas como claves (porque son inmutables)

```python
coordenadas = {(10, 20): "Punto A"}
print(coordenadas[(10, 20)])  # Punto A
```

---

## 🧮 **Métodos útiles de diccionarios**

| Método / función       | Descripción                               | Ejemplo                                |
| ---------------------- | ----------------------------------------- | -------------------------------------- |
| `len(dic)`             | Devuelve número de pares clave-valor      | `len(persona)`                         |
| `dic.keys()`           | Devuelve todas las claves                 | `persona.keys()`                       |
| `dic.values()`         | Devuelve todos los valores                | `persona.values()`                     |
| `dic.items()`          | Devuelve lista de tuplas `(clave, valor)` | `persona.items()`                      |
| `dic.pop("clave")`     | Elimina y devuelve el valor               | `persona.pop("edad")`                  |
| `dic.copy()`           | Copia el diccionario                      | `copia = persona.copy()`               |
| `dic.update(otro_dic)` | Agrega o actualiza pares clave-valor      | `persona.update({"ciudad": "Toluca"})` |

---

## 🔁 **Recorrer un diccionario**

```python
persona = {"nombre": "Luis", "edad": 25, "pais": "México"}

# Solo claves
for clave in persona:
    print(clave)

# Clave y valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

## 🧱 **Diccionarios anidados**

Puedes guardar un diccionario dentro de otro:

```python
usuarios = {
    "ssail": {"nombre": "Luis", "rol": "admin"},
    "noa": {"nombre": "Noa", "rol": "asistente"}
}

print(usuarios["ssail"]["rol"])  # admin
```

---

## ⚙️ **Comprobaciones y pertenencia**

```python
persona = {"nombre": "Luis", "edad": 25}

print("nombre" in persona)   # True
print("altura" not in persona)  # True
```

---

## 🔄 **Comparación con otras estructuras**

| Lenguaje       | Equivalente                          | Ejemplo                   |
| -------------- | ------------------------------------ | ------------------------- |
| **Python**     | `dict`                               | `{"clave": "valor"}`      |
| **JavaScript** | `Object` / `JSON`                    | `{ clave: "valor" }`      |
| **Java**       | `HashMap`                            | `HashMap<String, String>` |
| **SQL / BD**   | Fila identificada por clave primaria | `id -> registro`          |

---

## 🧠 **Resumen**

* Diccionarios = estructura **clave → valor**.
* Claves únicas, valores modificables.
* Acceso rápido y legible.
* Anidables y dinámicos.
* Soportan conversión, copia, actualización y borrado total.

---

## 💬 **Ejemplo práctico**

```python
inventario = {
    "manzanas": 10,
    "peras": 5,
    "plátanos": 8
}

nuevo = input("Agrega una fruta: ").lower()
cantidad = int(input("Cantidad: "))

inventario[nuevo] = cantidad

print("\nInventario actualizado:")
for fruta, cant in inventario.items():
    print(f"{fruta}: {cant}")
```

📤 **Salida:**

```py
Agrega una fruta: uvas
Cantidad: 12
Inventario actualizado:
manzanas: 10
peras: 5
plátanos: 8
uvas: 12
```

---
