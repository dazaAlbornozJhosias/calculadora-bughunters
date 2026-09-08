"""
Responsable: Art (Git Leader) - Integrante 10
Tests unitarios básicos para cada operación.
Cada integrante puede agregar más casos a su propia función de test.
"""
import unittest
from suma import suma, suma_lista
from resta import resta, resta_negativos
from multiplicacion import multiplicacion, multiplicacion_lista
from division import division, division_entera
from potencia import potencia, potencia_negativa
from raiz import raiz_cuadrada, raiz_n
from modulo import modulo, modulo_negativos
from porcentaje import porcentaje, variacion_porcentual


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma_lista([1, 2, 3]), 6)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta_negativos(-5, -3), -2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)
        self.assertEqual(multiplicacion_lista([1, 2, 3, 4]), 24)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia_negativa(2, -1), 0.5)

    def test_raiz(self):
        self.assertEqual(raiz_cuadrada(9), 3)
        with self.assertRaises(ValueError):
            raiz_cuadrada(-4)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

    def test_porcentaje(self):
        self.assertEqual(porcentaje(200, 10), 20)
        self.assertEqual(variacion_porcentual(100, 150), 50)


if __name__ == "__main__":
    unittest.main()
