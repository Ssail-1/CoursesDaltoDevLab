
# Manipulación de archivos CSV

## Trabajando con `csv`

- Importamos `csv`
- Para leer los archivos usamos el metodo `reader()` de `csv`

Asi se ven los archivos `.csv`:
> "Encabezado 1", "Encabezado 2", "Encabezado 3"
> "Dato E1F1", "Dato E2F1", "Dato E3F1"  
> "Dato E1F2", "Dato E2F2", "Dato E3F2"

```py
import csv

with open("datos_csv.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
```


### Instalando Pandas

Es importante tener todo limpio y trabajar con entornos aislados.  
Por ello cree un entorno para pandas para poder trabajar sin afectar el entorno global.

`pip install pandas`
Istalar Jupiter Nootbooks

## Trabajando con `Pandas`

- `read_csv("datos.csv")` lee el archivo CSV
- `df` acronimo de DataFrame conceptualmente representa una hoja de calculo
- `df["Namecolumn"]` muestra la columna indicada

Renombrar los encabezados del csv  
- `df = pd.read_csv('datos.csv',`**` names = ["name", "lastname", "age"])`**

Obtener datos de una columna

- `columna = df["name"]`

```py
import pandas as pd

df = pd.read_csv("datos.csv", names = "name", "last_name", "age")
print

nombres = df["names"]
 print(names)
```

## Buenas practicas

- Al importar `pandas` le damos el alias **`pd`** por estandar.

## Slicing o segmentacion

Suponiendo una `cadena = '01234567890'`

- `cadena[3:7]` obtienen los valores de los indices 3 hasta el 6

## Ordenando de los registros

### Forma acendente

`df_acentente = df.sort_values("edad")`

### Forma decendente

`df_decendente = df.sort_values("edad", acending = False)`

## Concatenando 2 frames

- Se realiza con la función `concat([ItemLista,])` que recibe como parametro una lista. 

`df_concatenado = pd.concat([df, df2])`

## Accediendo a la primera fila con **`head()`**

- Como parametro recibe un int que represente cuantas filas quieres ver de arriba a abajo.
- Con el argumento 0 obtenemos los encabezados.

`primer_fila = head(parametro)`

## Accediendo a las ultimas filas con **`tail()`**

- Muestra las ultimas filas indicadas de arriba hacia abajo

`ultimas_filas = df.tail(parametro)`

## Accediendo a la cantidad de filas y columnas con `shape`

```py
# Devuelve una tupla (fila_int, columna_int)
filas_y_columnas = df.shape

# DESEMPAQUETANDO
filas, columnas = df.shape
```

## Obteniendo data estadistica del Dataframe

- Calcula y devuelve los datos estadisticos del frame

`df_info = df.describe()`

## Accediendo a lun elemento especifico del df con `loc`

- Nos permite acceder a un valor especifico dentro del dataframe.  
- loc[`fila`, `encabezado`]

`elemento_especifico_loc = df.loc[2, "edad"]`

## Accediendo a un elemento especifico con `iloc`

- `iloc[fila, Indice_de_encabezado]`
- la `i`loc es de index

`elemento_especifico_iloc = df.iloc[2,2]`

## Accediendo a todos los datos de una columna

- con slicing: loc[**`:`**,1]; significa que accede a todos los elementos
- Con el segundo parametro le indicamos que queremos la segunda columan

```py
# Accediendo con loc
apellidos = df.loc[:,"apellidos"]

# Accediendo con iloc
apellidos = df.iloc[:, 1]
```

## Accediendo a todas los datos de una fila

```py
# Accediendo con loc e iloc es igual
fila_3 = df.loc[2, :]
```

## Accediendo a filas con edad mayor que 30

```py
mayor_30 = df.loc[df[edad]>30, :]
```

# Ejercio

<Noa> En el siguiente ejercicio trabajamos con pandas y usamod funciones y metodos que no estan en lo anterior, puedes tambien documentarlos, si los entendí pero me gustaria que formaran parte de este apunte...</Noa>

```py
# Cambiar el tipo de dato de una columna

import pandas as pd

# Convertimos a string los datos de una columna
df = pd.read_csv("datos.csv")
df["edad"] = df["edad"].astype(str)

print(df)

#mostrar el tipo de dato del primer elemento de una columna edad
print(type(df["edad"][0]))
print("\n")

# Remplazando los datos "dalto" por "Maestro"
df["apellido"].replace("dalto","maestro", inplace = True)

# Eliminando las filas con datos vacios
df = df.dropna()

#Para eliminar columnas con datos faltantes
df = df.dropna(axis=1)

# Elimiando las filas con repetidas
df = df.drop_duplicates()

print(df)

# CREANDO UN CSV CON EL DATAFRAME RESULTANTE (LIMPIO)
df.to_csv("datos_limpios.csv")
```
