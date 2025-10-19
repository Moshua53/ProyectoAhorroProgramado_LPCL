
import sys
sys.path.append("src")

from Controller.ahorros_controller import ControladorAhorros

print("\n=== EDITAR AHORRO ===")
try:
    id_ahorro = int(input("Ingrese el ID del ahorro que desea editar: ").strip())
except ValueError:
    print("\nID inválido. Debe ser un número entero.")
    sys.exit()

ahorro = ControladorAhorros.buscar_id(id_ahorro)
if not ahorro:
    print("\nNo existe ningún ahorro con ese ID.")
    print("Por favor verifique la información o cree un nuevo ahorro primero.")
    sys.exit()

print("\nDatos actuales del ahorro:")
print(f"ID:              {ahorro['id_ahorro']}")
print(f"Cédula:          {ahorro['cedula']}")
print(f"Objetivo:        {ahorro['objetivo'] or '(sin objetivo)'}")
print(f"Meta:            {ahorro['meta']}")
print(f"Meses:           {ahorro['meses']}")
print(f"Ahorro mensual:  {ahorro['ahorro_mensual']}")
print(f"Abonos extras:   {ahorro['abonos_extras']}")
print(f"Mes abono extra: {ahorro['mes_abono_extra']}")
print(f"Interés:         {ahorro['interes']}")

print("\nIngrese los nuevos valores (deje vacío si no desea modificarlo):")

nuevo_objetivo = input("Nuevo objetivo: ").strip()
nuevo_meta = input("Nueva meta total: ").strip()
nuevo_meses = input("Nuevo número de meses: ").strip()
nuevo_ahorro_mensual = input("Nuevo ahorro mensual: ").strip()
nuevo_abonos_extras = input("Nuevos abonos extras: ").strip()
nuevo_mes_abono_extra = input("Nuevo mes del abono extra: ").strip()
nuevo_interes = input("Nuevo interés (%): ").strip()

campos_a_actualizar = {}

if nuevo_objetivo:
    campos_a_actualizar["objetivo"] = nuevo_objetivo
if nuevo_meta:
    try:
        campos_a_actualizar["meta"] = float(nuevo_meta)
    except ValueError:
        print(" Meta inválida (debe ser número). Ignorada.")
if nuevo_meses:
    try:
        campos_a_actualizar["meses"] = int(nuevo_meses)
    except ValueError:
        print(" Meses inválido (debe ser entero). Ignorado.")
if nuevo_ahorro_mensual:
    try:
        campos_a_actualizar["ahorro_mensual"] = float(nuevo_ahorro_mensual)
    except ValueError:
        print(" Ahorro mensual inválido (debe ser número). Ignorado.")
if nuevo_abonos_extras:
    try:
        campos_a_actualizar["abonos_extras"] = float(nuevo_abonos_extras)
    except ValueError:
        print(" Abonos extras inválido (debe ser número). Ignorado.")
if nuevo_mes_abono_extra:
    try:
        campos_a_actualizar["mes_abono_extra"] = int(nuevo_mes_abono_extra)
    except ValueError:
        print(" Mes del abono extra inválido (debe ser entero). Ignorado.")
if nuevo_interes:
    try:
        campos_a_actualizar["interes"] = float(nuevo_interes)
    except ValueError:
        print(" Interés inválido (debe ser número). Ignorado.")

if not campos_a_actualizar:
    print("\n No se ingresaron cambios. Edición cancelada.")
else:
    try:
        ControladorAhorros.actualizar(id_ahorro, **campos_a_actualizar)
        print("\n Ahorro actualizado correctamente.")
    except Exception as e:
        print("\n Ocurrió un error al actualizar el ahorro:")
        print(e)