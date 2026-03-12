import unittest
import sqlite3
from src.data.database_mgr import get_connection, registrar_libro_db, validar_login

class TestSistemaLibreria(unittest.TestCase):
    
    def setUp(self):
        """Prepara la DB en memoria y mantiene la conexión abierta para el test."""
        self.db_test = ":memory:"
        self.conn = get_connection(self.db_test)
        c = self.conn.cursor()
        
        c.execute("""CREATE TABLE libro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT, autor TEXT, isbn TEXT UNIQUE, 
            cantidad_disponible INTEGER, precio REAL)""")
            
        c.execute("""CREATE TABLE usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT UNIQUE, password TEXT)""")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_01_registro_exitoso(self):
        # Pasamos la conexión activa para que vea las tablas
        registrar_libro_db("Halo: Cryptum", "Greg Bear", "111-AAA", 5, 120.0, connection=self.conn)
        res = self.conn.execute("SELECT * FROM libro WHERE isbn='111-AAA'").fetchone()
        self.assertIsNotNone(res)
        self.assertEqual(res["titulo"], "Halo: Cryptum")

    def test_02_campos_vacios(self):
        with self.assertRaises(ValueError):
            registrar_libro_db("", "Autor", "", "5", "100.0", connection=self.conn)

    def test_03_isbn_duplicado(self):
        registrar_libro_db("Libro 1", "Autor", "ISBN-99", 1, 50.0, connection=self.conn)
        with self.assertRaises(sqlite3.IntegrityError):
            registrar_libro_db("Libro 2", "Otro", "ISBN-99", 2, 60.0, connection=self.conn)

    def test_04_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            registrar_libro_db("Star Wars", "T. Zahn", "999", "muchos", 200.0, connection=self.conn)

    def test_05_login_usuario(self):
        self.conn.execute("INSERT INTO usuario (username, password) VALUES (?, ?)", ("admin", "itla123"))
        self.conn.commit()
        # Validamos usando la conexión abierta
        self.assertTrue(validar_login("admin", "itla123", connection=self.conn))

if __name__ == "__main__":
    unittest.main()