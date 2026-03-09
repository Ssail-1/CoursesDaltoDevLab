
# ⚖️ **Operadores de Comparación en Python**

Los operadores de comparación sirven para **comparar valores**.
El resultado **siempre es un valor booleano**: `True` o `False`.

---

## 🧩 **Tabla de operadores**

| Operador | Descripción       | Ejemplo  | Resultado |
| -------- | ----------------- | -------- | --------- |
| `==`     | Igual que         | `5 == 5` | ✅ `True`  |
| `!=`     | Diferente de      | `5 != 3` | ✅ `True`  |
| `<`      | Menor que         | `2 < 5`  | ✅ `True`  |
| `<=`     | Menor o igual que | `3 <= 3` | ✅ `True`  |
| `>`      | Mayor que         | `8 > 2`  | ✅ `True`  |
| `>=`     | Mayor o igual que | `7 >= 7` | ✅ `True`  |

---

## ⚙️ **Ejemplo práctico**

```python
a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= 10)  # True
print(b <= 5)   # True
```

---

## 💡 **Comparación de cadenas (strings)**

Python compara cadenas **carácter por carácter según el orden ASCII**:

```python
print("a" == "a")   # True
print("a" < "b")    # True
print("A" < "a")    # True (las mayúsculas valen menos en ASCII)
```

📌 *Tip:* Si quieres comparar cadenas sin importar mayúsculas/minúsculas, puedes usar `.lower()` o `.upper()`:

```python
print("Hola".lower() == "hola".lower())  # True
```

---

## 🧮 **Comparación entre tipos diferentes**

Python permite comparar distintos tipos, **pero no todos son compatibles**:

✅ Ejemplo válido:

```python
print(5 == 5.0)   # True → compara el valor numérico
```

❌ Ejemplo inválido:

```python
# print("5" > 3)  # Error → no se pueden comparar string con número
```

---

## 🔗 **Comparaciones encadenadas**

Una característica especial de Python es que puedes **encadenar comparaciones** sin repetir variables:

```python
x = 10
print(5 < x < 15)   # True
print(5 < x and x < 15)  # Equivalente
```

Esto hace el código más limpio y legible.

---

## ⚙️ **Comparación con listas, tuplas o sets**

Python compara estructuras **elemento por elemento**, hasta encontrar una diferencia:

```python
print([1, 2, 3] == [1, 2, 3])  # True
print((1, 2) < (1, 3))          # True → compara el segundo elemento
```

---

## 🧠 **Resumen**

* Devuelven siempre `True` o `False`.
* Sirven para comparar números, strings, o estructuras compatibles.
* Se pueden encadenar (por ejemplo, `0 < x <= 100`).
* Son fundamentales para **condicionales (`if`)** y **bucles (`while`, `for`)**.

---
