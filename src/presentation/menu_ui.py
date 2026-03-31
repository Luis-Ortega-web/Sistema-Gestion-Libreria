import customtkinter as ctk
from src.presentation.inventory_ui import menu_inventario

def abrir_clientes():
    from src.presentation.client_ui import menu_clientes
    menu_clientes()

def menu_principal():
    ventana = ctk.CTk()
    ventana.title("Sistema de Librería")
    ventana.geometry("400x300")

    ctk.CTkLabel(ventana, text="Menú Principal", font=("Arial", 22)).pack(pady=20)

    ctk.CTkButton(
        ventana,
        text="Inventario de Libros",
        command=lambda: [ventana.destroy(), menu_inventario()]
    ).pack(pady=10)

    ctk.CTkButton(
        ventana,
        text="Clientes",
        command=lambda: [ventana.destroy(), abrir_clientes()]
    ).pack(pady=10)

    ventana.mainloop()