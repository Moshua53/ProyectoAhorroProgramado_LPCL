class ErrprValorAhorro( Exception ):
    """ Valor de la meta debe ser mayor a cero """

    def __init__ (self, *args):
        super().__init__("ERROR: El valor de la meta debe ser mayor que cero

class ErrorAbonoExcesivo( Exception ):
    pass

def calcular_ahorro_mesual(meta: int, meses: int, abono: int) -> float:
    """ Permite calcular el ahorro mensual que se debe realizar para llegar a la meta del ahorro programado """

    if meta < 0:
        raise ValueError("La meta no puede ser negativa")

    if meses <= 0:
        raise ValueError("El número de meses debe ser mayor que cero")

    if (meta / meses) + abono > meta:
        raise ValueError("La meta ya fue superada con los abonos, ahorro innecesario")

    return (meta / meses) + abono

