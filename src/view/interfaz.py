
import sys

sys.path.append("src")
from model import Modulos

try:

    meta = float(input("\nIngrese la meta del ahorro: "))
    meses = int(input("Ingrese los meses del ahorro: "))
    abono_extra = float(input("Ingrese el abono extra: "))
    interes_mensual = float(input("Ingrese la tasa de interés mensual (ej. 0.01 = 1%): "))

    ahorro_mensual = Modulos.calcular_ahorro_mensual(meta, meses, abono_extra, interes_mensual)
    print(f"\n💰 El valor del ahorro mensual es: {ahorro_mensual:.2f}\n")

    saldo = 0
    total_depositado = 0

    print("Evolución del ahorro mes a mes:\n")
    print(f"{'Mes':<5}{'Depósito':<15}{'Interés':<15}{'Saldo final':<15}")
    print("-" * 50)

    for mes in range(1, meses + 1):

        saldo += ahorro_mensual
        total_depositado += ahorro_mensual

        interes_ganado = saldo * interes_mensual
        saldo += interes_ganado

        print(f"{mes:<5}{ahorro_mensual:<15.2f}{interes_ganado:<15.2f}{saldo:<15.2f}")

    ganancia_intereses = saldo - total_depositado
    print("\n<-- Resumen final:")
    print(f"--> Total depositado por el usuario: {total_depositado:.2f}")
    print(f"--> Saldo final en la cuenta: {saldo:.2f}")
    print(f"--> Ganancia generada por intereses: {ganancia_intereses:.2f}")

except ValueError:
    print("Por favor verifique los datos ingresados.")

except Exception as error:
    print("No se puede calcular el ahorro. " + str(error))