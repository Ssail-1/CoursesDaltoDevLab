
# EJERCICIO 1
# Obtener:
#   a) Diferencia en porcentaje entre el curso actual y:
#       - el más rapido de otros cursos
#       - el más lento de otros cursos
#       - el promedio de los cursos
#   b) Porcentaje de material inservible que se reduce en:
#       - el curso promedio de los cursos
#       - el curso actual (este curso)
#   c) Ver 10  horas de este cursos a cuantas horas de otros cursos equivale?, ¿Y al réves?


# a)

# tiempo de cursos efectivos
dalto_curso = 1.5
otros_cursos_min = 2.5
otros_cursos_promedio = 4
otros_cursos_max = 7

# Calculos
diferencia_con_max = 100 - dalto_curso *1000 // otros_cursos_max / 10

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100

diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# Mostrando las diferencias de duración
print(f"""
      El curso de Dalto en porcentaje dura menos que:
      {diferencia_con_max}% con el más rápido
      {diferencia_con_min}% con el mas lento
      {diferencia_con_promedio}% con el promedio""")

#b

# tiempo de cursos en crudo
dalto_crudo_curso = 3.5
otros_cursos_crudo_promedio = 5

# Calculos
tiempo_vacio_promedio = 100 - otros_cursos_promedio / otros_cursos_crudo_promedio *100

tiempo_vacio_dalto = 100 - dalto_curso * 1000 // dalto_crudo_curso / 10

# Mostrando la cantidad de tiempo que se remueve

print(f"Un curso promedio elimina un  {tiempo_vacio_promedio}% de tiempo vacio")

print(f"El curso de dalto elimina  {tiempo_vacio_dalto}% de tiempo vacio")


# c)

# Mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10}")

print(f"Ver 10 horas de este curso equivale a ver { dalto_curso * 100 // otros_cursos_promedio / 10}")
