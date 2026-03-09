
# Modulos

Los modulos son cualquier archivo con extención `.py`, existen los modulos:

- Internos, propios de python
- De terceros proporcionados por empresas
- Propios, creados por nosotros

## Importar modulos `import`

Para importar modulos tenemos que indicar la palabra reservada `import` seguido de la dirección del modulo

- Si el modulo se encuentra al mismo nivel de donde se esta importando, solo vasta llamarlo con el nombre.

```py
# Con ello se importa todo el contenido del modulo
import direccion_del_modulo

# Usando las funciones de los modulos
resultado = direccion_del_modulo.funcion(argumento)
```

## Asignandole un alias a los modulos

- Se usa la palabra reservada `as` para darle otro nombre al modulo y sea mas facil llamarlo

```py
import direccion_del_modulo as dm

# llamando una función del modulo
resultado = dm.funcion(argumento_1, argumento_2, etc)
```

## Importar solo algunas funciones del modulo

- Se usa la palabra reservada `from` seguido del modulo y despues indicar con `import` las funciones que se van a importar.
- Tambien se pueden renombrar las funciónes con `as`.

```py
from modulo import función1 as f1, funcion2, etc
# Se pueden importar tantas funciones se necesiten y al llamarlas no es necesario crear un objeto.

# Ejemplo
resultado = f1(argumento)
```