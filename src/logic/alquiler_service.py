from src.data.alquiler_repo import registrar_alquiler, listar_alquileres
from src.data.client_repo import listar_clientes
from src.data.book_repo import listar_libros

def crear_alquiler(cliente_id, libro_id, fecha_devolucion_prevista):
    registrar_alquiler(cliente_id, libro_id, fecha_devolucion_prevista)

def obtener_alquileres():
    return listar_alquileres()

def obtener_clientes():
    return listar_clientes()

def obtener_libros():
    return listar_libros()