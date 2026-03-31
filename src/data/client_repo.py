from src.data.database_mgr import get_connection

def agregar_cliente(nombre, telefono, email, direccion):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO cliente (nombre, telefono, email, direccion)
        VALUES (?, ?, ?, ?)
    """, (nombre, telefono, email, direccion))
    conexion.commit()
    conexion.close()

def listar_clientes():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados