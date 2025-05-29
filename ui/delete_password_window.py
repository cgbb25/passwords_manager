import tkinter as tk
from tkinter import messagebox
from database import get_passwords, delete_password

class DeletePasswordWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Eliminar Contraseña")
        self.window.geometry("600x300")
        
        self.frame = tk.Frame(self.window)
        self.frame.pack(padx=20, pady=20)

        # Campos para buscar contraseña
        self.service_label = tk.Label(self.frame, text="Servicio:")
        self.service_label.grid(row=0, column=0, pady=5, sticky="e")
        self.service_entry = tk.Entry(self.frame, width=30)
        self.service_entry.grid(row=0, column=1, pady=5)

        self.user_label = tk.Label(self.frame, text="Usuario:")
        self.user_label.grid(row=1, column=0, pady=5, sticky="e")
        self.user_entry = tk.Entry(self.frame, width=30)
        self.user_entry.grid(row=1, column=1, pady=5)

        self.search_button = tk.Button(self.frame, text="Buscar", width=20, command=self.search_password)
        self.search_button.grid(row=2, column=0, pady=10, columnspan=2)

        # Campos para editar la contraseña
        self.password_label = tk.Label(self.frame, text="Contraseña:")
        self.password_label.grid(row=3, column=0, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=5)
        self.password_entry.config(state="readonly")

        # Checkbutton para mostrar/ocultar la contraseña
        self.show_password_button = tk.Checkbutton(self.frame, text="Mostrar Contraseña", command=self.toggle_password)
        self.show_password_button.grid(row=3, column=2, pady=5, padx=10, sticky="w")

        self.notes_label = tk.Label(self.frame, text="Notas:")
        self.notes_label.grid(row=4, column=0, pady=5, sticky="e")
        self.notes_entry = tk.Entry(self.frame, width=30)
        self.notes_entry.grid(row=4, column=1, pady=5)
        self.notes_entry.config(state="readonly")

        self.save_button = tk.Button(self.frame, text="Eliminar contraseña", width=20, command=self.delete_data)
        self.save_button.grid(row=5, column=0, pady=10, columnspan=2)

        # Botón de cerrar
        self.close_button = tk.Button(self.frame, text="Cerrar", width=20, command=self.window.destroy)
        self.close_button.grid(row=5, column=2, pady=10)

        # Variable del id del password
        self.password_id = None

    def search_password(self):
        service = self.service_entry.get().strip()
        user = self.user_entry.get().strip()

        passwords = get_passwords()
        found = False
        for password in passwords:
            if password[1] == service and password[2] == user:
                # Si encontramos la contraseña, la precargamos
                self.password_id = password[0]
                print(password[0])
                self.password_entry.config(state="normal")
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, password[3])  # Contraseña desencriptada
                self.password_entry.config(state="readonly")

                self.notes_entry.config(state="normal")
                self.notes_entry.delete(0, tk.END)
                self.notes_entry.insert(0, password[4])  # Notas
                self.notes_entry.config(state="readonly")
                found = True
                break
        
        if not found:
            messagebox.showerror("Error", "No se encontró la contraseña con esos datos.")
    
    def toggle_password(self):
        """Alternar entre mostrar y ocultar la contraseña."""
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def delete_data(self):
        
        # Mensaje de confirmacion
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de proceder con la eliminación?")
        if not confirm:
            return

        if self.password_id:
            delete_password(self.password_id)
            messagebox.showinfo("Actualizado", "Contraseña eliminada con éxito!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "No se ha seleccionado una contraseña para eliminar")