# Empezemos, haber que sale
# Estoy inseguro...

from matplotlib import pyplot as plt
from matplotlib_venn import venn3
import os
from datetime import datetime

print("=== DEMOSTRACIÓN DE CONJUNTOS CON DIAGRAMA DE VENN ===\n")

# Pedimos los datos al usuario
A_input = input("Ingresa los elementos del conjunto A separados por comas: ")
B_input = input("Ingresa los elementos del conjunto B separados por comas: ")
C_input = input("Ingresa los elementos del conjunto C separados por comas: ")

# Convertimos las cadenas en conjuntos
A = set(A_input.replace(" ", "").split(","))
B = set(B_input.replace(" ", "").split(","))
C = set(C_input.replace(" ", "").split(","))

print("\n--- RESULTADOS ---")
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")

# Operaciones básicas
print("\nUnión (A ∪ B ∪ C):", A | B | C)
print("Intersección (A ∩ B ∩ C):", A & B & C)
print("Diferencia (A - B - C):", A - B - C)
print("Diferencia simétrica (A △ B △ C):", A ^ B ^ C)

# Crear el diagrama
venn3([A, B, C], set_labels=("A", "B", "C"))
plt.title("Diagrama de Venn - Conjuntos A, B y C")

# Crear carpeta de salida si no existe
#output_dir = "output_diagramas"
#os.makedirs(output_dir, exist_ok=True)

# Crear nombre de archivo con fecha y hora
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"venn_diagrama_{timestamp}.png"
file_path = os.path.join(output_dir, file_name)

# Guardar el gráfico en la carpeta
plt.savefig(file_path, dpi=300, bbox_inches="tight")
print(f"\n✅ Diagrama guardado como: {file_path}")

# Mostrar la figura
plt.show()

