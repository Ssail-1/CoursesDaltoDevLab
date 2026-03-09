'''
## 🧩 **Ejercicio sugerido**

Crea un pequeño programa que:

1. Pida al usuario su nombre y edad.
2. Valide que la edad sea un número.
3. Si la edad es mayor o igual a 18, imprima un mensaje de acceso; si no, deniegue el acceso.

```python
nombre = input("Nombre: ").strip().capitalize()
edad = input("Edad: ")

if edad.isdigit():
    edad = int(edad)
    if edad >= 18:
        print(f"Bienvenido, {nombre}. Acceso permitido.")
    else:
        print(f"Lo siento {nombre}, debes ser mayor de edad.")
else:
    print("Edad no válida, ingresa solo números.")
```

'''

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