from src.data.database_mgr import create_tables, get_connection
from src.presentation.login_ui import login
from src.presentation.inventory_ui import menu_inventario


def crear_usuario_prueba():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuario WHERE username = ?", ("admin",))
    usuario = cursor.fetchone()

    if not usuario:
        cursor.execute("""
            INSERT INTO usuario (username, password, nombre, rol)
            VALUES (?, ?, ?, ?)
        """, ("admin", "1234", "Administrador", "admin"))
        conn.commit()

    conn.close()


if __name__ == "__main__":

    create_tables()
    crear_usuario_prueba()

    if login():
        menu_inventario()