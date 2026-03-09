
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