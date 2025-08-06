import unittest
import Modulos

class Test_ahorro_Mensual(unittest.TestCase):

# caso normal 1
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

# caso normal 2
    def test_normal_2(self):
        
    # Entradas
        meta = 2_400_000
        meses = 24
        abonos_extra = 0
    # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)
    # Salidas
        ahorro_mensual_esperado = 100_000
    #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)

# caso normal 3
    def test_normal_3(self):
        
    # Entradas
        meta = 600_000
        meses = 6
        abonos_extra = 0
    # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)
    # Salidas
        ahorro_mensual_esperado = 100_000
    #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)

# caso normal 4
    def test_normal_4(self):
        
    # Entradas
        meta = 3_000_000
        meses = 15
        abonos_extra = 0
    # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)
    # Salidas
        ahorro_mensual_esperado = 200_000
    #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)

# caso extraordinario 1
    def prueba_caso_extraordinario_1():
        
    # Entradas
        meta = 1_000_000
        meses = 10
        abonos_extra = 200_000
    # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)
    # Salidas
        ahorro_mensual_esperado = 300_000
    #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)

# caso extraordinario 2
    def prueba_caso_extraordinario_2():
        
    # Entradas
        meta = 2_000_000
        meses = 20
        abonos_extra = 300_000
    # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)
    # Salidas
        ahorro_mensual_esperado = 400_000
    #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)

# caso extraordinario 3
    def prueba_caso_extraordinario_3():
        
    # Entradas
        meta = 900_000
        meses = 9
        abonos_extra = 400_000
    # Probar salidas
        ahorro_mensual = Modulos.calcular_ahorro_mesual(meta, meses, abonos_extra)
    # Salidas
        ahorro_mensual_esperado = 500_000
    #Prueba
        self.assertAlmostEqual(ahorro_mensual_esperado,ahorro_mensual, 2)

if __name__ == '__main__':
    unittest.main()
