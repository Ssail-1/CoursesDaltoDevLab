
# Escribir un programa que calcule la serie de fibonacci hasta un numero especifico de terminos.

def fibonacci_hasta(num):
    a, b = 0, 1
    fibonacci = [0]
    for i in range(num+2):
        if b > num: return fibonacci
        else:
            fibonacci.append(b)
            a, b = b, a + b

serie_fibonacci = fibonacci_hasta(int(input("Mostrar seríe fibonacci hasta...: ")))

print(serie_fibonacci) 