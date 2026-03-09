
# 🧩 **Operadores de Asignación en Python**

## 📘 ¿Qué hacen?

Asignan un valor a una variable, o **modifican su valor actual combinando una operación** (como suma, resta, multiplicación, etc.) con la asignación.

El más básico es `=`, pero Python tiene varios operadores abreviados.

---

## ⚙️ **Tabla de operadores de asignación**

| Operador | Descripción               | Ejemplo   | Equivalente  |
| -------- | ------------------------- | --------- | ------------ |
| `=`      | Asigna un valor.          | `x = 5`   | —            |
| `+=`     | Suma y asigna.            | `x += 3`  | `x = x + 3`  |
| `-=`     | Resta y asigna.           | `x -= 3`  | `x = x - 3`  |
| `*=`     | Multiplica y asigna.      | `x *= 3`  | `x = x * 3`  |
| `/=`     | Divide y asigna.          | `x /= 3`  | `x = x / 3`  |
| `//=`    | División entera y asigna. | `x //= 3` | `x = x // 3` |
| `%=`     | Módulo y asigna.          | `x %= 3`  | `x = x % 3`  |
| `**=`    | Exponente y asigna.       | `x **= 3` | `x = x ** 3` |

---

## 🔢 **Ejemplo práctico**

```python
x = 10

x += 2   # 12
x -= 4   # 8
x *= 3   # 24
x /= 2   # 12.0
x //= 5  # 2.0
x **= 3  # 8.0
```

📌 **Importante:**
Cuando usas `/=` el resultado siempre pasa a ser **float**, aunque antes fuera `int`.

---

## 💡 **Uso común en bucles**

Los operadores de asignación se usan mucho en iteraciones o acumulaciones:

```python
suma = 0
for i in range(1, 6):
    suma += i   # suma = suma + i

print(suma)  # 15
```

O para contadores:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## ⚙️ **Comparación con Java**

| Concepto               | Python                     | Java                                  |
| ---------------------- | -------------------------- | ------------------------------------- |
| Asignación básica      | `x = 5`                    | `int x = 5;`                          |
| Incremento abreviado   | `x += 1`                   | `x += 1;`                             |
| No existen `++` o `--` | Se usa `x += 1` o `x -= 1` | `x++`, `--x`, etc. sí existen en Java |

💬 En resumen: Python **no tiene operadores de incremento o decremento directos** (`++`, `--`), lo que evita ambigüedades en expresiones complejas.

---

## 🧠 **Resumen**

* `=` asigna directamente un valor.
* `+=`, `-=`, `*=` y demás combinan una operación y una reasignación.
* No existen `++` ni `--`.
* Son muy útiles para simplificar código en bucles y operaciones acumulativas.

---
