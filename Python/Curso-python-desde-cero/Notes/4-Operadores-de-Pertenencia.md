
# Operadores de pertenencia **(Membership Operators)**

## in

Se utiliza para verificar si un valor está presente en una secuencia **(lista, tupla, cadena, etc)**.

- Devuelve `True` o `False`

## not in

Función viceversa de in.

Estos sirven para **comprobar si un valor está o no dentro de una secuencia** (lista, tupla, string, conjunto, diccionario, etc.).

| Operador | Descripción                                                       | Ejemplo             | Resultado |
| -------- | ----------------------------------------------------------------- | ------------------- | --------- |
| `in`     | Devuelve `True` si el valor **está presente** en la secuencia.    | `"a" in "hola"`     | ✅ `True`  |
| `not in` | Devuelve `True` si el valor **NO está presente** en la secuencia. | `"z" not in "hola"` | ✅ `True`  |

💡 Usarlos con listas, tuplas o diccionarios:

```python
lista = [1, 2, 3]
print(2 in lista)      # True
print(4 not in lista)  # True

dic = {"nombre": "Luis", "edad": 21}
print("nombre" in dic)     # True (revisa las CLAVES, no los valores)
print("Luis" in dic)       # False
```