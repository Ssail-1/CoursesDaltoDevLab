
# Bucle for

En otros lenguajes los bucles for tienen otra estructura.
<Noa> Me gustaria que pusieras ejemplos de la estructura de los for en otros lenguajes como java, javascript y los que creas que son importantes, tanto sus for normales como sus for que se usan para recorrer estructuras como los for each o for in, que esos no los conosco pero que Dalto menciono </Noa>

Python simplifica los for, usando los for in

- Se pueden iterar listas y tuplas.

## Estructura

```py
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for animal in animales: # animal es donde se guardara cada item cuando valla recorriendo
    print(f'La variable es igual a: {animal}')
#Continua con la siguiente instrucción cuando ya no existan mas elementos
```

Salida

```py
Perro
Gato
Conejo
Pollito
```

## Iterando varias listas del mismo tamaño con Funcion: `zip()`

`zip()`

- Recibe como parametros las listas que va a recorrer

```py
numeros = [23, 43, 56, 64]
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for numeros, animales in zip(numeros, animales):
    print(f"Hay {numeros} {animales}")
```

## Iterando en rangos Funcion `range()`

range(`parametro1`, `parametro2`)

- El `parametro1` es de donde comienza
- El `parametro2` es donde termina

range(`Solo un parametro`)

- Comienza desde el 0 hasta llegar al parametro indicado

```py
for num in range(5, 10):
    print(num)
# Salida -> 5, 6, 7, 8, 9

for num in range(4):
    print(num)
# Salida -> 0, 1, 2, 3
```

## Forma correcta de recorrer una lista por su indice

```py
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for num in enumerate(animales):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

# U otra manera mas ELEGANTE: 

for i, valor in enumerate(animales):
     print(f"El indice es: {i} y el valor es: {valor}")

```

- `num` se convierte en una tupla que contendra (`indice`, `item_de_lista`)

### Desenpaquetado de `enumerate()`

- Al desempaquetar se tienen que considerar dos variables, la primera almacenara el indice `i` y la segunda desempaquetara el item `valor` correspondiente al indice.

## Usando `else` en el for

- El `else` siempre se ejecuta aunque no haya habido un recorrido dentro del for.
- Solo en caso de haber un `break` ya no se ejecuta

```py
animales = ["Perro", "Gato", "Conejo", "Pollito"]

for i, valor in enumerate(animales):
     print(f"El indice es: {i} y el valor es: {valor}")
else:
    print("El bucle termino") # Se imprime cuando termina el ciclo for
```

## Recorrido de Conjuntos

- En los conjuntos no se puede desempaquetar por indice y valor.
- Se puede usar la función `enumerate()`

## Iterando Diccionarios

### Iterando con función `items()`

- Con la función items() podemos obtener la clave y el item que contiene
- Sin el items, al pasarlo por el for, solo obtenemos la clave.

```py
diccionario = {
    "Nombre": "Luis"
    "Apellido": "Sánchez"
    "Carrera": "Ing. Software"
}

for datos in diccionario.items():
    key = datos[0] # Se pasa la llave que en listas sería el indice
    value = datos[1] # Se pasa el valor que contiene la llave
    print(f"La clave es: {key} y el valor es: {value})
```

## `continue` y `break` en el for

### continue

El `continue` en el for, se usa para brincar un recorrido en caso de ser necesarío. 

- Por tanto, todo lo que va despues de `continue` lo salta para seguir con el siguiente recorrido.

### break

El `break` interrumpe el ciclo y ya no continua o en otras palabras, se sale del ciclo for y tampoco ejecuta el `else` en caso de haber.

```py
frutas = ["manzana", "naranja", "ciruela", "durazno", "pera", "sandía", "banana"]

for fruta in frutas: 
    if fruta == "manzana": 
        continue # Porque soy alergico a la manzana, entonces no la comere
    print(f"Me voy a comer {fruta}")

    if fruta == "pera":
        print("me dolio mi panza, no puedo seguir comiendo...)
        break # Aqui termina el for
else:
    print("Ya me acabe las frutas") # pero por el break, no se ejecutara el else.
```

## Iterar cadena de texto

```py
cadena = "Hola Mundo"

for letra in cadena:
    print(letra) # Imprimira letra por letra
```

## for en ***una sola línea***

```py
lista_numeros = [1, 2, 3, 4, 5]

nueva_lista_numeros = [x*2 for x in lista_numeros]

print(nueva_lista_numero)
```
