from src.data.database_mgr import create_tables
from src.presentation.login_ui import login

if __name__ == "__main__":
    create_tables()

    if login():
        print("Bienvenido al sistema")
    else:
        print("Acceso denegado")
