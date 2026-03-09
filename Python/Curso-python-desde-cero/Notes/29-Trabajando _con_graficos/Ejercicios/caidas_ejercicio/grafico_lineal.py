
import pandas as pd
# Libreria de visualización de datos
import matplotlib.pyplot as plt
# Librería de graficos estadisticos
import seaborn as sns

# df = dataFrame y con pd leemos el archivo csv
df = pd.read_csv("caidas.csv")
print(df)

# Con esta linea dibujamos el grafico indicando las abcisas y ordenadas del df
sns.lineplot(x = "fecha", y = "caidas", data = df)

# Dibujamos un punto en donde hubo mayor numero de caidas
plt.plot("01-09",17,"o")

# Este comando muestra el grafico
plt.show()