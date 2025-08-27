import unittest
import sys

sys.path.append("src")
from src.model import Modulos

class TestAhorroMensual(unittest.TestCase):
    redondeo_cifras_decimales = 2   # ← corregido

    # caso normal 1
    def test_normal_1(self):
        meta = 1_200_000
        meses = 12
        abono_extra = 0
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 100_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    # caso normal 2
    def test_normal_2(self):
        meta = 2_400_000
        meses = 24
        abono_extra = 0
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 100_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    # caso normal 3
    def test_normal_3(self):
        meta = 600_000
        meses = 6
        abono_extra = 0
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 100_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    # caso normal 4
    def test_normal_4(self):
        meta = 3_000_000
        meses = 15
        abono_extra = 0
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 200_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    # caso extraordinario 1
    def test_caso_extraordinario_1(self):
        meta = 1_000_000
        meses = 10
        abono_extra = 200_000
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 80_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    # caso extraordinario 2
    def test_caso_extraordinario_2(self):
        meta = 2_000_000
        meses = 20
        abono_extra = 300_000
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 85_000
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, self.redondeo_cifras_decimales)

    # caso extraordinario 3
    def test_caso_extraordinario_3(self):
        meta = 900_000
        meses = 9
        abono_extra = 400_000
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)
        ahorro_mensual_esperado = 55_556
        self.assertAlmostEqual(ahorro_mensual_esperado, ahorro_mensual, 0)

    # caso error 1: meta negativa
    def test_error_meta_negativa(self):
        meta = -500_000
        meses = 5
        abono_extra = 0
        with self.assertRaises(Modulos.ErrorValorMeta):
            Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)

    # caso error 2: meses igual a cero
    def test_error_meses_cero(self):
        meta = 1_000_000
        meses = 0
        abono_extra = 0
        with self.assertRaises(Modulos.ErrorValorMeses):
            Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)

    # caso error 3: meta ya superada
    def test_error_meta_superada(self):
        meta = 1_500_000
        meses = 12
        abono_extra = 2_000_000
        with self.assertRaises(Modulos.ErrorAbonoExcesivo):
            Modulos.calcular_ahorro_mesual(meta, meses, abono_extra)


if __name__ == '__main__':
    unittest.main()
