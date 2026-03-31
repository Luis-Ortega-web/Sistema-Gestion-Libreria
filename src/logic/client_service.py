from src.data.client_repo import agregar_cliente, listar_clientes

def registrar_cliente(nombre, telefono, email, direccion):
    agregar_cliente(nombre, telefono, email, direccion)

def obtener_clientes():
    return listar_clientes()