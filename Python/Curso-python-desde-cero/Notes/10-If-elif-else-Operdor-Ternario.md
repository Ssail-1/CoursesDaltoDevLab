
# Condicionales **(`if`, `elif`, `else`)**

## **¿Qué son los condicionales?**

Los condicionales permiten **tomar decisiones** dentro del programa.
Evalúan una expresión lógica (`True` o `False`) y ejecutan código dependiendo del resultado.

---

## 🧱 **Estructura básica**

```python
if condicion:
    # código si la condición es verdadera
elif otra_condicion:
    # código si la condición anterior fue falsa
else:
    # código si ninguna condición fue verdadera
```

📌 **Importante:**

* En Python **los bloques de código se definen por indentación (espacios o tabulaciones)**, no por llaves `{}`.
* Lo habitual es usar **4 espacios** por nivel.

---

## ⚙️ **Ejemplo simple**

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

Salida:

```
Eres mayor de edad
```

---

## 🧠 **Ejemplo con `elif` (múltiples condiciones)**

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

Salida:

```
Muy bien
```

---

## 💡 **Condicionales anidados**

Puedes colocar un `if` dentro de otro, aunque se recomienda no abusar de esto para mantener la legibilidad.

```python
usuario = "Luis"
clave = "1234"

if usuario == "Luis":
    if clave == "1234":
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")
```

---

## 🔗 **Condiciones compuestas**

Puedes combinar condiciones con operadores lógicos (`and`, `or`, `not`):
*(estos los veremos a detalle en el siguiente tema, pero aquí tienes una vista previa)*

```python
edad = 20
licencia = True

if edad >= 18 and licencia:
    print("Puedes conducir")
else:
    print("No cumples los requisitos")
```

---

## 🧮 **Comparaciones dentro del `if`**

Cualquier operación que devuelva un valor booleano (`True` o `False`) puede usarse dentro de un condicional:

```python
x = 10
y = 5

if (x + y) > 12:
    print("La suma es mayor a 12")
else:
    print("La suma es 12 o menor")
```

---

## 🧩 **Condicional en una sola línea (expresión ternaria)**

Forma corta de escribir un `if/else` cuando solo hay una instrucción:

```python
edad = 17
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)
```

Salida:

```
Menor de edad
```

---

## 🧠 **Resumen**

* `if` evalúa una condición.
* `elif` permite agregar más condiciones.
* `else` se ejecuta si ninguna condición anterior fue verdadera.
* Se usa **indentación** (no llaves).
* Se pueden **anidar** y **combinar** con operadores lógicos.
* Python permite escribir un `if` en una sola línea (expresión condicional).

---

## 💬 **Comparación rápida con Java**

| Concepto           | Python                         | Java                             |
| ------------------ | ------------------------------ | -------------------------------- |
| Sintaxis           | `if`, `elif`, `else`           | `if`, `else if`, `else`          |
| Bloques            | Se definen con **indentación** | Se definen con `{}`              |
| Expresiones cortas | `"A" if cond else "B"`         | Operador ternario `cond ? A : B` |

---
