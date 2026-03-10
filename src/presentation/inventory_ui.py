import customtkinter as ctk
ctk.set_appearance_mode("light")
from src.logic.book_service import registrar_libro, obtener_libros


class InventarioUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Inventario de libros")
        self.geometry("600x500")

        titulo = ctk.CTkLabel(self, text="Inventario", font=("Arial", 22))
        titulo.pack(pady=10)

        # FORMULARIO
        self.titulo = ctk.CTkEntry(self, placeholder_text="Título")
        self.titulo.pack(pady=5)

        self.autor = ctk.CTkEntry(self, placeholder_text="Autor")
        self.autor.pack(pady=5)

        self.categoria = ctk.CTkEntry(self, placeholder_text="Categoría")
        self.categoria.pack(pady=5)

        self.isbn = ctk.CTkEntry(self, placeholder_text="ISBN")
        self.isbn.pack(pady=5)

        self.cantidad = ctk.CTkEntry(self, placeholder_text="Cantidad")
        self.cantidad.pack(pady=5)

        self.precio = ctk.CTkEntry(self, placeholder_text="Precio")
        self.precio.pack(pady=5)

        registrar = ctk.CTkButton(self, text="Registrar libro", command=self.registrar_libro)
        registrar.pack(pady=10)

        ver = ctk.CTkButton(self, text="Ver libros", command=self.ver_libros)
        ver.pack(pady=5)

        self.lista = ctk.CTkTextbox(self, width=500, height=200)
        self.lista.pack(pady=10)

    def registrar_libro(self):

     registrar_libro(
        self.titulo.get(),
        self.autor.get(),
        self.categoria.get(),
        self.isbn.get(),
        int(self.cantidad.get()),
        float(self.precio.get())
    )

     self.lista.insert("end", "Libro registrado correctamente\n")

     self.titulo.delete(0, "end")
     self.autor.delete(0, "end")
     self.categoria.delete(0, "end")
     self.isbn.delete(0, "end")
     self.cantidad.delete(0, "end")
     self.precio.delete(0, "end")

    def ver_libros(self):

        libros = obtener_libros()

        self.lista.delete("0.0", "end")

        for libro in libros:
            texto = f"{libro['id']} - {libro['titulo']} - {libro['autor']} - Stock: {libro['cantidad_disponible']} - Precio: {libro['precio']}\n"
            self.lista.insert("end", texto)


def menu_inventario():

    app = InventarioUI()
    app.mainloop()