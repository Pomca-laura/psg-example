# Comparar los números 123 y 890, comprobar si tienen la misma paridad ambos pares o ambos impares

# Números para comparar
numero1 = 123
numero2 = 890

# Verificar si ambos números tienen la misma paridad
mismo_paridad = (numero1 % 2 == numero2 % 2)

# Imprimir el resultado
if mismo_paridad:
    print("Ambos números tienen la misma paridad.")
else:
    print("Los números tienen diferente paridad.")
