
# Funciones Integradas (Build in)

## min() y max()

- Reciben como parametros una lista o tupla con datos numericos dentro
- Devuelven el dato con mayor o menor valor.

## round()

- Por defecto round() redondea eliminando los decimales
- Como parametros le pasamos el numero a redondear y al segundo el numero de decimales que queremos.
  - round(`numero`, `numero de decimales`)

## bool()

- Como parametro le pasamos un dato numerico

Funcion?

- Retorna `False` si:
  - El numero es 0
  - La variable esta vacia
  - Si contiene un False
  - No hay nada (`none`)
- Retorna `True` si:
  - Contiene numeros distintos a 0
  - Contiene True
  - Contiene Cadenas
  - Que no tenga datos vacios

## all()

- Como parametros se le pasa un iterable como lista o tupla
- Funciona como `bool()` y retorna `True` si todos los valores cumplen la condición de `bool()`.

## sum()

- Devuelve la suma de todos los numeros de un iterable.
