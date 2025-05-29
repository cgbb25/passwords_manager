import sqlite3
from encryption import*
from historial import*

# Paquete de funciones para la base de datos de contraseñas
# Crear la base de datos y la tabla si no existe
def create_db():
    
    # Si la base de datos no existe, la creará automátocamente
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password BLOB NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Agregar una nueva contraseña a la base de datos
def add_password(service, username, password, notes):

    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (service, username, password, notes)
        VALUES (?, ?, ?, ?)
    ''', (service, username, encrypted_password, notes))
    conn.commit()
    conn.close()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, service, password, notes FROM passwords WHERE service = ? AND username = ?", (service,username))
    row = cursor.fetchone()
    conn.close()

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    id = cursor.execute("SELECT MAX(id) FROM passwords").fetchone()[0]
    conn.close()

    if row:
        user, service, password, note = row
        log_add(id, user, service, password, note)


# Obtener todas las contraseñas almacenadas
def get_passwords():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords')  # Esto selecciona todo (incluyendo el id)
    passwords = cursor.fetchall()
    conn.close()

    # Ahora, devolvemos el `id` junto con los demás datos
    return [(id, service, username, decrypt_password(password), notes) for (id, service, username, password, notes) in passwords]

# Actualizar una contraseña existente
def update_password(id, service, username, password, notes):
    # Primero obtener datos actuales del password para el historial
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, service, password, notes FROM passwords WHERE id = ?", (id,))
    before_row = cursor.fetchone()
    conn.close()

    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE passwords
        SET service = ?, username = ?, password = ?, notes = ?
        WHERE id = ?
    ''', (service, username, encrypted_password, notes, id))
    conn.commit()
    conn.close()

    if before_row:
        before_user, before_service, before_password, before_note = before_row
        log_edit(id,before_user,before_service,before_password,before_note,username,service,encrypted_password,notes)

# Eliminar una contraseña por ID
def delete_password(id):

    # Primero obtener datos actuales del password para el historial
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, service, password, notes FROM passwords WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        user, service, password, note = row
        log_delete(id, user, service, password, note)

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Crear la base de datos y las tablas cuando se inicie la app
create_db()
