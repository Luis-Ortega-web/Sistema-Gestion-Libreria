from src.logic.book_service import registrar_libro, obtener_libros

def menu_inventario():
    while True:
        print("\n=== INVENTARIO ===")
        print("1. Registrar libro")
        print("2. Ver libros")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio: "))

            registrar_libro(titulo, autor, categoria, isbn, cantidad, precio)
            print("Libro registrado correctamente")

        elif opcion == "2":
            libros = obtener_libros()
            print("\n--- LISTA DE LIBROS ---")
            for libro in libros:
                print(f"{libro['id']} - {libro['titulo']} - {libro['autor']} - Stock: {libro['cantidad_disponible']} - Precio: {libro['precio']}")

        elif opcion == "3":
            break

        else:
            print("Opción inválida")
