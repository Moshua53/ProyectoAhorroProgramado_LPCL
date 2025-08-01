# caso normal 1

def calcular_ahorro_mesual(meta: int, meses: int, abono: int) -> float:
    """ Permite calcular el ahorro mesual que se debe realizar para llegar a la meta del ahorro programado """
    return (meta / meses) + abono


def prueba_caso_norma_1():
    # Entradas
    meta = 1_200_000
    meses = 12
    abonos_extra = 0

    # Probar salidas
    ahorro_mensual = calcular_ahorro_mesual(meta, meses, abonos_extra)

    # Salidas
    ahorro_mensual_esperado = 100_000

    if ahorro_mensual_esperado == ahorro_mensual:
        print("Prueba pasada")
    else:
        print("Prueba fallida")


# caso extraordinario 2

def calcular_ahorro_mesual(meta: int, meses: int, abono: int) -> float:
    """ Permite calcular el ahorro mesual que se debe realizar para llegar a la meta del ahorro programado """
    return (meta / meses) + abono


def prueba_caso_extraordinario_1():
    # Entradas
    meta = 1_000_000
    meses = 10
    abonos_extra = 200_000

    # Probar salidas
    ahorro_mensual = calcular_ahorro_mesual(meta, meses, abonos_extra)

    # Salidas
    ahorro_mensual_esperado = 300_000

    if ahorro_mensual_esperado == ahorro_mensual:
        print("Prueba pasada")
    else:
        print("Prueba fallida")


prueba_caso_norma_1()
prueba_caso_extraordinario_1()
