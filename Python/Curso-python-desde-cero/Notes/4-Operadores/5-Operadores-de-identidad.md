
# Operadores de identidad

Estos comparan **si dos variables apuntan al mismo objeto en memoria**, no si tienen el mismo valor.

| Operador | Descripción                                                                     | Ejemplo      | Resultado    |
| -------- | ------------------------------------------------------------------------------- | ------------ | ------------ |
| `is`     | Devuelve `True` si **ambos objetos son el mismo** (misma ubicación en memoria). | `a is b`     | True / False |
| `is not` | Devuelve `True` si **no son el mismo objeto** (diferente ubicación en memoria). | `a is not b` | True / False |

Ejemplo práctico:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)   # True → Tienen el mismo contenido
print(a is c)   # False → No son el mismo objeto en memoria
print(a is b)   # True  → b apunta al mismo objeto que a
```

🧩 **Resumen:**

* `==` → compara valores
* `is` → compara identidad (si son el mismo objeto en memoria)

---
