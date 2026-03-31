import customtkinter as ctk
from src.logic.client_service import registrar_cliente, obtener_clientes

class ClienteUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestión de Clientes")
        self.geometry("800x600")

        titulo = ctk.CTkLabel(self, text="Clientes", font=("Arial", 22))
        titulo.pack(pady=10)

        self.nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.nombre.pack(pady=5)

        self.telefono = ctk.CTkEntry(self, placeholder_text="Teléfono")
        self.telefono.pack(pady=5)

        self.email = ctk.CTkEntry(self, placeholder_text="Email")
        self.email.pack(pady=5)

        self.direccion = ctk.CTkEntry(self, placeholder_text="Dirección")
        self.direccion.pack(pady=5)

        registrar_btn = ctk.CTkButton(self, text="Registrar cliente", command=self.registrar_cliente)
        registrar_btn.pack(pady=10)

        ver_btn = ctk.CTkButton(self, text="Ver clientes", command=self.ver_clientes)
        ver_btn.pack(pady=5)

        self.lista = ctk.CTkTextbox(self, width=500, height=200)
        self.lista.pack(pady=10)
        
        volver_btn = ctk.CTkButton(self, text="Volver al menú", command=self.volver)
        volver_btn.pack(pady=10)
        

    def registrar_cliente(self):
        if self.nombre.get() == "":
            self.lista.insert("end", "El nombre es obligatorio\n")
            return

        registrar_cliente(
            self.nombre.get(),
            self.telefono.get(),
            self.email.get(),
            self.direccion.get(),
        )

        self.lista.insert("end", "Cliente registrado correctamente\n")

        self.nombre.delete(0, "end")
        self.telefono.delete(0, "end")
        self.email.delete(0, "end")
        self.direccion.delete(0, "end")

    def ver_clientes(self):
        clientes = obtener_clientes()
        self.lista.delete("0.0", "end")
        for cliente in clientes:
            texto = f"{cliente['id']} - {cliente['nombre']} - {cliente['telefono']} - {cliente['email']}\n"
            self.lista.insert("end", texto)

    def volver(self):
        self.destroy()
        from src.presentation.menu_ui import menu_principal
        menu_principal()


def menu_clientes():
    app = ClienteUI()
    app.mainloop()