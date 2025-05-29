import tkinter as tk
from tkinter import messagebox
from ui.main_window import MainWindow   # Ventana hacia MainWindow
from auth import get_master_key_hash, verify_password

# Clase de la ventana de login
class LoginWindow:
    def __init__(self, master):
        self.master = master
        
        # Frame principal
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        
        # Etiqueta y campo de contraseña
        self.label = tk.Label(self.frame, text="Contraseña maestra:")
        self.label.pack(pady=10)
        
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)
        
        # Botón para validar login
        self.login_button = tk.Button(self.frame, text="Ingresar", command=self.check_password)
        self.login_button.pack(pady=10)
        
    def check_password(self):
        entered_password = self.password_entry.get()
        stored_hash = get_master_key_hash()
        # Por ahora, la contraseña maestra es fija ("admin123")

        if stored_hash and verify_password(stored_hash, entered_password):
            messagebox.showinfo("Login exitoso", "Bienvenido!")
            # Limpiando el frame de Login
            self.frame.destroy()
            # Cargando el frame de MainLogin en el mismo "master"
            MainWindow(self.master)
        else:
            img_warning = tk.PhotoImage(file="assets/warning.png")
            self.master.iconphoto(False,img_warning)

            messagebox.showerror("Error", "Contraseña incorrecta")
            self.password_entry.delete(0, tk.END)

        img_icono = tk.PhotoImage(file="assets/icono.png")
        self.master.iconphoto(False,img_icono)
