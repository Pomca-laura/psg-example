"""Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar la cantidad de lugares que han visitado
Cada uno quiere saber en que parte del mundo ha estado el otro que el no haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}

Ahora quieren saber en que ciudades han estado ambos mochileros"""

# Listas de lugares visitados por cada mochilero
mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Perú", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sídney", "Argentina", "Brasil", "Panamá", "Bolivia"}

# Lugares únicos visitados por cada mochilero
lugares_unicos_a = mochilero_a - mochilero_b
lugares_unicos_b = mochilero_b - mochilero_a

# Lugares visitados por ambos mochileros
lugares_comunes = mochilero_a & mochilero_b

# Imprimir resultados
print("Lugares que mochilero A ha visitado y mochilero B no:")
print(lugares_unicos_a)

print("\nLugares que mochilero B ha visitado y mochilero A no:")
print(lugares_unicos_b)

print("\nLugares que ambos mochileros han visitado:")
print(lugares_comunes)
