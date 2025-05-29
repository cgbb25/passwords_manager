import tkinter as tk
from ui.login_window import LoginWindow

def main():
    # Crear ventana principal de la app
    root = tk.Tk()
    root.title("Administrador de Contraseñas")
    root.geometry("400x300")  # Tamaño inicial de la ventana
    root.resizable(False,False) # No se puede redimensionar la pantalla
    icono = tk.PhotoImage(file="assets/icono.png")
    root.iconphoto(False,icono)

    # Instanciar y mostrar la ventana de login
    app = LoginWindow(root)
    
    # Iniciar loop principal de eventos
    root.mainloop()

if __name__ == "__main__":
    main()
