from src.data.database_mgr import get_connection

def agregar_libro(titulo, autor, categoria, isbn, cantidad, precio):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO libro (titulo, autor, categoria, isbn, cantidad_disponible, precio)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, autor, categoria, isbn, cantidad, precio))

    conexion.commit()
    conexion.close()


def listar_libros():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libro")
    resultados = cursor.fetchall()

    conexion.close()
    return resultados
def eliminar_libro(id_libro):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM libro WHERE id = ?",
        (id_libro,)
    )

    conexion.commit()
    conexion.close()


def actualizar_libro(id_libro, titulo, autor, categoria, isbn, cantidad, precio):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE libro
        SET titulo = ?, autor = ?, categoria = ?, isbn = ?, cantidad_disponible = ?, precio = ?
        WHERE id = ?
    """, (titulo, autor, categoria, isbn, cantidad, precio, id_libro))
    conexion.commit()
    conexion.close()