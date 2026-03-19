import customtkinter as ctk

ctk.set_appearance_mode("light")
from src.logic.book_service import registrar_libro, obtener_libros
from src.data.book_repo import eliminar_libro

class InventarioUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Inventario de libros")
        self.geometry("800x800")

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

        registrar = ctk.CTkButton(
            self, text="Registrar libro", command=self.registrar_libro
        )
        registrar.pack(pady=10)

        ver = ctk.CTkButton(self, text="Ver libros", command=self.ver_libros)
        ver.pack(pady=5)

        self.buscar = ctk.CTkEntry(self, placeholder_text="Buscar libro")
        self.buscar.pack(pady=5)

        buscar_btn = ctk.CTkButton(self, text="Buscar", command=self.buscar_libro)
        buscar_btn.pack(pady=5)

        self.lista = ctk.CTkTextbox(self, width=500, height=200)
        self.lista.pack(pady=10)
        
        # ELIMINAR LIBRO
        self.eliminar_id = ctk.CTkEntry(self, placeholder_text="ID del libro a eliminar")
        self.eliminar_id.pack(pady=5)

        eliminar_btn = ctk.CTkButton(self, text="Eliminar libro", command=self.eliminar_libro)
        eliminar_btn.pack(pady=5)

    def registrar_libro(self):

        if (
            self.titulo.get() == ""
            or self.autor.get() == ""
            or self.categoria.get() == ""
            or self.isbn.get() == ""
            or self.cantidad.get() == ""
            or self.precio.get() == ""
        ):
            self.lista.insert("end", "Debe completar todos los campos\n")
            return

        registrar_libro(
            self.titulo.get(),
            self.autor.get(),
            self.categoria.get(),
            self.isbn.get(),
            int(self.cantidad.get()),
            float(self.precio.get()),
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

    def buscar_libro(self):

        libros = obtener_libros()
        texto_busqueda = self.buscar.get().lower()

        self.lista.delete("0.0", "end")

        for libro in libros:
            if texto_busqueda in libro['titulo'].lower():
                texto = f"{libro['id']} - {libro['titulo']} - {libro['autor']} - Stock: {libro['cantidad_disponible']} - Precio: {libro['precio']}\n"
                self.lista.insert("end", texto)

    def eliminar_libro(self):

        id_libro = self.eliminar_id.get()

        if id_libro == "":
            self.lista.insert("end", "Debe ingresar el ID del libro\n")
            return

        eliminar_libro(int(id_libro))

        self.lista.insert("end", "Libro eliminado correctamente\n")

        self.eliminar_id.delete(0, "end")


def menu_inventario():

    app = InventarioUI()
    app.mainloop()
