import customtkinter as ctk
from src.logic.alquiler_service import crear_alquiler, obtener_alquileres, obtener_clientes, obtener_libros, devolver_libro

class AlquilerUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestión de Alquileres")
        self.geometry("800x700")

        self.clientes = []
        self.libros = []

        ctk.CTkLabel(self, text="Alquileres", font=("Arial", 22)).pack(pady=10)

        # CLIENTE
        ctk.CTkLabel(self, text="Seleccionar cliente:").pack()
        self.combo_cliente = ctk.CTkComboBox(self, values=[], width=400)
        self.combo_cliente.pack(pady=5)

        # LIBRO
        ctk.CTkLabel(self, text="Seleccionar libro:").pack()
        self.combo_libro = ctk.CTkComboBox(self, values=[], width=400)
        self.combo_libro.pack(pady=5)

        # FECHA DEVOLUCION
        self.fecha = ctk.CTkEntry(self, placeholder_text="Fecha devolución (ej: 2025-12-31)")
        self.fecha.pack(pady=5)

        ctk.CTkButton(self, text="Cargar listas", command=self.cargar_listas).pack(pady=5)
        ctk.CTkButton(self, text="Registrar alquiler", command=self.registrar_alquiler).pack(pady=10)
        ctk.CTkButton(self, text="Ver activos", command=self.ver_activos).pack(pady=5)
        ctk.CTkButton(self, text="Ver devueltos", command=self.ver_devueltos).pack(pady=5)
        
        self.lista = ctk.CTkTextbox(self, width=600, height=130)
        self.lista.pack(pady=10)

        self.devolucion_id = ctk.CTkEntry(self, placeholder_text="ID del alquiler a devolver")
        self.devolucion_id.pack(pady=5)

        ctk.CTkButton(self, text="Registrar devolución", command=self.registrar_devolucion).pack(pady=5)

        ctk.CTkButton(self, text="Volver al menú", command=self.volver).pack(pady=5)
         

    def cargar_listas(self):
        self.clientes = obtener_clientes()
        self.libros = obtener_libros()

        nombres_clientes = [f"{c['id']} - {c['nombre']}" for c in self.clientes]
        nombres_libros = [f"{l['id']} - {l['titulo']} (Stock: {l['cantidad_disponible']})" for l in self.libros]

        self.combo_cliente.configure(values=nombres_clientes)
        self.combo_libro.configure(values=nombres_libros)

        if nombres_clientes:
            self.combo_cliente.set(nombres_clientes[0])
        if nombres_libros:
            self.combo_libro.set(nombres_libros[0])

        self.lista.delete("0.0", "end")
        self.lista.insert("end", "Listas cargadas correctamente\n")


    def registrar_alquiler(self):
        if self.combo_cliente.get() == "" or self.combo_libro.get() == "":
            self.lista.delete("0.0", "end")
            self.lista.insert("end", "Debe cargar las listas primero\n")
            return

        if self.fecha.get() == "":
            self.lista.delete("0.0", "end")
            self.lista.insert("end", "Debe ingresar la fecha de devolución\n")
            return

        cliente_id = int(self.combo_cliente.get().split(" - ")[0])
        libro_id = int(self.combo_libro.get().split(" - ")[0])

        crear_alquiler(cliente_id, libro_id, self.fecha.get())

        self.lista.delete("0.0", "end")
        self.lista.insert("end", "Alquiler registrado correctamente\n")

        self.fecha.delete(0, "end")


    def ver_activos(self):
        alquileres = obtener_alquileres()

        self.lista.delete("0.0", "end")
        self.lista.insert("end", "--- ALQUILERES ACTIVOS ---\n")

        encontrados = False
        for a in alquileres:
            if a['estado'] == 'activo':
                texto = f"#{a['id']} - {a['nombre']} - {a['titulo']} - Prestado: {a['fecha_prestamo']} - Devolver: {a['fecha_devolucion_prevista']}\n"
                self.lista.insert("end", texto)
                encontrados = True

        if not encontrados:
            self.lista.insert("end", "No hay alquileres activos\n")


    def ver_devueltos(self):
        alquileres = obtener_alquileres()

        self.lista.delete("0.0", "end")
        self.lista.insert("end", "--- ALQUILERES DEVUELTOS ---\n")

        encontrados = False
        for a in alquileres:
            if a['estado'] == 'devuelto':
                texto = f"#{a['id']} - {a['nombre']} - {a['titulo']} - Prestado: {a['fecha_prestamo']} - Devuelto: {a['fecha_devolucion_real']}\n"
                self.lista.insert("end", texto)
                encontrados = True

        if not encontrados:
            self.lista.insert("end", "No hay alquileres devueltos\n")


    def registrar_devolucion(self):
        alquiler_id = self.devolucion_id.get()

        if alquiler_id == "":
            self.lista.delete("0.0", "end")
            self.lista.insert("end", "Debe ingresar el ID del alquiler\n")
            return

        devolver_libro(int(alquiler_id))

        self.lista.delete("0.0", "end")
        self.lista.insert("end", f"Devolución del alquiler #{alquiler_id} registrada correctamente\n")

        self.devolucion_id.delete(0, "end")


    def volver(self):
        self.destroy()
        from src.presentation.menu_ui import menu_principal
        menu_principal()


def menu_alquileres():
    app = AlquilerUI()
    app.mainloop()