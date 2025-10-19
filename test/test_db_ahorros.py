import unittest
import sys
sys.path.append("src")

from src.model.ahorro import Ahorro
from src.Controller.ahorro_controller import ControladorAhorros


class TestAhorro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Test Fixtures que se ejecuta al inicio de las pruebas solamente """
        controller = ControladorAhorros
        controller.eliminar_tabla()
        controller.crear_tabla()

    def test_insert_1(self):
        # Crear un ahorro
        ahorro = Ahorro(
            cedula="1010101010",
            meta=1200000,
            meses=12,
            ahorro_mensual=100000,
            objetivo="Comprar una moto",
            abonos_extras=0,
            mes_abono_extra=0,
            interes=0.0
        )

        # Guardarlo en la BD
        ControladorAhorros.insertar(ahorro)

        # Buscarlo
        ahorro_buscado = ControladorAhorros.buscar_id(ahorro.id_ahorro)

        # Verificar si lo trajo bien
        self.assertTrue(ahorro_buscado.is_equal(ahorro))

    def test_insert_2(self):
        # Crear otro ahorro
        ahorro = Ahorro(
            cedula="1111111111",
            meta=3000000,
            meses=15,
            ahorro_mensual=200000,
            objetivo="Viaje a México",
            abonos_extras=500000,
            mes_abono_extra=6,
            interes=0.8
        )

        # Guardarlo en la BD
        ControladorAhorros.insertar(ahorro)

        # Buscarlo
        ahorro_buscado = ControladorAhorros.buscar_id(ahorro.id_ahorro)

        # Verificar si lo trajo bien
        self.assertTrue(ahorro_buscado.is_equal(ahorro))


if __name__ == '__main__':
    unittest.main()
