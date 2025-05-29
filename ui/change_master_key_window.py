import tkinter as tk
from tkinter import messagebox
from auth import *

class ChangeMasterKeyWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Cambiar Clave Maestra")
        self.window.geometry("400x250")

        frame = tk.Frame(self.window)
        frame.pack(padx=20, pady=20)

        # Clave actual
        tk.Label(frame, text="Clave Maestra Actual:").grid(row=0, column=0, sticky="e", pady=5)
        self.current_entry = tk.Entry(frame, show="*")
        self.current_entry.grid(row=0, column=1, pady=5)

        # Nueva clave
        tk.Label(frame, text="Nueva Clave Maestra:").grid(row=1, column=0, sticky="e", pady=5)
        self.new_entry = tk.Entry(frame, show="*")
        self.new_entry.grid(row=1, column=1, pady=5)

        # Confirmar nueva clave
        tk.Label(frame, text="Confirmar Nueva Clave:").grid(row=2, column=0, sticky="e", pady=5)
        self.confirm_entry = tk.Entry(frame, show="*")
        self.confirm_entry.grid(row=2, column=1, pady=5)

        # Botón para guardar
        save_button = tk.Button(frame, text="Guardar Cambios", command=self.change_key)
        save_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Botón para cerrar
        close_button = tk.Button(frame, text="Cerrar", command=self.window.destroy)
        close_button.grid(row=4, column=0, columnspan=2)

    def change_key(self):
        current = self.current_entry.get()
        new = self.new_entry.get()
        confirm = self.confirm_entry.get()

        if not current or not new or not confirm:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        if new != confirm:
            messagebox.showerror("Error", "Las nuevas claves no coinciden.")
            return

        stored_hash = get_master_key_hash()
        if not verify_password(stored_hash, current):
            messagebox.showerror("Error", "Clave maestra actual incorrecta.")
            return

        new_hash = hash_password(new)
        save_master_key_hash(new_hash)
        messagebox.showinfo("Éxito", "Clave maestra actualizada correctamente.")
        self.window.destroy()