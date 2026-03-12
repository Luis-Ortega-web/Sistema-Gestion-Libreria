# data/database_mgr.py

import sqlite3
from sqlite3 import Connection

DB_FILE = "libreria.db"

def get_connection(db_name=DB_FILE) -> Connection:
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS libro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        categoria TEXT,
        isbn TEXT,
        cantidad_disponible INTEGER NOT NULL DEFAULT 0,
        precio REAL DEFAULT 0.0
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT,
        email TEXT,
        direccion TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS venta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        fecha TEXT DEFAULT (datetime('now','localtime')),
        total REAL DEFAULT 0.0,
        FOREIGN KEY(cliente_id) REFERENCES cliente(id)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS detalle_venta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        venta_id INTEGER,
        libro_id INTEGER,
        cantidad INTEGER,
        precio_unitario REAL,
        subtotal REAL,
        FOREIGN KEY(venta_id) REFERENCES venta(id),
        FOREIGN KEY(libro_id) REFERENCES libro(id)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS alquiler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        fecha_prestamo TEXT DEFAULT (datetime('now','localtime')),
        fecha_devolucion_prevista TEXT,
        fecha_devolucion_real TEXT,
        estado TEXT DEFAULT 'activo',
        FOREIGN KEY(cliente_id) REFERENCES cliente(id)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS detalle_alquiler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alquiler_id INTEGER,
        libro_id INTEGER,
        cantidad INTEGER,
        FOREIGN KEY(alquiler_id) REFERENCES alquiler(id),
        FOREIGN KEY(libro_id) REFERENCES libro(id)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        nombre TEXT,
        rol TEXT
    )
    """)

    conn.commit()

    conn.close()

def registrar_libro_db(titulo, autor, isbn, cantidad, precio, db_name=DB_FILE, connection=None):
    if not titulo.strip() or not isbn.strip():
        raise ValueError("Campos obligatorios vacíos")
    
    # Si recibimos una conexión (para tests), la usamos. Si no, abrimos una nueva.
    conn = connection if connection else get_connection(db_name)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO libro (titulo, autor, isbn, cantidad_disponible, precio)
        VALUES (?, ?, ?, ?, ?)
    """, (titulo, autor, isbn, int(cantidad), float(precio)))
    
    if not connection: # Solo cerramos si nosotros abrimos la conexión
        conn.commit()
        conn.close()

def validar_login(username, password, db_name=DB_FILE, connection=None):
    conn = connection if connection else get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if not connection:
        conn.close()
    return user is not None