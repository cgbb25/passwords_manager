from cryptography.fernet import Fernet
from pathlib import Path

# Modulo para las funciones de encriptacion
def generate_key(ruta_archivo):
    if not Path(ruta_archivo).exists():
        key = Fernet.generate_key()
        with open(ruta_archivo,"wb") as key_file:
            key_file.write(key)

# Cargar la clave de encriptación desde el archivo
def load_key():
    return open("secret.key", "rb").read()

# Cifrar la contraseña antes de guardarla
def encrypt_password(password):
    fernet = Fernet(load_key())
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Desencriptar la contraseña cuando se lee
def decrypt_password(encrypted_password):
    if encrypted_password is None:
        return None
    
    fernet = Fernet(load_key())
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

generate_key('secret.key')