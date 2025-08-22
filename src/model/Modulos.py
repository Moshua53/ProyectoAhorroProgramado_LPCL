class ErrorValorMeta( Exception ):
    """ Valor de la meta debe ser mayor a cero """

    def __init__ (self, *args):
        super().__init__("ERROR: El valor de la meta debe ser mayor que cero")
                         
class ErrorValorMeses( Exception ):
    """Valor de los meses debe ser mayor que cero """

    def __init__ (self, *args):
        super().__init__("ERROR: el valor de los meses debe ser mayor que cero")

class ErrorAbonoExcesivo( Exception ):
    """La meta ya fue superada con los abonos, ahorro innecesario"""
    def __init__ (self, *args):
        super().__init__("ERROR: El valor de la meta debe ser mayor que cero")

def calcular_ahorro_mesual(meta: int, meses: int, abono: int) -> float:
    """ Permite calcular el ahorro mensual que se debe realizar para llegar a la meta del ahorro programado """

    if meta < 0:
        raise ErrorValorMeta()

    if meses <= 0:
        raise ErrorValorMeses()

    if (meta / meses) + abono > meta:
        raise ErrorAbonoExcesivo()

    return (meta - abono)/ meses
