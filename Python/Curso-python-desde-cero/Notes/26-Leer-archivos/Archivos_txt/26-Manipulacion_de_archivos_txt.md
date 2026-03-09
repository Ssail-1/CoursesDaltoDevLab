
# Manipulación de archivos txt

Archivo => Contenedor de información

## Lectura basica del archivo completo

```py
# Abrimos el archivo y lo asignamos a una variable para trabajar con el.
archivo = open("carpeta\\archivo.txt", encoding = "UTF-8")

# Para leer el archivo completo
print(archivo.read())

# Cerrando el archivo
archivo.close()
```

- `encoding = "UTF-8"` para indicar la codificación con la que se va a leer el archivo.
- `read()` para poder leer el archivo.
- `close()` para cerrar el archivo una vez trabajado con el.

## Leyendo el archivo por lineas

Es importante tener en cuenta que una vez que se lee el archivo `read()`, ya no puede volver a ser leido, tiene que cerrarse para volver a leer. <Noa> porque? </Noa>

### Leyendo todas las lineas

```py
archivo = open("carpeta\\archivo.txt", encoding = "UTF-8")

# Nos devuelve un arreglo o lista con todas las lineas del archivo.
lineas = archivo.readlines()

archivo.close()
```

### Leyendo una sola linea o determinados caracteres

`linea = archivo.readline()`

Si le pasamos como argumento algun numero entero, nos devuelve la cantidad de caracteres indicada empezando por el inicio.

## Manipulando de forma optima `with open`

```py
with open("carpeta\\archivo.txt", encoding = "UTF-8") as archivo:
    # Si se abrio correctamente, se ejecuta este bloque
    contenido = archivo.read()

    print(contenido)

# No es necesario cerrar el archivo con with open
```
