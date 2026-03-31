from src.data.database_mgr import get_connection

def registrar_alquiler(cliente_id, libro_id, fecha_devolucion_prevista):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO alquiler (cliente_id, fecha_devolucion_prevista)
        VALUES (?, ?)
    """, (cliente_id, fecha_devolucion_prevista))

    alquiler_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO detalle_alquiler (alquiler_id, libro_id, cantidad)
        VALUES (?, ?, 1)
    """, (alquiler_id, libro_id))

    cursor.execute("""
        UPDATE libro SET cantidad_disponible = cantidad_disponible - 1
        WHERE id = ? AND cantidad_disponible > 0
    """, (libro_id,))

    conexion.commit()
    conexion.close()

def listar_alquileres():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT a.id, c.nombre, l.titulo, a.fecha_prestamo, a.fecha_devolucion_prevista, a.estado
        FROM alquiler a
        JOIN cliente c ON a.cliente_id = c.id
        JOIN detalle_alquiler da ON da.alquiler_id = a.id
        JOIN libro l ON da.libro_id = l.id
    """)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados