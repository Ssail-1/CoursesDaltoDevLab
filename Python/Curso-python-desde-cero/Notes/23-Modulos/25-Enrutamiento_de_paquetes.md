
# Importando paquetes

Un paquete es una carpeta con mas modulos dentro y para acceder a todos ellos podemos importar la carpeta completa

Requisitos 

- La carpeta que sera paquete deberá tener un archivo llamado `__init__.py`, aunque no contenga nada.
- Los subpaquetes tambien deben contener el archivo `__init__.py`

<Noa> Que propiedad les da el archivo `__init__`?, en que los diferencia si lo tienen y no lo tienen?, hice un experimento y al quitarle el archivo mencionado y despues de importarlo, hice un print(type(paquete)) y me devolvio class module y con el init tambien, entonces me queda duda. 
- Como es para acceder a un paquete en otro nivel a donde me encuentro?, o en otro directorio por decirlo de otra forma</Noa>

```py
import paquete.subpaquete.modulo_subpaquete as m_sub

print(m_sub.funcion(argumento))
```
