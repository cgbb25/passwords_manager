import tkinter as tk
from tkinter import ttk
from historial import motrar_historial

class HistoryListWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Historial de Acciones")
        self.window.geometry("1000x400")

        frame = tk.Frame(self.window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear Treeview con columnas
        columns = ("action", "timestamp", "service", "user", "new_service", "new_user")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=True)

        # Definir encabezados y anchura
        self.tree.heading("action", text="Acción")
        self.tree.heading("timestamp", text="Hora")
        self.tree.heading("service", text="Servicio")
        self.tree.heading("user", text="Usuario")
        self.tree.heading("new_service", text="Nuevo Servicio")
        self.tree.heading("new_user", text="Nuevo Usuario")

        self.tree.column("action", width=100)
        self.tree.column("timestamp", width=150)
        self.tree.column("service", width=150)
        self.tree.column("user", width=150)
        self.tree.column("new_service", width=150)
        self.tree.column("new_user", width=150)

        # Cargar datos en el Treeview
        self.load_data()

        # Botón para cerrar ventana
        close_btn = tk.Button(frame, text="Cerrar", command=self.window.destroy)
        close_btn.pack(pady=10)

    def load_data(self):
        # Limpiar la tabla antes de cargar nuevos datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener historial desde la base de datos
        history = motrar_historial()

        for record in history:
            # record = (id_historial, accion, hora, id_password, user, service, password, note, new_user, new_service, new_password, new_note)
            self.tree.insert("", "end", values=(record[1], record[2], record[5], record[4], record[9], record[8]))
