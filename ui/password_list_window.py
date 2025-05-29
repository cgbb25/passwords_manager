import tkinter as tk
from tkinter import ttk
from database import get_passwords  # Se asume devuelve lista (id, service, username, password, notes)

class PasswordListWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Lista de Contraseñas")
        self.window.geometry("700x400")

        frame = tk.Frame(self.window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear Treeview con columnas
        columns = ("service", "username", "password", "notes")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=True)

        # Definir encabezados y anchura
        self.tree.heading("service", text="Servicio")
        self.tree.heading("username", text="Usuario")
        self.tree.heading("password", text="Contraseña")
        self.tree.heading("notes", text="Notas")

        self.tree.column("service", width=150)
        self.tree.column("username", width=150)
        self.tree.column("password", width=150)
        self.tree.column("notes", width=200)

        # Cargar datos en el Treeview
        self.load_data()

        # Botón para cerrar ventana
        close_btn = tk.Button(frame, text="Cerrar", command=self.window.destroy)
        close_btn.pack(pady=10)

    def load_data(self):
        # Limpiar tabla antes de cargar
        for item in self.tree.get_children():
            self.tree.delete(item)

        passwords = get_passwords()
        for p in passwords:
            # p = (id, service, username, password, notes)
            self.tree.insert("", "end", values=(p[1], p[2], p[3], p[4] if p[4] else ""))
