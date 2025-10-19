
class Ahorro:
    def __init__(self, id_ahorro: int | None, cedula: str, meta: float, meses: int, ahorro_mensual: float, objetivo: str | None = None, abonos_extras: float = 0.0, mes_abono_extra: int = 0, interes: float = 0.0):
        """
        Representa un registro de la tabla 'ahorros'.
        """
        self.id_ahorro = id_ahorro
        self.cedula = cedula
        self.meta = meta
        self.meses = meses
        self.abonos_extras = abonos_extras
        self.mes_abono_extra = mes_abono_extra
        self.interes = interes
        self.ahorro_mensual = ahorro_mensual
        self.objetivo = objetivo

    def __repr__(self):
        return (f"<Ahorro id={self.id_ahorro}, cedula={self.cedula}, "
                f"meta={self.meta}, meses={self.meses}, "
                f"objetivo={self.objetivo}>")

    def is_equal(self, otro) -> bool:
        """ Verifica si esta instancia es igual a otra (para pruebas o comparación). """
        assert self.cedula == otro.cedula
        assert self.meta == otro.meta
        assert self.meses == otro.meses
        assert self.abonos_extras == otro.abonos_extras
        assert self.mes_abono_extra == otro.mes_abono_extra
        assert self.interes == otro.interes
        assert self.ahorro_mensual == otro.ahorro_mensual
        assert self.objetivo == otro.objetivo
        return True

    @classmethod
    def from_dict(cls, data: dict):
        """ Crea un objeto Ahorro desde un diccionario (útil al leer desde la BD). """
        return cls(
            id_ahorro=data.get("id_ahorro"),
            cedula=data["cedula"],
            meta=float(data["meta"]),
            meses=int(data["meses"]),
            ahorro_mensual=float(data["ahorro_mensual"]),
            objetivo=data.get("objetivo"),
            abonos_extras=float(data.get("abonos_extras", 0)),
            mes_abono_extra=int(data.get("mes_abono_extra", 0)),
            interes=float(data.get("interes", 0))
        )