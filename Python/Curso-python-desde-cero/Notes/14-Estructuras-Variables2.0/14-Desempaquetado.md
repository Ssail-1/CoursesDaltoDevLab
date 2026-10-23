
# 🎁 **Desempaquetado en Python**

## 📘 **¿Qué es el desempaquetado?**

El **desempaquetado** permite asignar los valores de una colección (como una **tupla**, **lista** o **set**) a variables individuales de una sola vez.
Es una forma rápida y limpia de extraer varios valores sin acceder por índices.

```python
datos = ("Luis", "Sánchez", "Estudiante")
nombre, apellido, ocupacion = datos

print(nombre)      # Luis
print(apellido)    # Sánchez
print(ocupacion)   # Estudiante
```

📌 **Regla:**
El número de variables debe coincidir con el número de elementos en la estructura.

---

## 🧩 **Desempaquetado con diferentes estructuras**

### 🟦 **Tuplas**

Funciona naturalmente:

```python
tupla = ("Python", "Java", "C++")
a, b, c = tupla
print(a, b, c)  # Python Java C++
```

### 🟨 **Listas**

Exactamente igual:

```python
lista = [1, 2, 3]
x, y, z = lista
print(x, y, z)  # 1 2 3
```

### 🟪 **Conjuntos**

El **orden es aleatorio**, porque los conjuntos no son estructuras indexadas.

```python
datos = {"Luis", "Sánchez", 25}
nombre, apellido, edad = datos
print(nombre, apellido, edad)
# El orden puede variar cada vez que ejecutes el programa
```

> [!tip]
> 💡 Por eso **no se recomienda usar desempaquetado con sets** cuando el orden importa.

---

## ⚙️ **Ignorar valores en el desempaquetado**

Si no necesitas todos los valores, puedes ignorar alguno usando `_` (una convención en Python para valores “desechables”):

```python
persona = ("Luis", "Sánchez", 25)
nombre, _, edad = persona
print(nombre, edad)  # Luis 25
```

---

## 🧮 **Desempaquetado extendido**

Usando `*` puedes capturar **varios valores en una sola variable** (como una lista):

```python
numeros = [1, 2, 3, 4, 5]
a, b, *resto = numeros
print(a, b, resto)  # 1 2 [3, 4, 5]
```

También puedes colocar el `*` en medio o al inicio:

```python
*a, b, c = numeros
print(a, b, c)  # [1, 2, 3] 4 5
```

📘 Este tipo de desempaquetado es muy útil cuando no sabes exactamente cuántos elementos hay en una lista o cuando solo te interesan algunos.

---

## 🔁 **Desempaquetado dentro de bucles**

Se usa mucho para recorrer estructuras con tuplas o pares clave-valor:

```python
usuarios = [("Luis", 25), ("Ana", 20), ("Carlos", 30)]

for nombre, edad in usuarios:
    print(f"{nombre} tiene {edad} años")
```

📌 Aquí el bucle va desempaquetando cada tupla en dos variables por iteración.

---

## 🔄 **Desempaquetado en diccionarios**

Por defecto, un `for` sobre un diccionario recorre **solo las claves**.
Pero usando `.items()` puedes desempaquetar claves y valores fácilmente:

```python
persona = {"nombre": "Luis", "edad": 25, "pais": "México"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

## 🧠 **Resumen**

| Concepto                 | Descripción                                                       | Ejemplo                   |
| ------------------------ | ----------------------------------------------------------------- | ------------------------- |
| Desempaquetado           | Asigna varios valores de una estructura a variables individuales. | `a, b = (1, 2)`           |
| Ignorar valores          | Usa `_` para valores que no necesitas.                            | `a, _, b = (1, 2, 3)`     |
| Desempaquetado extendido | Usa `*` para agrupar varios valores.                              | `a, *b = [1,2,3,4]`       |
| En bucles                | Permite recorrer listas o tuplas fácilmente.                      | `for x, y in lista:`      |
| Con sets                 | Funciona, pero el orden es impredecible.                          | `a, b, c = {"x","y","z"}` |

---

💬 **Conclusión:**
El desempaquetado hace tu código más **limpio, legible y profesional**.
Se usa muchísimo en Python moderno, especialmente con:

* Retornos múltiples de funciones.
* Iteraciones con tuplas o diccionarios.
* Asignaciones dinámicas.

---
