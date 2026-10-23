
import pandas as pd
# Libreria de visualización de datos
import matplotlib.pyplot as plt
# Librería de graficos estadisticos
import seaborn as sns

# df = dataFrame y con pd leemos el archivo csv
df = pd.read_csv("cofla_ingresos.csv")
print(df)

# barplot => Grafico de barras
sns.barplot(x = "FUENTE", y = "INGRESOS", data = df)

#Obteniendo el total de ingresos
total_ingresos = df["INGRESOS"].sum()
print(f"El total de ingresos es de: {total_ingresos}")

# Este comando muestra el grafico
plt.show()