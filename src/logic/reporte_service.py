from src.data.database_mgr import get_connection

def total_ventas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total) as total FROM venta")
    resultado = cursor.fetchone()

    conn.close()
    return resultado["total"] if resultado["total"] else 0