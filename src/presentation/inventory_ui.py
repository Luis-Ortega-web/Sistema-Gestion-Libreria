import customtkinter as ctk

ctk.set_appearance_mode("light")
from src.logic.book_service import registrar_libro, obtener_libros, actualizar_libro
from src.data.book_repo import eliminar_libro

class InventarioUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Inventario de libros")
        self.geometry("700x600")

        ctk.CTkLabel(self, text="Inventario", font=("Arial", 24)).pack(pady=10)

        self.tabs = ctk.CTkTabview(self, width=650, height=480)
        self.tabs.pack(pady=5, padx=20)

        self.tabs.add("Registrar")
        self.tabs.add("Ver / Buscar")
        self.tabs.add("Eliminar")
        self.tabs.add("Actualizar")

        self._tab_registrar()
        self._tab_ver()
        self._tab_eliminar()
        self._tab_actualizar()

        ctk.CTkButton(self, text="Volver al menú", command=self.volver).pack(pady=10)

    def _tab_registrar(self):
        tab = self.tabs.tab("Registrar")

        self.titulo = ctk.CTkEntry(tab, placeholder_text="Título", width=300)
        self.titulo.pack(pady=5)

        self.autor = ctk.CTkEntry(tab, placeholder_text="Autor", width=300)
        self.autor.pack(pady=5)

        self.categoria = ctk.CTkEntry(tab, placeholder_text="Categoría", width=300)
        self.categoria.pack(pady=5)

        self.isbn = ctk.CTkEntry(tab, placeholder_text="ISBN", width=300)
        self.isbn.pack(pady=5)

        self.cantidad = ctk.CTkEntry(tab, placeholder_text="Cantidad", width=300)
        self.cantidad.pack(pady=5)

        self.precio = ctk.CTkEntry(tab, placeholder_text="Precio", width=300)
        self.precio.pack(pady=5)

        self.msg_registrar = ctk.CTkLabel(tab, text="")
        self.msg_registrar.pack(pady=5)

        ctk.CTkButton(tab, text="Registrar libro", command=self.registrar_libro).pack(pady=10)

    def _tab_ver(self):
        tab = self.tabs.tab("Ver / Buscar")

        self.buscar = ctk.CTkEntry(tab, placeholder_text="Buscar por título", width=300)
        self.buscar.pack(pady=5)

        ctk.CTkButton(tab, text="Buscar", command=self.buscar_libro).pack(pady=5)
        ctk.CTkButton(tab, text="Ver todos", command=self.ver_libros).pack(pady=5)

        self.lista = ctk.CTkTextbox(tab, width=580, height=280)
        self.lista.pack(pady=10)

    def _tab_eliminar(self):
        tab = self.tabs.tab("Eliminar")

        ctk.CTkLabel(tab, text="Primero ve la lista para ver los IDs", font=("Arial", 13)).pack(pady=10)

        self.eliminar_id = ctk.CTkEntry(tab, placeholder_text="ID del libro a eliminar", width=300)
        self.eliminar_id.pack(pady=5)

        self.msg_eliminar = ctk.CTkLabel(tab, text="")
        self.msg_eliminar.pack(pady=5)

        ctk.CTkButton(tab, text="Eliminar libro", fg_color="red", hover_color="darkred", command=self.eliminar_libro).pack(pady=10)

    def _tab_actualizar(self):
        tab = self.tabs.tab("Actualizar")

        self.actualizar_id = ctk.CTkEntry(tab, placeholder_text="ID del libro a actualizar", width=300)
        self.actualizar_id.pack(pady=5)

        ctk.CTkButton(tab, text="Cargar datos", command=self.cargar_libro).pack(pady=5)

        self.msg_actualizar = ctk.CTkLabel(tab, text="")
        self.msg_actualizar.pack(pady=5)

        ctk.CTkButton(tab, text="Guardar cambios", command=self.guardar_actualizacion).pack(pady=5)

    def registrar_libro(self):
        if not all([self.titulo.get(), self.autor.get(), self.categoria.get(),
                    self.isbn.get(), self.cantidad.get(), self.precio.get()]):
            self.msg_registrar.configure(text="Debe completar todos los campos", text_color="red")
            return

        registrar_libro(self.titulo.get(), self.autor.get(), self.categoria.get(),
                        self.isbn.get(), int(self.cantidad.get()), float(self.precio.get()))

        self.msg_registrar.configure(text="Libro registrado correctamente", text_color="green")
        for campo in [self.titulo, self.autor, self.categoria, self.isbn, self.cantidad, self.precio]:
            campo.delete(0, "end")

    def ver_libros(self):
        libros = obtener_libros()
        self.lista.delete("0.0", "end")
        for libro in libros:
            self.lista.insert("end", f"{libro['id']} - {libro['titulo']} - {libro['autor']} - Stock: {libro['cantidad_disponible']} - Precio: {libro['precio']}\n")

    def buscar_libro(self):
        libros = obtener_libros()
        texto = self.buscar.get().lower()
        self.lista.delete("0.0", "end")
        for libro in libros:
            if texto in libro['titulo'].lower():
                self.lista.insert("end", f"{libro['id']} - {libro['titulo']} - {libro['autor']} - Stock: {libro['cantidad_disponible']} - Precio: {libro['precio']}\n")

    def eliminar_libro(self):
        id_libro = self.eliminar_id.get()
        if id_libro == "":
            self.msg_eliminar.configure(text="Debe ingresar el ID del libro", text_color="red")
            return
        eliminar_libro(int(id_libro))
        self.msg_eliminar.configure(text="Libro eliminado correctamente", text_color="green")
        self.eliminar_id.delete(0, "end")

    def cargar_libro(self):
        id_libro = self.actualizar_id.get()
        if id_libro == "":
            self.msg_actualizar.configure(text="Debe ingresar el ID", text_color="red")
            return

        libros = obtener_libros()
        libro = next((l for l in libros if l["id"] == int(id_libro)), None)

        if not libro:
            self.msg_actualizar.configure(text="No se encontró el libro", text_color="red")
            return

        self.titulo.delete(0, "end")
        self.titulo.insert(0, libro["titulo"])
        self.autor.delete(0, "end")
        self.autor.insert(0, libro["autor"])
        self.categoria.delete(0, "end")
        self.categoria.insert(0, libro["categoria"] or "")
        self.isbn.delete(0, "end")
        self.isbn.insert(0, libro["isbn"] or "")
        self.cantidad.delete(0, "end")
        self.cantidad.insert(0, str(libro["cantidad_disponible"]))
        self.precio.delete(0, "end")
        self.precio.insert(0, str(libro["precio"]))

        self.tabs.set("Registrar")
        self.msg_actualizar.configure(text="Datos cargados, edítalos en la pestaña Registrar", text_color="blue")

    def guardar_actualizacion(self):
        id_libro = self.actualizar_id.get()
        if id_libro == "" or self.titulo.get() == "":
            self.msg_actualizar.configure(text="Carga un libro primero", text_color="red")
            return

        actualizar_libro(int(id_libro), self.titulo.get(), self.autor.get(),
                         self.categoria.get(), self.isbn.get(),
                         int(self.cantidad.get()), float(self.precio.get()))

        self.msg_actualizar.configure(text=f"Libro #{id_libro} actualizado", text_color="green")
        self.actualizar_id.delete(0, "end")

    def volver(self):
        self.destroy()
        from src.presentation.menu_ui import menu_principal
        menu_principal()


def menu_inventario():
    app = InventarioUI()
    app.mainloop()