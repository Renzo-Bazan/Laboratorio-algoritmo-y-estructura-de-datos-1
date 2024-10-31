import os

# Ruta de la carpeta de recetas
ruta_recetas = "C:/Proyecto Dia 6/recetas"

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar las categorías disponibles
def mostrar_categorias():
    categorias = [cat for cat in os.listdir(ruta_recetas) if os.path.isdir(os.path.join(ruta_recetas, cat))]
    if categorias:
        print("Categorías disponibles:")
        for i in range(len(categorias)):
            print(f"{i + 1}. {categorias[i]}")
        return categorias
    else:
        print("No hay categorías disponibles.")
        return []

# Opción 1: Leer una receta
def opcion_leer_receta():
    categorias = mostrar_categorias()
    if categorias:
        eleccion_categoria = int(input("Elige una categoría por su número: ")) - 1
        categoria_elegida = categorias[eleccion_categoria]
        ruta_categoria = os.path.join(ruta_recetas, categoria_elegida)
        recetas = [rec for rec in os.listdir(ruta_categoria) if os.path.isfile(os.path.join(ruta_categoria, rec))]

        if recetas:
            print("Recetas disponibles:")
            for i in range(len(recetas)):
                print(f"{i + 1}. {recetas[i]}")
            eleccion_receta = int(input("Elige una receta por su número para leer: ")) - 1
            receta_elegida = recetas[eleccion_receta]
            with open(os.path.join(ruta_categoria, receta_elegida), 'r') as file:
                print("\nContenido de la receta:")
                print(file.read())
        else:
            print("No hay recetas en esta categoría.")

# Opción 2: Crear una receta
def opcion_crear_receta():
    categorias = mostrar_categorias()
    if categorias:
        eleccion_categoria = int(input("Elige una categoría por su número: ")) - 1
        categoria_elegida = categorias[eleccion_categoria]
        nombre_receta = input("Escribe el nombre de la receta: ") + ".txt"
        contenido_receta = input("Escribe el contenido de la receta:\n")

        ruta_receta = os.path.join(ruta_recetas, categoria_elegida, nombre_receta)
        with open(ruta_receta, 'w') as file:
            file.write(contenido_receta)
        print("Receta creada correctamente.")

# Opción 3: Crear una categoría
def opcion_crear_categoria():
    nombre_categoria = input("Escribe el nombre de la nueva categoría: ")
    ruta_categoria = os.path.join(ruta_recetas, nombre_categoria)

    if not os.path.exists(ruta_categoria):
        os.makedirs(ruta_categoria)
        print("Categoría creada correctamente.")
    else:
        print("La categoría ya existe.")

# Opción 4: Eliminar una receta
def opcion_eliminar_receta():
    categorias = mostrar_categorias()
    if categorias:
        eleccion_categoria = int(input("Elige una categoría por su número: ")) - 1
        categoria_elegida = categorias[eleccion_categoria]
        ruta_categoria = os.path.join(ruta_recetas, categoria_elegida)
        recetas = [rec for rec in os.listdir(ruta_categoria) if os.path.isfile(os.path.join(ruta_categoria, rec))]

        if recetas:
            print("Recetas disponibles:")
            for i in range(len(recetas)):
                print(f"{i + 1}. {recetas[i]}")
            eleccion_receta = int(input("Elige una receta por su número para eliminar: ")) - 1
            receta_elegida = recetas[eleccion_receta]
            os.remove(os.path.join(ruta_categoria, receta_elegida))
            print("Receta eliminada correctamente.")
        else:
            print("No hay recetas en esta categoría.")

# Opción 5: Eliminar una categoría
def opcion_eliminar_categoria():
    categorias = mostrar_categorias()
    if categorias:
        eleccion_categoria = int(input("Elige una categoría por su número para eliminar: ")) - 1
        categoria_elegida = categorias[eleccion_categoria]
        ruta_categoria = os.path.join(ruta_recetas, categoria_elegida)

        if os.path.exists(ruta_categoria):
            for archivo in os.listdir(ruta_categoria):
                os.remove(os.path.join(ruta_categoria, archivo))
            os.rmdir(ruta_categoria)
            print("Categoría eliminada correctamente.")
        else:
            print("La categoría no existe.")

# Bucle principal
while True:
    limpiar_pantalla()
    print("¡Bienvenido a nuestro gestor de recetas!")
    print("\nPor favor, elija una de las siguientes opciones:")
    print("1. Leer una receta")
    print("2. Crear una receta")
    print("3. Crear una categoría")
    print("4. Eliminar una receta")
    print("5. Eliminar una categoría")
    print("6. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == "1":
        opcion_leer_receta()
    elif opcion == "2":
        opcion_crear_receta()
    elif opcion == "3":
        opcion_crear_categoria()
    elif opcion == "4":
        opcion_eliminar_receta()
    elif opcion == "5":
        opcion_eliminar_categoria()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        # Pausa para que el usuario pueda ver el resultado antes de limpiar la pantalla
    input("\nPresiona cualquier tecla para volver al menú...")
