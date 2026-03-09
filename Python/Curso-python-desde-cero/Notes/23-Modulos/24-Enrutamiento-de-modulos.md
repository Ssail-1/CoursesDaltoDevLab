
# Enrutamiento de modulos

## Acceder al modulo en una carpeta en el mismo nivel

```py
import carpeta.modulo 

# Al llamar una función
carpeta.modulo.funcion(argumento)
```

## Si el modulo se encontrara fuera

<Noa> - Que es sys?
Tambien dale orden a este tema aparte de complementarlo, porfa Noa.</Noa>

Tenemos que hacer uso del modulos `sys` quien es el que contiene el acceso a los modulos nativos de python y por ende quien nos puede dar acceso a integrar nuestros propios modulos.

```py
import sys
sys.path.append("c:\\Dirección-del-modulo\\modulo")
import modulo as m

print(m.funcion("argumento"))
```

<Noa>¿Los directorios que agregamos a sys, son globales para todos los programas?, en cuestión a que si agrego una dirección en un modulo actual, si despues trabajo en otro modulo tambien voy a tener acceso a la dirección que agregue sin tener que volver a agregar la dirección.</Noa>

### Accediendo a los modulos de `sys`

`sys.builtin_module_names`

- Tenemos que crear modulos que no coincidan con el nombre de los built_in ya que python le da prioridad a los nativos.

### Como Saber donde estan alojados los modulos

`sys.path`

<Noa>- Que es path?</Noa>
