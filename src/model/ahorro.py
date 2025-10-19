class Ahorro:
    def __init__(self, id_ahorro=None, cedula=None, meta=None, meses=None,
                 ahorro_mensual=None, objetivo=None,
                 abonos_extras=0, mes_abono_extra=0, interes=0):
        self.id_ahorro = id_ahorro
        self.cedula = cedula
        self.meta = meta
        self.meses = meses
        self.ahorro_mensual = ahorro_mensual
        self.objetivo = objetivo
        self.abonos_extras = abonos_extras
        self.mes_abono_extra = mes_abono_extra
        self.interes = interes

    def is_equal(self, comparar_con):
        """
        Compara el objeto actual con otra instancia de la clase Ahorro
        """
        assert(self.cedula == comparar_con.cedula)
        assert(self.meta == comparar_con.meta)
        assert(self.meses == comparar_con.meses)
        assert(self.ahorro_mensual == comparar_con.ahorro_mensual)
        assert(self.objetivo == comparar_con.objetivo)
        assert(self.abonos_extras == comparar_con.abonos_extras)
        assert(self.mes_abono_extra == comparar_con.mes_abono_extra)
        assert(self.interes == comparar_con.interes)
        return True
