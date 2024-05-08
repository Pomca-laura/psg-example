# ¿El cuadrado de 123 se encuentra en el siguiente rango? [N > 0 & N < 20000]
# Calcular el cuadrado de 123
cuadrado_123 = 123 ** 2

# Verificar si el cuadrado se encuentra en el rango [0, 20000)
esta_en_rango = cuadrado_123 > 0 and cuadrado_123 < 20000

# Imprimir el resultado
print("¿El cuadrado de 123 está en el rango [0, 20000)?:", esta_en_rango)
