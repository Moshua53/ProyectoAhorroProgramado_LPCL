
class ErrorValorMeta(Exception):
    """Excepción lanzada cuando la meta es menor o igual a cero."""
    def __init__(self):
        super().__init__("ERROR: El valor de la meta debe ser mayor que cero")


class ErrorValorMeses(Exception):
    """Excepción lanzada cuando el número de meses es menor o igual a cero."""
    def __init__(self):
        super().__init__("ERROR: El valor de los meses debe ser mayor que cero")


class ErrorAbonoExcesivo(Exception):
    """Excepción lanzada cuando la meta ya fue superada con los abonos iniciales."""
    def __init__(self):
        super().__init__("ERROR: La meta ya fue superada con los abonos")


def calcular_ahorro_mensual(
    meta: float, meses: int, abono_extra: float, interes_mensual: float = 0.0
) -> float:
    """
    Calcula el ahorro mensual necesario para alcanzar una meta de ahorro.

    Considera un abono extra inicial y los intereses mensuales.

    Args:
        meta (float): Meta de ahorro (valor futuro).
        meses (int): Número de meses para ahorrar.
        abono_extra (float): Abono inicial extra.
        interes_mensual (float, opcional): Tasa de interés mensual (ejemplo: 0.01 = 1%).

    Returns:
        float: Valor del ahorro mensual necesario.

    Raises:
        ErrorValorMeta: Si la meta es menor o igual a cero.
        ErrorValorMeses: Si los meses son menores o iguales a cero.
        ErrorAbonoExcesivo: Si la meta ya fue alcanzada/superada con el abono extra.
    """

    if meta <= 0:
        raise ErrorValorMeta()

    if meses <= 0:
        raise ErrorValorMeses()

    if interes_mensual == 0:
        ahorro_mensual = (meta - abono_extra) / meses
        if ahorro_mensual + abono_extra > meta:
            raise ErrorAbonoExcesivo()
        return ahorro_mensual

    # Fórmula de anualidad (con interés compuesto mensual)
    factor_interes = ((1 + interes_mensual) ** meses - 1) / interes_mensual
    monto_ajustado = meta - abono_extra * (1 + interes_mensual) ** meses

    if monto_ajustado <= 0:
        raise ErrorAbonoExcesivo()

    return monto_ajustado / factor_interes