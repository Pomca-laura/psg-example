# Tienes una tienda de abarrotes y tienes dos listas una con los productos que tienes y otra con los precios

productos = ["Leche", "Pan", "Huevos"]
print(productos)

precios = [3000, 5000, 20000]
print(precios)

# 1. Agregar 5 productos nuevos al final de las listas

productos.extend(["Uvas", "Sandia", "Queso", "Pasta", "Aceite"])
print(productos)

precios.extend([7000, 10000, 11000, 6000, 30000])
print(precios)

# 2. Eliminar el producto con el nombre "Leche" de las listas

productos.remove("Leche")
print(productos)

# 3. ¿Cuanto cuesta el producto "Pan" y "Huevo"?

print(f"El pan vale $", precios[0] , "y los huevos valen $", precios[1])

# 4. ¿Cual es el producto más caro y más barato?

print(max(precios))
print(min(precios))

# 5. ¿Cuántos productos tienes en total?

print(len(productos))

# 6. ¿Cuanto cuesta el total de los productos?

print(sum(precios))

# 7. Ordena los productos alfabéticamente y precios si es posible

print(productos.sort())
print(precios.sort())

# 8. Eliminar todos los productos de las listas

productos.clear()
print(productos)











