
import pandas as pd
# Libreria de visualización de datos
import matplotlib.pyplot as plt
# Librería de graficos estadisticos
import seaborn as sns

# df = dataFrame y con pd leemos el archivo csv
df = pd.read_csv("bigotes.csv")
print(df)

# barplot => Grafico de barras
sns.boxplot(x = "CATEGORIA", y = "VALOR", data = df)


# Este comando muestra el grafico
plt.show()