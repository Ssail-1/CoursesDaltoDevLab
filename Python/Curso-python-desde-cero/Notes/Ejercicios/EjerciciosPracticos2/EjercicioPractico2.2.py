
# Crear una funcion que nos devuelva los numeros primos anteriores al numero ingresado

# Entre el 0 y el argumento que le pasamos.

def es_primo(num):
    for i in range(2, num-1):
        if num % i == 0: return False
    return True

def primos_hasta(num):
    primos = list()
    for i in range(2, num + 1):
        resultado = es_primo(i)
        if resultado: primos.append(i)
    return primos

num_primos = primos_hasta(int(input("Ingresa la cantidad de num primos que deseas saber: ")))

print(num_primos)
    