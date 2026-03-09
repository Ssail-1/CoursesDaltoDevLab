
# 🧩 **Métodos de Cadenas en Python (`str`)**

Las cadenas en Python (`str`) tienen **métodos integrados** para manipular, buscar, analizar y transformar texto.
No modifican la cadena original (son **inmutables**): cada método devuelve una **nueva cadena**.

---

> `dir(objeto)`

- Devuelve la lista de atributos válidos del objeto pasado.
- Permite explorar las características de un objeto, como métodos, atributos y propiedades.
- Es útil para descubrir qué métodos o atributos están disponibles en un objeto o módulo, especialmente al trabajar con bibliotecas o clases nuevas así como para depurar codigo.

## 🔤 **Cambiar formato del texto**

| Método          | Descripción                                   | Ejemplo                | Resultado      |
| --------------- | --------------------------------------------- | ---------------------- | -------------- |
| `.upper()`      | Convierte todo el texto a mayúsculas.         | `"hola".upper()`       | `"HOLA"`       |
| `.lower()`      | Convierte todo el texto a minúsculas.         | `"Hola".lower()`       | `"hola"`       |
| `.capitalize()` | Primera letra en mayúscula, resto minúsculas. | `"hOLA".capitalize()`  | `"Hola"`       |
| `.title()`      | Primera letra de cada palabra en mayúscula.   | `"hola mundo".title()` | `"Hola Mundo"` |
| `.swapcase()`   | Invierte mayúsculas y minúsculas.             | `"HoLa".swapcase()`    | `"hOlA"`       |

---

## 🔍 **Búsqueda y posición**

| Método             | Descripción                                                          | Ejemplo                          | Resultado |
| ------------------ | -------------------------------------------------------------------- | -------------------------------- | --------- |
| `.find("sub")`     | Devuelve la posición donde aparece la subcadena (o `-1` si no está). | `"python".find("th")`            | `2`       |
| `.index("sub")`    | Igual que `find()`, pero lanza error si no la encuentra.             | `"python".index("th")`           | `2`       |
| `.count("sub")`    | Devuelve cuántas veces aparece una subcadena.                        | `"banana".count("a")`            | `3`       |
| `.startswith("x")` | Verifica si la cadena comienza con “x”.                              | `"Hola".startswith("H")`         | `True`    |
| `.endswith("x")`   | Verifica si la cadena termina con “x”.                               | `"archivo.txt".endswith(".txt")` | `True`    |

---

## 🔠 **Validación de contenido**

| Método       | Descripción                                    | Ejemplo                  | Resultado |
| ------------ | ---------------------------------------------- | ------------------------ | --------- |
| `.isalpha()` | `True` si solo contiene letras (a–z, A–Z).     | `"Python".isalpha()`     | `True`    |
| `.isdigit()` | `True` si solo contiene dígitos.               | `"123".isdigit()`        | `True`    |
| `.isalnum()` | `True` si solo contiene letras o números.      | `"abc123".isalnum()`     | `True`    |
| `.isspace()` | `True` si solo contiene espacios.              | `"   ".isspace()`        | `True`    |
| `.islower()` | `True` si todos los caracteres son minúsculas. | `"hola".islower()`       | `True`    |
| `.isupper()` | `True` si todos los caracteres son mayúsculas. | `"HOLA".isupper()`       | `True`    |
| `.istitle()` | `True` si cada palabra comienza con mayúscula. | `"Hola Mundo".istitle()` | `True`    |

---

## ✂️ **Modificación y limpieza**

| Método               | Descripción                          | Ejemplo                      | Resultado  |
| -------------------- | ------------------------------------ | ---------------------------- | ---------- |
| `.replace("a", "b")` | Reemplaza un valor por otro.         | `"banana".replace("a", "o")` | `"bonono"` |
| `.strip()`           | Elimina espacios en ambos extremos.  | `" hola ".strip()`           | `"hola"`   |
| `.lstrip()`          | Elimina espacios del lado izquierdo. | `" hola".lstrip()`           | `"hola"`   |
| `.rstrip()`          | Elimina espacios del lado derecho.   | `"hola ".rstrip()`           | `"hola"`   |

---

## 🧮 **Dividir y unir cadenas**

| Método            | Descripción                                         | Ejemplo                     | Resultado                |
| ----------------- | --------------------------------------------------- | --------------------------- | ------------------------ |
| `.split()`        | Separa la cadena por espacios o por un delimitador. | `"uno dos tres".split()`    | `['uno', 'dos', 'tres']` |
| `.split(",")`     | Divide usando una coma.                             | `"a,b,c".split(",")`        | `['a', 'b', 'c']`        |
| `",".join(lista)` | Une una lista en una sola cadena.                   | `",".join(['a', 'b', 'c'])` | `"a,b,c"`                |

---

## 🔢 **Otros métodos útiles**

| Método         | Descripción                                              | Ejemplo             | Resultado      |
| -------------- | -------------------------------------------------------- | ------------------- | -------------- |
| `.len(cadena)` | Función que cuenta caracteres (no método).               | `len("Python")`     | `6`            |
| `.center(n)`   | Centra el texto en un ancho definido.                    | `"hola".center(10)` | `'   hola   '` |
| `.zfill(n)`    | Rellena con ceros al inicio hasta llegar a n caracteres. | `"42".zfill(5)`     | `'00042'`      |

---

## ⚙️ **Ejemplo práctico**

```python
nombre = "  luis isaías  "
print(nombre.strip().title())  # "Luis Isaías"

frase = "Aprender Python es divertido"
print(frase.replace("divertido", "poderoso"))  # "Aprender Python es poderoso"

cadena = "correo@gmail.com"
print(cadena.endswith(".com"))  # True
```

---

## 🧠 **Resumen**

* Las cadenas son **inmutables** (no cambian, devuelven una nueva versión).
* Los métodos más usados: `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `find()`.
* Se pueden encadenar:

  ```python
  texto = " hola mundo ".strip().capitalize()
  print(texto)  # "Hola mundo"
  ```

---
