
# Funciones Propias

## Función simple

Estructura:

```py
def saludar():
    print("Hola Luis, Que tal estas?")
```

def -> Indica a python que vamos a crear una funcion
Despúes indicamos el `nombre de la función`

## Función con parametros

```py
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adj = "reina"
    elif sexo == "hombre":
        adj = "titan"
    else:
        adj = "amor"

    print(f"Hola {nombre}, mi {adj}, ¿como estas?")
```

## Crear una función que nos retorne valores

Usamos `return` para poder devolver algun dato dentro dentro de una función.

- Podemos devolver todo tipo de datos
- Tambien multiples valores tan solo separandolos con comas.

```py
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña # Devuelve la contraseña

password = crear_contraseña_random(3)
frase = f"Tu contraseña nueva es: {password}"
print(frase)
```

## Utilizando el parametro `*args`

<Noa> Desarrolla este tema porfavor, si lo entendí, pero como tal no hubo teoría solo fueron practicas y me gustaría que me dieras información clave.</Noa>

`args` se usa para pasar un número variable de argumentos.

- Cuando se utiliza esta forma de pasar un numero indefinido de variables, los argumentos se agrupan en una **tupla**.
- Esta tupla se guarda y se indica al parametro con un asterisco antes: `*parametro_Tupla`.
  - De esta manera ya no es necesario definirlo como `*args`.
  - Se puede definir cualquier nombre en lugar de args.

### Ejemplo

```py 
def sumar_todos(*args):
    total = 0
    for num in args:
        total += num
    # o -> sum(args)
    return total

print(sumar_todos(1, 2, 3, 4, 5, 6))
```

## Utilizando parametros ***`**kwargs `***

- `*args` se utiliza para argumentos pocisionales (sin nombre).
- Para pasar varias variables de argumentos con (`clave: valor`), se define como parametro `**kwargs`.

## Orden de argumentos

Al pasar los argumentos, estos tienen que ser congruentes al orden.

```py
def saludar(nombre, edad, soltero):
    if soltero:
        soltero = "tienes pareja"
    else:
        soltero = "no tiene pareja"
    
    print(f"Hola {nombre}, tienes {edad} años y {soltero}")

saludar("Luis", 25, False)

# Esto sería incorrecto
saludar(25, False, "Luis")
```

### Forzando argumentos

Podemos pasar argumentos en desorden forzandolos de la siguiente manera...

```py
def saludar(nombre, edad, soltero):
    if soltero:
        soltero = "tienes pareja"
    else:
        soltero = "no tiene pareja"
    
    print(f"Hola {nombre}, tienes {edad} años y {soltero}")

# Forzando los argumentos
saludar(edad = 25, soltero = False, nombre = "Luis")
```

> [!important]
> Si se tiene la necesidad de forzar algun argumento, todos se tienen que forzar para que funcione.
>
