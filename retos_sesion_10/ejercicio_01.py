"""Anita y Pepito llevan saliendo juntos por 4 semanas, 
cada vez que salen van a comer a una plaza de comidas. 
Ambos quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 

A continuación tienes los platos de comida que ambos han ido pidiendo a los largo de sus citas:
Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa

Si la cantidad platos de comida que tienen en comunes mayor a 50% entonces ambos seguirán saliendo"""

# Listas de platos de comida de Anita y Pepito
platos_anita = ["Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"]
platos_pepito = ["Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"]

# Encontrar los platos en común usando conjuntos
platos_anita_set = set(platos_anita)
platos_pepito_set = set(platos_pepito)

platos_en_comun = platos_anita_set.intersection(platos_pepito_set)

# Calcular el número de platos en común y el total de platos únicos
numero_platos_en_comun = len(platos_en_comun)
total_platos_unicos = len(platos_anita_set.union(platos_pepito_set))

# Calcular el porcentaje de platos en común
porcentaje_en_comun = (numero_platos_en_comun / total_platos_unicos) * 100

# Determinar si la compatibilidad es mayor al 50%
compatibles = porcentaje_en_comun > 50

# Mostrar resultados
print(f"Platos de Anita: {platos_anita}")
print(f"Platos de Pepito: {platos_pepito}")
print(f"Platos en común: {list(platos_en_comun)}")
print(f"Porcentaje de platos en común: {porcentaje_en_comun:.2f}%")

if compatibles:
    print("Anita y Pepito seguirán saliendo.")
else:
    print("Anita y Pepito no seguirán saliendo.")
