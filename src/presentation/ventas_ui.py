import customtkinter as ctk
from src.logic.venta_service import crear_venta, obtener_ventas
from src.logic.alquiler_service import obtener_clientes, obtener_libros
from src.logic.reporte_service import total_ventas


class VentaUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestión de Ventas")
        self.geometry("800x650")

        self.clientes = []
        self.libros = []

        ctk.CTkLabel(self, text="Ventas", font=("Arial", 22)).pack(pady=10)

        # CLIENTE
        ctk.CTkLabel(self, text="Seleccionar cliente:").pack()
        self.combo_cliente = ctk.CTkComboBox(self, values=[], width=400)
        self.combo_cliente.pack(pady=5)

        # LIBRO
        ctk.CTkLabel(self, text="Seleccionar libro:").pack()
        self.combo_libro = ctk.CTkComboBox(self, values=[], width=400)
        self.combo_libro.pack(pady=5)

        # CANTIDAD
        self.cantidad = ctk.CTkEntry(self, placeholder_text="Cantidad")
        self.cantidad.pack(pady=5)

        # BOTONES
        ctk.CTkButton(self, text="Cargar listas", command=self.cargar_listas).pack(pady=5)
        ctk.CTkButton(self, text="Registrar venta", command=self.registrar_venta).pack(pady=10)
        ctk.CTkButton(self, text="Ver ventas", command=self.ver_ventas).pack(pady=5)
        ctk.CTkButton(self, text="Ver total vendido", command=self.mostrar_total).pack(pady=5)

        # ÁREA DE RESULTADOS
        self.lista = ctk.CTkTextbox(self, width=600, height=200)
        self.lista.pack(pady=10)

        # BOTÓN VOLVER
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


    def registrar_venta(self):
        if self.cantidad.get() == "":
            self.lista.delete("0.0", "end")
            self.lista.insert("end", "Debe ingresar la cantidad\n")
            return

        try:
            cliente_id = int(self.combo_cliente.get().split(" - ")[0])
            libro_id = int(self.combo_libro.get().split(" - ")[0])
            cantidad = int(self.cantidad.get())

            crear_venta(cliente_id, libro_id, cantidad)

            self.lista.delete("0.0", "end")
            self.lista.insert("end", "Venta registrada correctamente\n")

        except Exception as e:
            self.lista.delete("0.0", "end")
            self.lista.insert("end", f"Error: {str(e)}\n")

        self.cantidad.delete(0, "end")


    def ver_ventas(self):
        ventas = obtener_ventas()

        self.lista.delete("0.0", "end")
        self.lista.insert("end", "--- VENTAS ---\n")

        if not ventas:
            self.lista.insert("end", "No hay ventas registradas\n")
            return

        for v in ventas:
            texto = f"#{v['id']} - {v['nombre']} - {v['fecha']} - Total: {v['total']}\n"
            self.lista.insert("end", texto)


    def mostrar_total(self):
        total = total_ventas()

        self.lista.delete("0.0", "end")
        self.lista.insert("end", f"Total vendido: {total}\n")


    def volver(self):
        self.destroy()
        from src.presentation.menu_ui import menu_principal
        menu_principal()


def menu_ventas():
    app = VentaUI()
    app.mainloop()