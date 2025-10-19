
import sys
sys.path.append("src")

from model.ahorros import Ahorro
from Controller.ahorros_controller import ControladorAhorros

ahorro = Ahorro( id_ahorro=None, cedula="", meta=0, meses=0, ahorro_mensual=0, objetivo="", abonos_extras=0, mes_abono_extra=0, interes=0 )

ahorro.cedula = input("Ingrese el número de cédula: ")
ahorro.meta = float(input("Ingrese la meta total de ahorro: "))
ahorro.meses = int(input("Ingrese la cantidad de meses: "))
ahorro.ahorro_mensual = float(input("Ingrese el valor del ahorro mensual: "))
ahorro.objetivo = input("Ingrese el objetivo del ahorro (opcional): ")

ControladorAhorros.insertar( ahorro.cedula, ahorro.meta, ahorro.meses, ahorro.ahorro_mensual, ahorro.objetivo, ahorro.abonos_extras, ahorro.mes_abono_extra, ahorro.interes )

print("Ahorro insertado exitosamente!")