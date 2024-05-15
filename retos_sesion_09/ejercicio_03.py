"""Crear una lista de personas con 10 nombres de personas
1. Obtener una sub lista de 2 a 7
2. Buscar si existe el nombre "Jhon" en la lista original
3. Ordenar la sub lista alfabéticamente
4. Ordenar la lista original alfabéticamente de forma descendente"""

lista = ["Laura", "Catalina", "Luz", "Marina", "Liduvina", "Amparo", "Aura", "Dora", "Alicia", "Martha"]
print(lista)

lista_sub = lista[2:7]
print(lista_sub)

print("Jhon" in lista)

lista_sub.sort()
print(lista_sub)

lista_sub.sort(reverse=True)
print(lista_sub)


