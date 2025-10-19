
import sys
sys.path.append("src")

from model.usuarios import Usuario
from Controller.usuarios_controller import ControladorUsuarios

usuario  = Usuario( cedula="", nombre="", apellido="", correo="" )

print("Por favor ingrese los datos del usuario que desea crear")

usuario.cedula = input("Cedula : ")
usuario.nombre = input("Nombre : ")
usuario.apellido = input("Apellido : ")
usuario.correo = input("Correo : ")

ControladorUsuarios.insertar( usuario )

print("Usuario insertado correctamente!")