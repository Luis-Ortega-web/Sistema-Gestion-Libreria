from src.data.book_repo import agregar_libro, listar_libros

def registrar_libro(titulo, autor, categoria, isbn, cantidad, precio):
    agregar_libro(titulo, autor, categoria, isbn, cantidad, precio)

def obtener_libros():
    return listar_libros()
