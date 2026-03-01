
from src.data.database_mgr import get_connection

def login():
    print("=== LOGIN ===")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuario WHERE username = ? AND password = ?",
        (username, password)
    )

    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        print("Login exitoso")
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False
