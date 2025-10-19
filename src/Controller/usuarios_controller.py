
import sys
sys.path.append("src")

import psycopg2
import psycopg2.extras
import SecretConfig
from model.usuarios import Usuario
class ControladorUsuarios:
    """CRUD para la tabla 'usuarios'.
    Esquema esperado (crear_usuarios.sql):
    cedula VARCHAR(20) PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    correo TEXT
    """

    @staticmethod
    def obtener_cursor():
        connection = psycopg2.connect(
        database=SecretConfig.PGDATABASE,
        user=SecretConfig.PGUSER,
        password=SecretConfig.PGPASSWORD,
        host=SecretConfig.PGHOST,
        port=SecretConfig.PGPORT,
        )
        return connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    @staticmethod
    def insertar(usuario:Usuario) -> None:
        cursor = ControladorUsuarios.obtener_cursor()
        cursor.execute(
            """
            INSERT INTO usuarios (cedula, nombre, apellido, correo)
            VALUES (%s, %s, %s, %s);
            """,
            (usuario.cedula, usuario.nombre, usuario.apellido, usuario.correo),
        )
        cursor.connection.commit()
        cursor.close()
    
    @staticmethod
    def listar(limit: None, offset: int = 0) -> list[dict]:
        cursor = ControladorUsuarios.obtener_cursor()
        if limit is None:
            cursor.execute(
            """
            SELECT cedula, nombre, apellido, correo
            FROM usuarios
            ORDER BY apellido, nombre;
            """
            )
        else:
            cursor.execute(
            """
            SELECT cedula, nombre, apellido, correo
            FROM usuarios
            ORDER BY apellido, nombre
            LIMIT %s OFFSET %s;
            """,
            (limit, offset),
            )
            rows = cursor.fetchall()
            cursor.close()
            return [dict(r) for r in rows]


    @staticmethod
    def actualizar(cedula: str, **campos) -> None:
        if not campos:
            return
        set_clause = ", ".join([f"{k} = %s" for k in campos.keys()])
        params = list(campos.values()) + [cedula]
        cursor = ControladorUsuarios.obtener_cursor()
        cursor.execute(
        f"UPDATE usuarios SET {set_clause} WHERE cedula = %s;",
        params,
        )
        cursor.connection.commit()
        cursor.close()


    @staticmethod
    def eliminar(cedula: str) -> None:
        cursor = ControladorUsuarios.obtener_cursor()
        cursor.execute("DELETE FROM usuarios WHERE cedula = %s;", (cedula,))
        cursor.connection.commit()
        cursor.close()