
import sys

sys.path.append("src")
from model import Modulos

try:
  # Datos de entrada
  meta = float(input("Ingrese la meta del ahorro: "))
  meses = float(input("Ingrese los meses del ahorro: "))
  abono_extra = float(input("Ingrese el abono extra: "))

  # Realizar procesos
  ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)

  # Mostrar datos de salida
  print(f"El valor del ahorro mensual es: {ahorro_mensual}")

except ValueError as error_entrada:
  print("Por favor verifique los datos ingresados.")

except Exception as error:
  print("No se puede calcular el ahorro " + str(error))
