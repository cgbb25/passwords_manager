import tkinter as tk
from tkinter import messagebox
from database import get_passwords  # Asumo que devuelve lista con (id, service, username, password, notes)

class SearchPasswordWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Buscar Contraseña")
        self.window.geometry("450x250")

        frame = tk.Frame(self.window)
        frame.pack(padx=20, pady=20)

        # Entradas para servicio y usuario
        tk.Label(frame, text="Servicio:").grid(row=0, column=0, sticky="e", pady=5)
        self.service_entry = tk.Entry(frame, width=30)
        self.service_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="e", pady=5)
        self.user_entry = tk.Entry(frame, width=30)
        self.user_entry.grid(row=1, column=1, pady=5)

        # Botón buscar
        search_button = tk.Button(frame, text="Buscar", command=self.search_password)
        search_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Mostrar contraseña y notas (solo lectura)
        tk.Label(frame, text="Contraseña:").grid(row=3, column=0, sticky="e", pady=5)
        self.password_var = tk.StringVar()
        self.password_label = tk.Entry(frame, textvariable=self.password_var, state="readonly", width=30)
        self.password_label.grid(row=3, column=1, pady=5)

        tk.Label(frame, text="Notas:").grid(row=4, column=0, sticky="e", pady=5)
        self.notes_var = tk.StringVar()
        self.notes_label = tk.Entry(frame, textvariable=self.notes_var, state="readonly", width=30)
        self.notes_label.grid(row=4, column=1, pady=5)

        # Botón cerrar
        close_button = tk.Button(frame, text="Cerrar", command=self.window.destroy)
        close_button.grid(row=5, column=0, columnspan=2, pady=15)

    def search_password(self):
        service = self.service_entry.get().strip()
        user = self.user_entry.get().strip()

        if not service or not user:
            messagebox.showerror("Error", "Por favor, ingresa servicio y usuario.")
            return

        passwords = get_passwords()
        for p in passwords:
            # p = (id, service, username, password, notes)
            if p[1] == service and p[2] == user:
                self.password_var.set(p[3])
                self.notes_var.set(p[4] if p[4] else "")
                return

        messagebox.showinfo("No encontrado", "No se encontró la contraseña para ese servicio y usuario.")
        self.password_var.set("")
        self.notes_var.set("")
