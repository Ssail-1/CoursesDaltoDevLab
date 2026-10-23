
import pandas as pd
# Libreria de visualización de datos
import matplotlib.pyplot as plt
# Librería de graficos estadisticos
import seaborn as sns

# df = dataFrame y con pd leemos el archivo csv
df = pd.read_csv("dispersion.csv")
print(df)

# barplot => Grafico de barras
sns.scatterplot(x = "TIEMPO", y = "DINERO", data = df)

# Este comando muestra el grafico
plt.show()