# Gestor de Contraseñas — Aplicación de Escritorio

## Descripción General

Este proyecto es una aplicación de escritorio con interfaz gráfica (GUI) para la gestión segura de contraseñas. El usuario accede mediante una **clave maestra**, que por defecto es `"admin123"`, y puede modificarla posteriormente desde la aplicación.

La aplicación permite almacenar, editar, eliminar y buscar contraseñas asociadas a diferentes servicios, junto con notas opcionales. Además, lleva un registro (historial) de las modificaciones y eliminaciones realizadas para auditoría.

---

## Estructura del Proyecto

├── assets/ # Recursos adicionales, imágenes y iconos

├── ui/ # Paquete con ventanas gráficas (Tkinter)

│ ├── add_password_window.py # Añadir nueva contraseña

│ ├── change_master_key_window.py # Cambiar clave maestra

│ ├── delete_password_window.py # Eliminar contraseña

│ ├── edit_password_window.py # Editar contraseña

│ ├── history_list_window.py # Mostrar historial de acciones

│ ├── login_window.py # Ventana de login

│ ├── main_window.py # Ventana principal con funciones

│ ├── password_list_window.py # Mostrar lista de contraseñas

│ ├── search_password_window.py # Buscar contraseña por servicio y usuario

├── auth.py # Funciones de autenticación y hashing de clave maestra

├── database.py # Funciones para gestión de base de datos de contraseñas

├── encryption.py # Funciones para encriptar/desencriptar contraseñas (Fernet)

├── historial.py # Gestión de base de datos de historial de uso

├── main.py # Punto de entrada para ejecutar la aplicación

├── mostrar_data.py # Archivo auxiliar para mostrar datos en lista

├── requirements.txt # Librerías necesarias para instalar el entorno

---

## Características Principales

- **Clave maestra protegida con hashing** (bcrypt). La clave inicial es `"admin123"` pero puede ser cambiada por el usuario.
- **Gestión completa de contraseñas**: agregar, editar, eliminar, buscar y listar.
- **Historial de uso**: se guarda un registro con fecha y detalles de cada edición o eliminación.
- **Encriptación de contraseñas** usando el paquete `cryptography` (Fernet).
- **Interfaz intuitiva y modular**, organizada en múltiples ventanas para cada función.
- **Validaciones** para evitar duplicados y confirmar acciones importantes.
- **Sensibilidad a mayúsculas y minúsculas** en servicios, usuarios y contraseñas.

---

## Instalación y Ejecución

1. **Clonar el repositorio** o descargar el proyecto.
2. **Crear un entorno virtual** en la carpeta raíz (opcional pero recomendado):

---

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

---

3. **Instalar las dependencias:**

4. **Ejecutar la aplicación:**

## Carpetas y Archivos Generados

Al ejecutar por primera vez, el programa crea dos carpetas para almacenamiento:

- historial/: contiene la base de datos con el historial de acciones.

- auth/: contiene la clave maestra cifrada (hash).

- El archivo secret.key se generará en la carpeta raíz de la carpeta

## Consideraciones del Programa

- La aplicación distingue entre mayúsculas y minúsculas para todos los campos (servicio, usuario, contraseña y notas).

- Se recomienda futuras mejoras para implementar búsquedas y comparaciones insensibles a mayúsculas.

- El historial registra solo modificaciones y eliminaciones, no accesos de lectura.

## Posibles Mejoras Futuras

- Añadir funcionalidad para exportar/importar contraseñas cifradas.

- Implementar autenticación por biometría o PIN adicional.

- Añadir búsqueda avanzada con filtro insensible a mayúsculas y ordenamiento.

- Mejorar la seguridad del archivo de clave (secret.key) con métodos de protección externos.

- Implementar notificaciones o alertas de seguridad ante accesos sospechosos.

- Añadir funcionalidad para copiar contraseñas al portapapeles con timeout automático.

- Incorporar un modo oscuro para la interfaz gráfica.

## Consideraciones Finales y Aclaraciones

1. ***Proposito Educativo y Demostrativo***

Esta aplicación está diseñada principalmente con fines educativos y en se hace uso de habilidades en desarrollo de software, criptografía y gestión segura de datos. No pretende ser una solución definitiva o lista para producción en entornos sensibles. Se recomienda evaluar cuidadosamente antes de usarla para gestionar contraseñas reales y considerar futuras mejoras para robustecer su seguridad y funcionalidad.

2. ***Apertura a Sugerencias y Mejoras***

Se agradecen contribuciones y feedback constructivo para enriquecer el proyecto. Sin embargo, la atención a estas propuestas dependerá del tiempo disponible y prioridades del autor.

## Licencia

Este proyecto es para fines demostrativos y educativos. No está diseñado para producción sin auditoría de seguridad adicional

## Contacto

Para dudas, sugerencias o contribuciones, contactar a:
carlosgbaltodanoing@gmail.com

