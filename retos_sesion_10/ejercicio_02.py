"""El dueño de un restaurante de comida Mexicana ha decidido comprar un restaurante de comida Italiana y abrir un nuevo restaurante de comida fusion. 
La apertura esta a la vuelta de la esquina y aun no hay podido actualizar el Menu, Ayuda a actualizar su menu de platos disponibles

menu_mexicano: "Tacos", "Enchiladas", "Guacamole", "Tamales"
menu_italiano: "Pizza", "Pasta", "Lasagna", "Tiramisú"""

# Menús originales
menu_mexicano = ["Tacos", "Enchiladas", "Guacamole", "Tamales"]
menu_italiano = ["Pizza", "Pasta", "Lasagna", "Tiramisú"]

# Función para crear el menú de fusión
def crear_menu_fusion(menu_mexicano, menu_italiano):
    menu_fusion = []
    for plato_mexicano in menu_mexicano:
        for plato_italiano in menu_italiano:
            menu_fusion.append(f"{plato_mexicano} con {plato_italiano}")
    return menu_fusion

# Crear el menú de fusión
menu_fusion = crear_menu_fusion(menu_mexicano, menu_italiano)

# Imprimir el nuevo menú
print("Menú de Fusión Mexicana e Italiana:")
for plato in menu_fusion:
    print(plato)
