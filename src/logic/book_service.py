from src.data.book_repo import agregar_libro, listar_libros, actualizar_libro as repo_actualizar

def registrar_libro(titulo, autor, categoria, isbn, cantidad, precio):
    agregar_libro(titulo, autor, categoria, isbn, cantidad, precio)

def obtener_libros():
    return listar_libros()

def actualizar_libro(id_libro, titulo, autor, categoria, isbn, cantidad, precio):
    repo_actualizar(id_libro, titulo, autor, categoria, isbn, cantidad, precio)