
# ⚙️ Funciones propias

Las funciones permiten **agrupar instrucciones** para reutilizarlas cuando sea necesario.
Ayudan a que el código sea más **ordenado, legible y reutilizable**.

---

## 🧱 Función simple

### Estructura

```python
def saludar():
    print("Hola Luis, ¿qué tal estás?")
```

* `def` → indica a Python que vamos a crear una función.
* Después se escribe el **nombre de la función**.
* Los paréntesis `()` indican los parámetros que recibirá.
* Los dos puntos `:` abren el bloque de código de la función.

📌 La función no se ejecuta sola, hay que llamarla:

```python
saludar()
```

---

## 🧩 Función con parámetros

Los parámetros permiten que la función reciba datos externos.

```python
def saludar(nombre, sexo):
    sexo = sexo.lower()

    if sexo == "mujer":
        adj = "reina"
    elif sexo == "hombre":
        adj = "titán"
    else:
        adj = "amor"

    print(f"Hola {nombre}, mi {adj}, ¿cómo estás?")
```

📌 Aquí `nombre` y `sexo` son parámetros.

Ejemplo de llamada:

```python
saludar("María", "mujer")
saludar("Luis", "hombre")
```

---

## 🛟 Argumentos por defecto

Si al llamar una función el usuario olvida indicar un argumento, podemos definir un valor por defecto.

```python
def saludar(nombre, nacionalidad="No indicada"):
    print(f"Hola {nombre}, Nacionalidad: {nacionalidad}")

saludar("Luis", "Mexicana")   # Hola Luis, Nacionalidad: Mexicana
saludar("María")              # Hola María, Nacionalidad: No indicada
```

📌 Los parámetros con valor por defecto deben colocarse **después** de los obligatorios.

---

## 🔁 Crear una función que retorne valores

Usamos `return` para devolver un valor desde una función.

* Puede devolver cualquier tipo de dato.
* También puede devolver varios valores separándolos con comas.

```python
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])

    c1 = num - 2
    c2 = num
    c3 = num - 5

    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña
```

```python
password = crear_contraseña_random(3)
frase = f"Tu contraseña nueva es: {password}"
print(frase)
```

📌 `return` termina la ejecución de la función y devuelve el valor indicado.

---

## 📦 Utilizando el parámetro `*args`

`*args` se usa para pasar un **número variable de argumentos posicionales**.

* Los argumentos se agrupan automáticamente en una **tupla**.
* No es obligatorio llamarlo `args`, pero es la convención más usada.
* El asterisco `*` es lo importante.

### Ejemplo

```python
def sumar_todos(*args):
    total = 0

    for num in args:
        total += num

    return total
```

```python
print(sumar_todos(1, 2, 3, 4, 5, 6))
```

También se puede hacer así:

```python
def sumar_todos(*numeros):
    return sum(numeros)
```

📌 Aquí `args` funciona como una tupla:

```python
def ejemplo(*args):
    print(args)

ejemplo(10, 20, 30)   # (10, 20, 30)
```

### ¿Cuándo usar `*args`?

Cuando no sabes cuántos argumentos va a recibir la función.

---

## 🗂️ Utilizando parámetros `**kwargs`

`**kwargs` se usa para pasar un **número variable de argumentos con nombre** (`clave=valor`).

* `*args` → argumentos posicionales
* `**kwargs` → argumentos nombrados
* Los valores se agrupan en un **diccionario**

### Ejemplo

```python
def mostrar_datos(**kwargs):
    print(kwargs)
```

```python
mostrar_datos(nombre="Luis", edad=25, carrera="Ing. Software")
```

Salida:

```python
{'nombre': 'Luis', 'edad': 25, 'carrera': 'Ing. Software'}
```

### Recorriendo `kwargs`

```python
def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
```

```python
mostrar_datos(nombre="Luis", edad=25, carrera="Ing. Software")
```

📌 `kwargs` funciona como un diccionario, por eso se puede recorrer con `.items()`.

### ¿Cuándo usar `**kwargs`?

Cuando no sabes qué cantidad de argumentos con nombre se enviarán, o cuando quieres flexibilidad al recibir datos.

---

## 🧠 Diferencia entre `*args` y `**kwargs`

| Parámetro  | Tipo de argumentos         | Cómo se agrupan |
| ---------- | -------------------------- | --------------- |
| `*args`    | Posicionales               | Tupla           |
| `**kwargs` | Con nombre (`clave=valor`) | Diccionario     |

Ejemplo usando ambos:

```python
def ejemplo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

ejemplo(1, 2, 3, nombre="Luis", edad=25)
```

Salida:

```python
args: (1, 2, 3)
kwargs: {'nombre': 'Luis', 'edad': 25}
```

---

## 🔢 Orden de argumentos

Al pasar argumentos posicionales, deben ir en el orden correcto de los parámetros.

```python
def saludar(nombre, edad, soltero):
    if soltero:
        estado = "tienes pareja"
    else:
        estado = "no tienes pareja"

    print(f"Hola {nombre}, tienes {edad} años y {estado}")
```

```python
saludar("Luis", 25, False)
```

Esto sería incorrecto:

```python
saludar(25, False, "Luis")
```

📌 Python asigna los valores según la posición en que se envían.

---

## 🎯 Forzando argumentos por nombre

Podemos pasar argumentos en desorden si indicamos explícitamente a qué parámetro corresponde cada valor.

```python
def saludar(nombre, edad, soltero):
    if soltero:
        estado = "tienes pareja"
    else:
        estado = "no tienes pareja"

    print(f"Hola {nombre}, tienes {edad} años y {estado}")
```

```python
saludar(edad=25, soltero=False, nombre="Luis")
```

> [!important]
> Si se mezclan argumentos posicionales y nombrados, primero deben ir los posicionales.
> Si ya empiezas a forzar por nombre, lo más claro es mantener todos de esa forma.

---

## 💡 Resumen

* Las funciones agrupan código reutilizable.
* `def` se usa para definir funciones.
* Los parámetros permiten recibir datos.
* Los argumentos por defecto evitan errores cuando falta información.
* `return` devuelve valores.
* `*args` recibe varios argumentos posicionales en forma de tupla.
* `**kwargs` recibe varios argumentos con nombre en forma de diccionario.
* Los argumentos pueden enviarse por **posición** o por **nombre**.

---