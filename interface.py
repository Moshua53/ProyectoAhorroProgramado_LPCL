import Modulos

Try:

  # Datos de entrada
  meta = float(input("Ingrese la meta del ahorro: "))
  meses = float(input("Ingrese los meses del ahorro: "))
  abono_extra = float(input("Ingrese los abonos extras: "))

  # Realizar procesos
  ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)

  # Mostrar datos de salida
  print(f"El valor del ahorro es: {ahorro_mensual}")

except ValueError as error_entrada:
  print("Por favor verifique los datos ingresados.")
except Exception as e:
  print("No se puede calcular el ahorro " + str(e))
