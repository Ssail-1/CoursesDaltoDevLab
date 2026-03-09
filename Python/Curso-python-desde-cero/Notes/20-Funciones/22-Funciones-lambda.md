
# Funciones lambda

Las funciones lambda son equivalentes a las funciones de flecha (arrow functions) en JavaScript.

Es una forma de crear una **función anonima** porque no tiene nombre

- Son funciones que se definen en una sola línea.
- Palabra reservada: `lambda`.
- Solo pueden contener una única expreción
- La palabra clave `lambda` va seguida de los `argumentos`, dos puntos `:` y la `expresión a evaluar`.
- Aunque no tienen nombre se pueden asignar a una variable para volver a utilizarlas porsteriormente.

```py
# Sintaxis
lambda argumentos: expreción
```

## Función equivalente

```py
# Esta función 
def multiplicar_por_dos(x):
    return x*2

# Es equivalente a: 
duplicar_argumento = lambda x: x*2

# Llamando a la función def
multiplicar_por_dos(5) # = 10

# Llamando a la función lambda almacenada en una variable
duplicar_argumento(5) # = 10
```

## Ejemplos de uso

<Noa> Pongo estos ejemplos pero cambialos porfa, estos los saque de internet, aparte explica como funcionan y que hacen las funciones que estoy utilizando en estos ejemplos. </Noa>

### Uso con sorted

```py
lista = [(1, 'a'), (3, 'c'), (2, 'b')]
# Ordenar la lista por el segundo elemento de cada tupla
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)
# Salida: [(1, 'a'), (2, 'b'), (3, 'c')]
```

### Uso con filter()

```py
numeros = [1, 2, 3, 4, 5, 6]
# Filtrar solo los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
# Salida: [2, 4, 6]
```

### Uso con map()

```py
numeros = [1, 2, 3, 4]
# Elevar cada número al cuadrado
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)
# Salida: [1, 4, 9, 16]
