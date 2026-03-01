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
