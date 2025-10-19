import sys
sys.path.append("src")

import psycopg2
import psycopg2.extras
import SecretConfig

class ControladorAhorros:

    @staticmethod
    def obtener_cursor():
        """ Crea la conexión y retorna un cursor dict. """
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        return connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # --------- TABLA ---------
    @staticmethod
    def crear_tabla():
        """ Crea la tabla ahorros (FK a usuarios y columna objetivo). """
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ahorros (
                id_ahorro         SERIAL PRIMARY KEY,
                cedula            VARCHAR(20) NOT NULL,
                meta              NUMERIC(14,2) NOT NULL,
                meses             INT NOT NULL CHECK (meses > 0),
                abonos_extras     NUMERIC(14,2) DEFAULT 0,
                mes_abono_extra   INT DEFAULT 0,
                interes           NUMERIC(6,3) DEFAULT 0,
                ahorro_mensual    NUMERIC(14,2) NOT NULL,
                objetivo          VARCHAR(255),
                CONSTRAINT fk_ahorros_usuarios
                    FOREIGN KEY (cedula)
                    REFERENCES usuarios(cedula)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            );
        """)
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def eliminar_tabla():
        """ Borra la tabla ahorros. """
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute("DROP TABLE IF EXISTS ahorros;")
        cursor.connection.commit()
        cursor.close()

    def insertar(cedula: str, meta: float, meses: int,
                 ahorro_mensual: float, objetivo: str | None = None,
                 abonos_extras: float = 0, mes_abono_extra: int = 0,
                 interes: float = 0) -> int:
        """ Inserta un ahorro y retorna el id_ahorro creado. """
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute(
            """INSERT INTO ahorros
               (cedula, meta, meses, abonos_extras, mes_abono_extra,
                interes, ahorro_mensual, objetivo)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
               RETURNING id_ahorro;""",
            (cedula, meta, meses, abonos_extras, mes_abono_extra,
             interes, ahorro_mensual, objetivo)
        )
        new_id = cursor.fetchone()["id_ahorro"]
        cursor.connection.commit()
        cursor.close()
        return int(new_id)

    def buscar_por_cedula(cedula: str) -> list[dict]:
        """ Devuelve todos los ahorros de un usuario. """
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute(
            """SELECT id_ahorro, cedula, objetivo, meta, meses,
                      ahorro_mensual, abonos_extras, mes_abono_extra, interes
               FROM ahorros
               WHERE cedula = %s
               ORDER BY id_ahorro DESC;""",
            (cedula,)
        )
        filas = cursor.fetchall()
        cursor.close()
        return [dict(f) for f in filas]


    def buscar_id(id_ahorro: int) -> dict | None:
        """ Trae un ahorro por id. """
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute(
            """SELECT id_ahorro, cedula, objetivo, meta, meses,
                      ahorro_mensual, abonos_extras, mes_abono_extra, interes
               FROM ahorros WHERE id_ahorro = %s;""",
            (id_ahorro,)
        )
        fila = cursor.fetchone()
        cursor.close()
        return dict(fila) if fila else None

    def actualizar(id_ahorro: int, **campos) -> None:
        """ Actualiza campos del ahorro. Ej: actualizar(5, objetivo='Viaje', interes=1.2) """
        if not campos:
            return
        set_clause = ", ".join([f"{k} = %s" for k in campos.keys()])
        params = list(campos.values()) + [id_ahorro]
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute(f"UPDATE ahorros SET {set_clause} WHERE id_ahorro = %s;", params)
        cursor.connection.commit()
        cursor.close()

    def eliminar(id_ahorro: int) -> None:
        """ Elimina un ahorro por id. """
        cursor = ControladorAhorros.obtener_cursor()
        cursor.execute("DELETE FROM ahorros WHERE id_ahorro = %s;", (id_ahorro,))
        cursor.connection.commit()
        cursor.close()