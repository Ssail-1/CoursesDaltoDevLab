
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