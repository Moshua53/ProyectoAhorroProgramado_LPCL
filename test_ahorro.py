import unittest
import Modulos

class Test_ahorro_Mensual(unittest.TestCase):

    def test_normal_1(self):
        # Entradas
        meta = 1_200_000
        meses = 12
        abonos_extra = 0

        # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)

        # Salidas
        ahorro_mensual_esperado = 100_000

        #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)


if __name__ == '__main__':
    unittest.main()


