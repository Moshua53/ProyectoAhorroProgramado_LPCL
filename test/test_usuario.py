
# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

import sys
sys.path.append("src")

from datetime import date

from model.usuarios import Usuario
from Controller.usuarios_controller import ControladorAhorros

import psycopg2

class ControllerTest(unittest.TestCase):

    # Test Fixture
    def setUpClass():
        # Llamar a la clase Controlador para que cree la tabla
        ControladorAhorros.eliminar_tabla()
        ControladorAhorros.crear_tabla()

    def testInsertAndSelect1( self ):
        """ Prueba que se cree correctamente la tabla en la BD """
        # Insertar un Usuario en la tabla
        usuario_prueba  = Usuario( cedula="1234657", nombre="Prueba", apellido="Unitaria", correo="no@tiene.com" )
        ControladorAhorros.insertar_usuario( usuario_prueba )

        # Verificar si la tabla quedo creada correctamente
        usuario_buscado = ControladorAhorros.buscar_usuario( cedula="1234657" )

        # Comparar si el usuario que se insertó, contiene la misma información, que el retornado
        usuario_buscado.is_equal( usuario_prueba )


    def testInsertAndSelect2( self ):
        """ Prueba que se cree correctamente la tabla en la BD """

        # Insertar un Usuario en la tabla
        usuario_prueba  = Usuario( cedula="5555555", nombre="Otra", apellido="Prueba", correo="otro@tiene.com" )
        ControladorAhorros.insertar_usuario( usuario_prueba )

        # Verificar si la tabla quedo creada correctamente
        usuario_buscado = ControladorAhorros.buscar_usuario( cedula=usuario_prueba.cedula )

        # Comparar si el usuario que se insertó, contiene la misma información, que el retornado
        usuario_buscado.is_equal( usuario_prueba )

    def testPrimaryKey(self):
        # Insertar un Usuario en la tabla
        usuario_prueba  = Usuario( cedula="4444", nombre="Otra", apellido="Prueba", correo="otro@tiene.com" )
        ControladorAhorros.insertar_usuario( usuario_prueba )

        # Insertar un Usuario en la tabla
        usuario_otro  = Usuario( cedula="4444", nombre="Diferente", apellido="Prueba", correo="otro@tiene.com" )
        
        self.assertRaises( Exception, ControladorAhorros.insertar_usuario, usuario_otro )

if __name__ == '__main__':
    unittest.main()