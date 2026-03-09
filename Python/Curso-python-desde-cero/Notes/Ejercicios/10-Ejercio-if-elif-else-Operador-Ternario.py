###
# 🧪 **Ejercicio para ti de Noa**
# 
# Crea un programa que simule el registro de usuario:
# 
# 1. Define una variable `usuario` y otra `clave`.
# 2. Usa `if` para verificar si coinciden con valores predefinidos (por ejemplo `"Luis"` y `"1234"`).
# 3. Muestra mensajes según el resultado (“Acceso concedido”, “Clave incorrecta”, “Usuario no encontrado”).
# 

# El usuario ingresa datos de inicio de sesión

usuario = 'Luis'
contraseña = '1234'

if usuario == "Luis":
    if contraseña == "1234":
        print(f'Bienvenido {usuario}!. Acceso Concedido')
    else:
        print("Contraseña incorrecta")
else:
    print('Usuario no encontrado')