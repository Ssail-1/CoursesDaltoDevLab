
# Modificando Archivos txt

## Sobreescribiendo el archivo `'w'`

- `'w'` como segundo parametro para indicar que se **sobreescribira** el archivo.
- Con el permiso `'w'` si no encuentra el archivo, **lo crea**.
- `as archivo` asi asignamos nombre al archivo.

```py
with open("carpeta\\archivo.txt", 'w', encoding = "UTF-8") as archivo:
    #Sobre escribe el archivo, elimina lo que contiene e inserta el argumento
    archivo.write("argumento")
```

### Escribir varias lineas

> ```py
> archivo.writelines(["item_lista\n", "item_lista"])
> ```

- Cada componente o elemento es una linea en el archivo.
- Los saltos de línea se indican con `\n`
- Se pueden acumular las lineas con `writelines()`.

## Escribiendo el archivo `'a'`

- `'a'` de append y permite **escribir** sobre el archivo al final de este sin borrar el contenido anterior.

```py
with open('archivo_txt.txt', "a", encoding = "UTF-8") as archivo:
    
    # Forma normal
    for i in range(5):
        archivo.write(f"Linea {i + 1} agregada!\n")
    
    archivo.write("\n--------------------\n")
    
    # EN UNA SOLA LINEA
    
    # Con write lines, for dentro de parametro para formar el string y despues ejecuta writeLines creo xs
    archivo.writelines(f"Linea {i + 1} agregada\n" for i in range(5))
    
    archivo.write("\n--------------------\n")
    
    # Con write, for por fuera para que ejecune n veces el write
    [archivo.write(f"Linea {i + 1} agregada\n") for i in range(5)]
```
