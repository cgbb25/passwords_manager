import bcrypt
from pathlib import Path
import sqlite3

# Crea carpeta si no existe
directorio_actual = Path(__file__).parent
nombre_carpeta = "auth"
ruta_carpeta = directorio_actual / nombre_carpeta
ruta_carpeta.mkdir(exist_ok=True)

# Ruta para la base de datos de historial
MASTER_KEY_DB_PATH = Path.cwd() / nombre_carpeta / "master_key.db"

def create_master_key_db():
    conn = sqlite3.connect(MASTER_KEY_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS master_key (
            id INTEGER PRIMARY KEY,
            hashed_key BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_master_key_hash():
    conn = sqlite3.connect(MASTER_KEY_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT hashed_key FROM master_key WHERE id=1')
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def save_master_key_hash(hashed_key):
    conn = sqlite3.connect(MASTER_KEY_DB_PATH)
    cursor = conn.cursor()
    if get_master_key_hash() is None:
        cursor.execute('INSERT INTO master_key (id, hashed_key) VALUES (1, ?)', (hashed_key,))
    else:
        cursor.execute('UPDATE master_key SET hashed_key = ? WHERE id=1', (hashed_key,))
    conn.commit()
    conn.close()

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(stored_hash, password_attempt):
    return bcrypt.checkpw(password_attempt.encode(), stored_hash)

# Inicializar la base y crear el hash de "admin123" si no existe
def initialize_master_key():

    create_master_key_db()
    if get_master_key_hash() is None:
        hashed = hash_password("admin123")
        save_master_key_hash(hashed)

initialize_master_key()