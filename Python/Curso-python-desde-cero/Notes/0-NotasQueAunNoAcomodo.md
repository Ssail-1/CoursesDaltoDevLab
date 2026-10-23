

### Imprimir salidas

> `print()`

### Comentarios

Los comentarios se inician con el caracter **#**

```py
    # Esto es un comentario

    """
    Esto tambien es un comentario
    Y puede ser multilinias
    Hasta cerrar las
    triples comillas
    """
```

### Conocer el tipo de dato

```py
tipo_de_dato = type(dato)
```

## 🧭 **Herramienta útil: `dir(objeto)`**

> `dir(objeto)`

* Devuelve una **lista de los atributos válidos** del objeto pasado.
* Permite **explorar las características** de un objeto, como sus métodos, atributos y propiedades.
* Es muy útil para **descubrir qué métodos o atributos** están disponibles en un objeto o módulo, especialmente cuando trabajas con **librerías nuevas o clases personalizadas**.
* También se usa para **depurar código** o investigar cómo funcionan estructuras internas de Python.

Ejemplo:

```python
lista = [1, 2, 3]
print(dir(lista))
```

Salida (acortada):

```
['__add__', '__class__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort', ...]
```

💡 Esto te permite ver *todos los métodos disponibles* para cualquier objeto, no solo las listas.

---

## que onda con esto

### lo use al trabajar con pandas
cambie el tipo de dato que almacenaba de int a str
- astype(str)

Es **"Casteo"**
