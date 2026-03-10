import customtkinter as ctk
ctk.set_appearance_mode("light")
from src.data.database_mgr import get_connection


class LoginUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Librería - Login")
        self.geometry("450x300")

        # Título
        titulo = ctk.CTkLabel(self, text="Librería - Login", font=("Arial", 20))
        titulo.pack(pady=20)

        # Usuario
        label_user = ctk.CTkLabel(self, text="Usuario")
        label_user.pack(anchor="w", padx=70)

        self.entry_user = ctk.CTkEntry(self, width=300)
        self.entry_user.pack(pady=5)

        # Contraseña
        label_pass = ctk.CTkLabel(self, text="Contraseña")
        label_pass.pack(anchor="w", padx=70)

        self.entry_pass = ctk.CTkEntry(self, width=300, show="*")
        self.entry_pass.pack(pady=5)

        # Botones
        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(pady=20)

        cancelar = ctk.CTkButton(
            frame_botones,
            text="Cancelar",
            command=self.destroy
        )
        cancelar.grid(row=0, column=0, padx=10)

        login_btn = ctk.CTkButton(
            frame_botones,
            text="Iniciar sesión",
            command=self.login
        )
        login_btn.grid(row=0, column=1, padx=10)

        self.mensaje = ctk.CTkLabel(self, text="")
        self.mensaje.pack()

        self.login_exitoso = False

    def login(self):

        username = self.entry_user.get()
        password = self.entry_pass.get()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuario WHERE username = ? AND password = ?",
            (username, password)
        )

        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            self.login_exitoso = True
            self.destroy()
        else:
            self.mensaje.configure(text="Usuario o contraseña incorrectos")


def login():

    app = LoginUI()
    app.mainloop()

    return app.login_exitoso