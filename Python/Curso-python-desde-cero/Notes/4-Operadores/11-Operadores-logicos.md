
# 🔗 **Operadores Lógicos en Python**

Estos operadores permiten **combinar condiciones** en los condicionales `if`, `elif` o `while`, para tomar decisiones más complejas.

---

## 🧩 **Operadores lógicos**

| Operador | Descripción                                                  | Ejemplo                | Resultado |
| -------- | ------------------------------------------------------------ | ---------------------- | --------- |
| `and`    | Devuelve `True` si **todas las condiciones** son verdaderas. | `(5 > 2) and (10 > 5)` | ✅ `True`  |
| `or`     | Devuelve `True` si **al menos una condición** es verdadera.  | `(5 > 10) or (10 > 5)` | ✅ `True`  |
| `not`    | Invierte el valor lógico.                                    | `not (5 > 2)`          | ❌ `False` |

---

## ⚙️ **Ejemplos prácticos**

### 1️⃣ Usando `and`

```python
edad = 20
licencia = True

if edad >= 18 and licencia:
    print("Puedes conducir")
else:
    print("No cumples los requisitos")
```

---

### 2️⃣ Usando `or`

```python
nota = 60
asistencia = 85

if nota >= 70 or asistencia >= 80:
    print("Aprobado por nota o asistencia")
else:
    print("Reprobado")
```

---

### 3️⃣ Usando `not`

```python
bloqueado = False

if not bloqueado:
    print("Acceso permitido")
else:
    print("Usuario bloqueado")
```

---

## 🧮 **Combinación de operadores**

Puedes mezclarlos para crear condiciones más precisas:

```python
edad = 25
nacionalidad = "mexicana"
licencia = True

if (edad >= 18 and licencia) or nacionalidad == "mexicana":
    print("Autorizado")
else:
    print("No autorizado")
```

📌 Python evalúa de izquierda a derecha y respeta **prioridades**:

1. `not`
2. `and`
3. `or`

💡 Usa paréntesis para que la condición sea clara, especialmente si es larga.

---

## 🧠 **Resumen**

* `and` → todas las condiciones deben ser verdaderas.
* `or` → basta con que una lo sea.
* `not` → invierte el valor lógico.
* Pueden combinarse y agruparse con paréntesis.
* Son esenciales para condicionales y bucles complejos.

---
