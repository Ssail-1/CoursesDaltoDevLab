
# ➕ Operadores Aritméticos

Los operadores aritméticos se usan para realizar **operaciones matemáticas básicas** entre valores numéricos (enteros, flotantes, complejos, etc.).

| Operador | Descripción                          | Ejemplo  | Resultado |
| -------- | ------------------------------------ | -------- | --------- |
| `+`      | Suma                                 | `5 + 2`  | `7`       |
| `-`      | Resta                                | `5 - 2`  | `3`       |
| `*`      | Multiplicación                       | `5 * 2`  | `10`      |
| `/`      | División (siempre flotante)          | `5 / 2`  | `2.5`     |
| `//`     | División entera (descarta decimales) | `5 // 2` | `2`       |
| `%`      | Módulo (resto de la división)        | `5 % 2`  | `1`       |
| `**`     | Exponente                            | `5 ** 2` | `25`      |

---

## ⚙️ **Ejemplos prácticos**

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 💡 **Diferencias importantes con otros lenguajes**

| Concepto     | Python                                                   | Java                                                |
| ------------ | -------------------------------------------------------- | --------------------------------------------------- |
| División `/` | Devuelve **float**, aunque ambos sean enteros.           | Si ambos son enteros, devuelve **entero truncado**. |
| Exponente    | Se usa `**` (doble asterisco).                           | Se usa `Math.pow(a, b)`.                            |
| Módulo       | Igual que Java (`%`), pero también funciona con `float`. | No funciona con flotantes directamente.             |

Ejemplo:

```python
# Python
print(7 / 2)   # 3.5
print(7 // 2)  # 3

# Java
System.out.println(7 / 2);  // 3
```

---

## 🔢 **Combinación con variables**

Los operadores se pueden usar dentro de expresiones más complejas:

```python
x = 5
y = 2
resultado = (x ** 2 + y ** 3) / (x + y)
print(resultado)
```

---

## 🧮 **Prioridad de operadores**

El orden de evaluación sigue las reglas matemáticas (PEMDAS):

1. Paréntesis `()`
2. Exponentes `**`
3. Multiplicación, División, Módulo `*`, `/`, `//`, `%`
4. Suma y Resta `+`, `-`

Ejemplo:

```python
print(2 + 3 * 2)     # 8 (multiplica antes)
print((2 + 3) * 2)   # 10 (usa paréntesis primero)
```

---

## 🧠 **Resumen**

* Python maneja **automáticamente los tipos numéricos** (`int`, `float`, `complex`).
* La **división `/`** siempre devuelve un valor flotante.
* Usa `//` para divisiones enteras sin decimales.
* Los operadores siguen las **reglas de precedencia matemática**.
* Es posible combinar expresiones complejas sin declarar tipos explícitos.

---
