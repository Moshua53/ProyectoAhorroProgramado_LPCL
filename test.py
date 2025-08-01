def calcular_ahorro_mesual(meta:int, meses:int, abono:int)->float:
    """Permite calcular el ahorro mesual que se debe realizar para llegar a la meta del ahorro programado"""
    return (meta/meses)+abono

def prueba():
    #Entradas
    meta= 1_200_000
    meses= 12
    abonos_extra= 0

    #Probar salidas
    ahorro_mensual= calcular_ahorro_mesual(meta, meses, abonos_extra)

    #Salidas
    ahorro_mensual_esperado = 100_000

    if ahorro_mensual_esperado == ahorro_mensual:
        print("Prueba pasada")
    else:
        print("Prueba fallida")

prueba()
