
# Ejercicio 2

# a) Pedirle al usuario que diga cualquier texto real y: 
#   - Calcular cuanto tardaría en decir esa frase
#   - ¿Cuantas palabras dijo?

# b) Si se tarda mas de 1 minuto
#   - Decirle: "para flaco, tampoco te pedí un testamento".

# c) Dalto habla un 30% más rápido:
#   - ¿Cuanto tardaría él en decirlo?


# Pedirle al usuario una frase
frase = input("Dime una frase y te calculo cuanto tardarías si tuvieras que decirla: ")

#calculando cantidad de palabras
cantidad_de_palabras = len(frase.split(" "))

# Mostrando a)
print(f"Dijiste {cantidad_de_palabras} palabras, y te tardarías {cantidad_de_palabras/2} segundos en decirlo")

# Calculando tiempo en que lo diría
tiempo_user = cantidad_de_palabras / 2

# Mostrando b) si tarda mas de 1 minuto
if tiempo_user > 60:
    print("Para flaco, tampoco te pedí un testamento")

# c) Calculando cuanto tardaría Dalto en decirlo
print(f"Dalto tardaria {cantidad_de_palabras / 2.6} segundos en decirlo")
