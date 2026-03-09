# Tener 2 listas; nombre y apellidos
# Lo hare dinamico...
nombres = [""]
with open("archivo.txt", "w") as archivo_CSV:
    archivo_CSV.write("Datos de los integrantes\n\n")
    integrantes = int(input("Cuantos integrantes vas ingresar?: "))
    for i in range(integrantes):
        name = input("Nombre de integrante: ")
        apellido = input(f"Apellido del integrante {name}? ")
        archivo_CSV.writelines(f"Nombre: {name}\nApellido: {apellido}\n-----------------------\n")