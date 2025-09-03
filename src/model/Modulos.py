
class ErrorValorMeta(Exception):
    """ Valor de la meta debe ser mayor a cero """
    def __init__(self,):
        super().__init__("ERROR: El valor de la meta debe ser mayor que cero")


class ErrorValorMeses(Exception):
    """ Valor de los meses debe ser mayor a cero """
    def __init__(self,):
        super().__init__("ERROR: El valor de los meses debe ser mayor que cero")


class ErrorAbonoExcesivo(Exception):
    """ La meta ya fue superada con los abonos, ahorro innecesario """
    def __init__(self,):
        super().__init__("ERROR: La meta ya fue superada con los abonos")


def calcular_ahorro_mensual(meta: float, meses: int, abono_extra: float, interes_mensual: float = 0.0) -> float:
    """
    Calcula el ahorro mensual necesario para alcanzar una meta de ahorro,
    teniendo en cuenta un abono extra inicial y los intereses mensuales.

    :param meta: Meta de ahorro (valor futuro)
    :param meses: Número de meses
    :param abono_extra: Abono inicial extra
    :param interes_mensual: Tasa de interés mensual (ejemplo 0.01 = 1%)
    :return: Valor del ahorro mensual necesario
    """

    if meta <= 0:
        raise ErrorValorMeta()

    if meses <= 0:
        raise ErrorValorMeses()

    if interes_mensual == 0:
        if (meta / meses) + abono_extra > meta:
            raise ErrorAbonoExcesivo()
        return (meta - abono_extra) / meses
    
    factor = ((1 + interes_mensual) ** meses - 1) / interes_mensual
    numerador = meta - abono_extra * (1 + interes_mensual) ** meses

    if numerador <= 0:
        raise ErrorAbonoExcesivo()

    return numerador / factor
