import tkinter as tk
from tkinter import messagebox
from ui.add_password_window import AddPasswordWindow
from ui.edit_password_window import EditPasswordWindow
from ui.delete_password_window import DeletePasswordWindow
from ui.change_master_key_window import ChangeMasterKeyWindow
from ui.search_password_window import SearchPasswordWindow
from ui.password_list_window import PasswordListWindow
from ui.history_list_window import HistoryListWindow

from database import get_passwords
from historial import motrar_historial

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Administrador de Contraseñas - Principal")
        self.master.geometry("600x500")

        # Interceptar evento de cierre de ventana para mostrar confirmación
        self.master.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        
        # Frame principal
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Label de bienvenida
        self.label = tk.Label(self.frame, text="Bienvenido al Administrador de Contraseñas", font=("Arial", 16))
        self.label.pack(pady=20)
        
        # Botón para agregar nueva contraseña
        self.add_button = tk.Button(self.frame, text="Agregar nueva contraseña", width=30, command=self.add_password)
        self.add_button.pack(pady=10)

        # Botón para editar contraseña
        self.edit_button = tk.Button(self.frame, text="Editar contraseña", width=30, command=self.update_password)
        self.edit_button.pack(pady=10)

        # Botón para eliminar contraseña
        self.edit_button = tk.Button(self.frame, text="Eliminar contraseña", width=30, command=self.delete_password)
        self.edit_button.pack(pady=10)

        # Mostrar lista
        self.edit_button = tk.Button(self.frame, text="Buscar contraseña", width=30, command=self.search_password)
        self.edit_button.pack(pady=10)

        # Cambiar contraseña maestra
        self.edit_button = tk.Button(self.frame, text="Editar contraseña maestra", width=30, command=self.edit_master_key)
        self.edit_button.pack(pady=10)

        # Lista de contraseñas
        self.edit_button = tk.Button(self.frame, text="Lista de contraseñas", width=30, command=self.password_list)
        self.edit_button.pack(pady=10)

        # Lista de contraseñas
        self.edit_button = tk.Button(self.frame, text="Historial", width=30, command=self.history_list)
        self.edit_button.pack(pady=10)
        
        # Botón para salir
        self.exit_button = tk.Button(self.frame, text="Salir", width=30, command=self.confirm_exit)
        self.exit_button.pack(pady=10)

        # Instancia para ver que las ventanas no abrir más de una vez una ventana
        self.add_password_window = None
        self.edit_password_window = None
        self.delete_password_window = None
        self.edit_master_key_window = None
        self.search_password_window = None
        self.password_list_window = None
        self.history_list_window = None
        
    def add_password(self):
        # Si la ventana ya está abierta, solo se enfoca
        if self.add_password_window is not None and tk.Toplevel.winfo_exists(self.add_password_window.window):
            self.add_password_window.window.lift()
            self.add_password_window.window.focus_force()
            return
        
        # Abre la ventana para agregar una nueva contraseña
        self.add_password_window = AddPasswordWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.add_password_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_add_password_window_close
        )
    
    def update_password(self):
        # Si la ventana ya está abierta, solo se enfoca
        if self.edit_password_window is not None and tk.Toplevel.winfo_exists(self.edit_password_window.window):
            self.edit_password_window.window.lift()
            self.edit_password_window.window.focus_force()
            return

        # Abre la ventana para editar una contraseña existente
        self.edit_password_window = EditPasswordWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.edit_password_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_edit_password_window_close
        )

    def delete_password(self):
        # Si la ventana ya está abierta, solo se enfoca
        if self.delete_password_window is not None and tk.Toplevel.winfo_exists(self.delete_password_window.window):
            self.delete_password_window.window.lift()
            self.delete_password_window.window.focus_force()
            return
        
        # Abre la ventana para eliminar contraseña
        self.delete_password_window = DeletePasswordWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.delete_password_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_delete_password_window_close
        )
    
    def search_password(self):
        # Si la ventana ya está abierta, solo se enfoca
        if self.search_password_window is not None and tk.Toplevel.winfo_exists(self.search_password_window.window):
            self.search_password_window.window.lift()
            self.search_password_window.window.focus_force()
            return
        
        self.search_password_window = SearchPasswordWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.search_password_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_search_password_window_close
        )

    def mostrar_passwords(self):
        print("Mostrando ...")
        print(get_passwords())
        print(motrar_historial())

    def edit_master_key(self):
        if self.edit_master_key_window is not None and tk.Toplevel.winfo_exists(self.edit_master_key_window.window):
            self.edit_master_key_window.window.lift()
            self.edit_master_key_window.window.focus_force()
            return
            
        self.edit_master_key_window = ChangeMasterKeyWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.edit_master_key_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_edit_master_key_window_close
        )

    def password_list(self):
        if self.password_list_window is not None and tk.Toplevel.winfo_exists(self.password_list_window.window):
            self.password_list_window.window.lift()
            self.password_list_window.window.focus_force()
            return
            
        self.password_list_window = PasswordListWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.password_list_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_password_list_window_close
        )
    
    def history_list(self):
        if self.history_list_window is not None and tk.Toplevel.winfo_exists(self.history_list_window.window):
            self.history_list_window.window.lift()
            self.history_list_window.window.focus_force()
            return
            
        self.history_list_window = HistoryListWindow(self.master)

        # Cuando la ventana se cierre, se elimina la referencia
        self.history_list_window.window.protocol(
            "WM_DELETE_WINDOW", self.on_history_list_window_close
        )

    def on_add_password_window_close(self):
        # Cuando la ventana AddPasswordWindow se cierre, se elimina la referencia
        if self.add_password_window is not None:
            self.add_password_window.window.destroy()
            self.add_password_window = None
    
    def on_edit_password_window_close(self):
        # Cuando la ventana EditPasswordWindow se cierre, se elimina la referencia
        if self.edit_password_window is not None:
            self.edit_password_window.window.destroy()
            self.edit_password_window = None

    def on_delete_password_window_close(self):
        # Cuando la ventana DeletePasswordWindow se cierre, se elimina la referencia
        if self.delete_password_window is not None:
            self.delete_password_window.window.destroy()
            self.delete_password_window = None
    
    def on_search_password_window_close(self):
        # Cuando la ventana DeletePasswordWindow se cierre, se elimina la referencia
        if self.search_password_window is not None:
            self.search_password_window.window.destroy()
            self.search_password_window = None

    def on_edit_master_key_window_close(self):
        # Cuando la ventana DeletePasswordWindow se cierre, se elimina la referencia
        if self.edit_master_key_window is not None:
            self.edit_master_key_window.window.destroy()
            self.edit_master_key_window = None

    def on_password_list_window_close(self):
        # Cuando la ventana DeletePasswordWindow se cierre, se elimina la referencia
        if self.password_list_window is not None:
            self.password_list_window.window.destroy()
            self.password_list_window = None

    def on_history_list_window_close(self):
        # Cuando la ventana DeletePasswordWindow se cierre, se elimina la referencia
        if self.history_list_window is not None:
            self.history_list_window.window.destroy()
            self.history_list_window = None

    def confirm_exit(self):
        respuesta = messagebox.askyesno("Salir","¿Estás seguro que deseas salir?")
        if respuesta:
            self.master.destroy()