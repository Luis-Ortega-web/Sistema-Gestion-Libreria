from src.data.database_mgr import get_connection

def crear_venta(cliente_id, libro_id, cantidad):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT precio, cantidad_disponible FROM libro WHERE id = ?", (libro_id,))
    libro = cursor.fetchone()

    if not libro:
        raise ValueError("Libro no encontrado")

    if libro["cantidad_disponible"] < cantidad:
        raise ValueError("Stock insuficiente")

    precio = libro["precio"]
    total = precio * cantidad

    cursor.execute(
        "INSERT INTO venta (cliente_id, total) VALUES (?, ?)",
        (cliente_id, total)
    )

    venta_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO detalle_venta (venta_id, libro_id, cantidad, precio_unitario, subtotal)
        VALUES (?, ?, ?, ?, ?)
    """, (venta_id, libro_id, cantidad, precio, total))

    cursor.execute("""
        UPDATE libro 
        SET cantidad_disponible = cantidad_disponible - ?
        WHERE id = ?
    """, (cantidad, libro_id))

    conn.commit()
    conn.close()


def obtener_ventas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT v.id, c.nombre, v.fecha, v.total
        FROM venta v
        JOIN cliente c ON v.cliente_id = c.id
    """)

    data = cursor.fetchall()
    conn.close()
    return data