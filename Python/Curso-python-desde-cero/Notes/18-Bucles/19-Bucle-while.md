
# 🔁 Bucle `while`

El bucle `while` ejecuta un bloque de código **mientras una condición sea verdadera (`True`)**.

Se usa cuando **no sabemos exactamente cuántas veces se repetirá el ciclo**, pero sí conocemos la condición que lo controla.

---

## 🧱 Estructura

```python
num = 0

while num < 5:
    print(num)
    num += 1
```

Salida:

```
0
1
2
3
4
```

📌 Cuando `num` llega a `5`, la condición `num < 5` deja de cumplirse y el bucle termina.

---

## ⛔ `break`

`break` **interrumpe inmediatamente el bucle**, aunque la condición del `while` siga siendo verdadera.

```python
contador = 0

while contador < 10:
    print(contador)

    if contador == 5:
        break

    contador += 1
```

Salida:

```
0
1
2
3
4
5
```

El ciclo se detiene cuando `contador` vale `5`.

---

## ⏭ `continue`

`continue` **salta a la siguiente iteración del bucle**, ignorando el resto del código dentro del ciclo en esa vuelta.

```python
num = 0

while num < 5:
    num += 1

    if num == 3:
        continue

    print(num)
```

Salida:

```
1
2
4
5
```

Cuando `num` vale `3`, el `print()` se omite y el ciclo continúa.

---

## 🧩 `else` en `while`

El bloque `else` se ejecuta **cuando el bucle termina normalmente**, es decir, cuando la condición deja de cumplirse.

No se ejecuta si el bucle termina con `break`.

```python
num = 0

while num < 3:
    print(num)
    num += 1
else:
    print("El bucle terminó")
```

Salida:

```
0
1
2
El bucle terminó
```

---

## 🧠 Resumen

| Elemento   | Función                                            |
| ---------- | -------------------------------------------------- |
| `while`    | Ejecuta código mientras la condición sea verdadera |
| `break`    | Termina el bucle inmediatamente                    |
| `continue` | Salta a la siguiente iteración                     |
| `else`     | Se ejecuta cuando el bucle termina normalmente     |

---
