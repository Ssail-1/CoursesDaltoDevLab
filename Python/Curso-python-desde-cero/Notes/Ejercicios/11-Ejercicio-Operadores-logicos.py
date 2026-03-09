'''
## 🧪 **Ejercicio para ti de Noa**

Haz un programa que simule el acceso a un sistema, pero con **más condiciones**:

1. Pide tres variables (pueden ser fijas por ahora):

   * `usuario`, `contraseña`, y `activo` (booleano).
2. Solo debe conceder acceso si el usuario es `"Luis"`, la contraseña es `"1234"`, **y además el usuario está activo**.
3. Si el usuario o la contraseña son incorrectos, muestra mensajes específicos.
4. Si el usuario está inactivo, muestra `"Cuenta inactiva"`.

---
'''

usuario = 'Luis'
contraseña = '1234'
activo = False

if (usuario == "Luis") and (contraseña == "1234") and activo:
    print(f'Bienvenido {usuario}!. Acceso Concedido')
elif not(usuario == "Luis") and contraseña == "1234":
    print('Usuario no encontrado')
elif not(contraseña == "1234") and usuario == "Luis":
    print("Contraseña incorrecta")
else:
    print("Cuenta Inactiva")


# Como Noa esperaba que lo hiciera

if not activo:
    print("Cuenta inactiva")
elif usuario != "Luis":
    print("Usuario no encontrado")
elif contraseña != "1234":
    print("Contraseña incorrecta")
else:
    print(f"Bienvenido {usuario}!. Acceso concedido")

'''
Ventajas de esta versión

Más fácil de leer (una sola condición por bloque).

Evalúa de arriba a abajo sin redundancias.

Escalable: podrías añadir fácilmente nuevos casos (bloqueado, intentos fallidos, etc.).

Sigue el principio de “fail fast” (detectar errores cuanto antes).
'''
