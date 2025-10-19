
import unittest
import sys

sys.path.append("src")
from model import modulos

class TestAhorroMensual(unittest.TestCase):
    redondeo_cifras_decimales = 2

    def test_normal_1(self):
        meta = 1_200_000
        meses = 12
        abono_extra = 0
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)
        ahorro_mensual_esperado = 100_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_normal_2(self):
        meta = 2_400_000
        meses = 24
        abono_extra = 0
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)
        ahorro_mensual_esperado = 100_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_normal_3(self):
        meta = 600_000
        meses = 6
        abono_extra = 0
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)
        ahorro_mensual_esperado = 100_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_normal_4(self):
        meta = 3_000_000
        meses = 15
        abono_extra = 0
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)
        ahorro_mensual_esperado = 200_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_extraordinario_1(self):
        meta = 1_000_000
        meses = 10
        abono_extra = 200_000
        interes = 0.01
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, interes)
        ahorro_mensual_esperado = 74_465.66
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_extraordinario_2(self):
        meta = 2_000_000
        meses = 20
        abono_extra = 300_000
        interes = 0.01
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, interes)
        ahorro_mensual_esperado = 74_206.035
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_extraordinario_3(self):
        meta = 900_000
        meses = 9
        abono_extra = 400_000
        interes = 0.01
        ahorro_mensual = modulos.calcular_ahorro_mensual(meta, meses, abono_extra, interes)
        ahorro_mensual_esperado = 49_370.18
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    def test_error_meta_negativa(self):
        meta = -500_000
        meses = 5
        abono_extra = 0
        with self.assertRaises(modulos.ErrorValorMeta):
            modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)

    def test_error_meses_cero(self):
        meta = 1_000_000
        meses = 0
        abono_extra = 0
        with self.assertRaises(modulos.ErrorValorMeses):
            modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)

    def test_error_meta_superada(self):
        meta = 1_500_000
        meses = 12
        abono_extra = 2_000_000
        with self.assertRaises(modulos.ErrorAbonoExcesivo):
            modulos.calcular_ahorro_mensual(meta, meses, abono_extra, 0)

if __name__ == '__main__':
    unittest.main()
