
# 🧩 **Entrada de Datos en Python (`input()`)**

---

## 📘 **¿Qué hace `input()`?**

La función `input()` **pausa la ejecución del programa** y **espera que el usuario ingrese un valor por teclado**.
El texto que escribas se almacena como una **cadena (`str`)**.

```python
nombre = input("Escribe tu nombre: ")
print("Hola", nombre)
```

📌 **Importante:**
Todo lo que devuelve `input()` es de tipo **string**, sin importar si ingresas un número, texto o símbolo.

---

## 🔠 **Casting o conversión de tipos**

Para usar el valor como número (entero o decimal), debes **convertirlo manualmente**.

```python
edad = input("Ingresa tu edad: ")

# Convertir a entero
edad = int(edad)

# Convertir a flotante
altura = float(input("Ingresa tu altura en metros: "))

print("Tienes", edad, "años y mides", altura, "m.")
```

> [!important]
>📍 *Si el usuario ingresa algo no numérico y tratas de convertirlo con `int()` o `float()`, el programa lanzará un error (`ValueError`).*

---

## 🔍 **Ejemplo práctico con casting**

```python
numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))

suma = numero_1 + numero_2

print("La suma es:", suma)
```

Salida:

```py
Ingresa el primer número: 5
Ingresa el segundo número: 3
La suma es: 8.0
```

---

## ⚙️ **Validar datos de entrada**

Python no tiene un “try-except” automático como Java,
pero puedes **controlar errores manualmente** con estructuras condicionales o excepciones.

### Ejemplo simple de validación

```python
dato = input("Ingresa un número: ")

if dato.isdigit():
    numero = int(dato)
    print("Número ingresado:", numero)
else:
    print("Error: no ingresaste un número válido.")
```

---

## 🚫 **Control de errores con try-except**

Si quieres evitar que el programa se detenga por un error de tipo, puedes usar `try` y `except`:

```python
try:
    numero = int(input("Ingresa un número entero: "))
    print("Número válido:", numero)
except ValueError:
    print("Error: Debes ingresar un número entero.")
```

📘 *Esto es muy usado en programas reales que requieren robustez en la interacción con el usuario.*

---

## 🧠 **Combinar `input()` con métodos de cadenas**

Puedes limpiar, validar o transformar el texto directamente:

```python
nombre = input("Nombre: ").strip().capitalize()
print(f"Bienvenido, {nombre}!")
```

Aquí:

* `.strip()` elimina espacios al inicio y final.
* `.capitalize()` pone en mayúscula la primera letra.

---

## 🔄 **Usar `input()` dentro de bucles**

Ideal cuando necesitas repetir la entrada hasta que cumpla una condición:

```python
while True:
    edad = input("Ingresa tu edad: ")
    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("Por favor ingresa un número válido.")
```

---

## 💡 **Comparación con Java**

| Lenguaje   | Entrada                      | Observaciones                                                                                                          |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Python** | `input()`                    | Devuelve `str`, conversión manual con `int()` o `float()`.                                                             |
| **Java**   | `Scanner` / `BufferedReader` | `Scanner` es más simple pero más lento; `BufferedReader` es más eficiente. En ambos casos hay que manejar excepciones. |

💬 En resumen:

* `input()` en Python cumple el mismo rol que `Scanner.nextLine()` en Java.
* Python evita la complejidad de clases de lectura; todo se basa en una sola función simple y flexible.

---

## 🧩 **Ejercicio sugerido**

Crea un pequeño programa que:

1. Pida al usuario su nombre y edad.
2. Valide que la edad sea un número.
3. Si la edad es mayor o igual a 18, imprima un mensaje de acceso; si no, deniegue el acceso.

### Ejercicio Resuelto

---

```python
# Entrada de datos
nombre = input("Ingresa tu nombre: ").strip().capitalize()

while True:
    edad = input('Cual es tu edad?: ')
    if edad.isdigit():
        edad = int(edad)
        if edad > 17:
            print(f"""Bienvenido {nombre}.
                  Acceso permitido""")
            break
        else:
            print(f"Lo siento {nombre}, debes ser mayor de edad.")
            break
    else:
        print("Edad no válida, ingresa solo números.")
```

---

## 🧭 **Resumen general**

* `input()` → lee texto desde teclado.
* Todo lo que devuelve es **string**.
* Usa `int()` o `float()` para convertir a número.
* Valida con `.isdigit()` o `try/except`.
* Puedes combinarlo con métodos de cadena (`strip`, `lower`, `capitalize`).
* Ideal para construir programas interactivos.

---
