
import sys
sys.path.append("src")

from Controller.usuarios_controller import ControladorUsuarios

print("\n=== EDITAR USUARIO ===")
cedula = input("Ingrese la cédula del usuario que desea editar: ").strip()

usuario = ControladorUsuarios.buscar_por_cedula(cedula)
if not usuario:
    print("\nNo existe ningún usuario con esa cédula.")
    print("Por favor verifique la información o cree el usuario primero.")
    sys.exit()

print("\n📋 Datos actuales del usuario:")
print(f"Nombre:   {usuario['nombre']}")
print(f"Apellido: {usuario['apellido']}")
print(f"Correo:   {usuario['correo']}")

print("\nIngrese los nuevos datos (deje vacío para no cambiar):")

nuevo_nombre = input("Nuevo nombre: ").strip()
nuevo_apellido = input("Nuevo apellido: ").strip()
nuevo_correo = input("Nuevo correo: ").strip()

campos_a_actualizar = {}
if nuevo_nombre:
    campos_a_actualizar["nombre"] = nuevo_nombre
if nuevo_apellido:
    campos_a_actualizar["apellido"] = nuevo_apellido
if nuevo_correo:
    campos_a_actualizar["correo"] = nuevo_correo

if not campos_a_actualizar:
    print("\nNo se ingresaron cambios. Edición cancelada.")
else:
    try:
        ControladorUsuarios.actualizar(cedula, **campos_a_actualizar)
        print("\nUsuario actualizado correctamente.")
    except Exception as e:
        print("\nOcurrió un error al actualizar el usuario:")
        print(e)