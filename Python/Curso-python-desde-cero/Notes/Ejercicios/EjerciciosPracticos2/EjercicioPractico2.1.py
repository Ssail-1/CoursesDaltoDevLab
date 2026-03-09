
# Ejercicio
# El maestro no fue y los alumnos organizaran quien es el maestro y el asistente.

# A) Pedir la edad y nombre de los compañeros que vinieron a clases y ordenar de menor a mayor

# B) El mayor es el profesor y el menor es el asistente: ¿Quien es quien?

compañeros = list()

def obtener_compañeros(cantidad):
    for i in range(cantidad):
        nombre = input("Nombre del compañero: ")
        edad = int(input(f"Edad del compañero {nombre}: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key = lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return profesor, asistente

profesor, asistente = obtener_compañeros(5)

print(f"El profesor es: {profesor} y su asistente es: {asistente}")