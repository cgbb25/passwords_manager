import sqlite3
from pathlib import Path
from datetime import datetime
from encryption import*

# Crea carpeta si no existe
directorio_actual = Path(__file__).parent
nombre_carpeta = "historial"
ruta_carpeta = directorio_actual / nombre_carpeta
ruta_carpeta.mkdir(exist_ok=True)

# Ruta para la base de datos de historial
HISTORIAL_DB_PATH = Path.cwd() / nombre_carpeta / "password_manager_history.db"

def create_history_db():
    conn = sqlite3.connect(HISTORIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
            accion TEXT NOT NULL,
            hora TEXT NOT NULL,
            id_password INTEGER,
            user TEXT,
            service TEXT,
            password BLOB,
            note TEXT,
            new_user TEXT,
            new_service TEXT,
            new_password BLOB,
            new_note TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_add(id_password, user, service, password, note):
    conn = sqlite3.connect(HISTORIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (accion, hora, id_password, new_user, new_service, new_password, new_note)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', ("ADD", datetime.now().isoformat(), id_password, user, service, password, note))
    conn.commit()
    conn.close()

def log_delete(id_password, user, service, password, note):
    conn = sqlite3.connect(HISTORIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (accion, hora, id_password, user, service, password, note)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', ("DELETE", datetime.now().isoformat(), id_password, user, service, password, note))
    conn.commit()
    conn.close()

def log_edit(id_password, user, service, password, note, new_user, new_service, new_password, new_note):
    conn = sqlite3.connect(HISTORIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (accion, hora, id_password, user, service, password, note, new_user, new_service, new_password, new_note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', ("EDIT", datetime.now().isoformat(), id_password, user, service, password, note, new_user, new_service, new_password, new_note))
    conn.commit()
    conn.close()

def motrar_historial():
    conn = sqlite3.connect(HISTORIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history')  # Esto selecciona todo (incluyendo el id)
    historial = cursor.fetchall()
    conn.close()

    # Se muestra el `id` junto con los demás datos
    return [(id_historial, accion, hora, id_password, user, service, decrypt_password(password), note,
             new_user, new_service, decrypt_password(new_password), new_note) for (id_historial,
             accion, hora, id_password, user, service, password, note,
             new_user, new_service, new_password, new_note) in historial]
    
create_history_db()