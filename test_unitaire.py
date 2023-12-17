from main import Fraction
import unittest
import coverage

class TestUnitaire(unittest.TestCase):

    def test_den_is_zero_error(self):
        """Test si ZeroDivisionError est raises"""
        with self.assertRaises(ZeroDivisionError) as zero_error:
            Fraction(1, 0)
        self.assertEqual(zero_error.exception.args[0], "Le dénominateur de la fraction ne peut pas être 0")
        with self.assertRaises(ZeroDivisionError) as zero_error:
            Fraction(30, 0)
        self.assertEqual(zero_error.exception.args[0], "Le dénominateur de la fraction ne peut pas être 0")

    def test_type_error(self):
        """Test si TypeError est raises"""
        with self.assertRaises(TypeError) as type_error:
            print(Fraction(2,12) ** "test")
        self.assertEqual(type_error.exception.args[0], 'Doit être un nombre entier')
        with self.assertRaises(TypeError) as type_error:
            print(Fraction(2,1) ** 3.3)
        self.assertEqual(type_error.exception.args[0], 'Doit être un nombre entier')

    def test_declaration(self):
        """Test la déclaration de la F raction"""
        fraction1 = Fraction(1, 2)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
        fraction2 = Fraction(-10, 3)
        self.assertEqual(fraction2.numerator, -10)
        self.assertEqual(fraction2.denominator, 3)
    
    def test_str(self):
        """Test la representation textuelle de la Fraction"""
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(13, 2)), "13/2")

    def test_mixed_number(self):
        """Test la représentation d'une fraction en nombres mixtes"""
        self.assertEqual(Fraction(1, 4).as_mixed_number(), "0 + 1/4")
        self.assertEqual(Fraction(5, 7).as_mixed_number(), "0 + 5/7")

    def test_add(self):
        """Test de l'opération d'addition sur une fraction"""
        self.assertEqual(str(Fraction(3, 3) + Fraction(3, 3)), "2/1")
        self.assertEqual(str(Fraction(1, 2) + Fraction(3, 4)), "5/4")
    
    def test_sub(self):
        """Test de l'opération de soustraction sur une fraction"""
        self.assertEqual(str(Fraction(4, 4) - Fraction(3, 4)), "1/4")   

    def test_mul(self):
        """Test de l'opération de multiplication sur Fraction"""
        self.assertEqual(str(Fraction(3, 2) * Fraction(3, 2)), "9/4")
        self.assertEqual(str(Fraction(1, 2) * Fraction(3, 4)), "3/8")

    def test_div(self):
        """Test de l'opération de division sur Fraction"""
        self.assertEqual(str(Fraction(8, 4) / Fraction(2, 2)), "2/1")
        self.assertEqual(Fraction(1, 2) / Fraction(3, 4), Fraction(2, 3))

    def test_pow(self):
        """Test de l'opération de puissancce sur Fraction"""
        self.assertEqual(str(Fraction(1, 2) ** 1), "1/2")
        self.assertEqual(str(Fraction(1, 2) ** 2), "1/4")
    
    def test_eq(self):
        """Test == opération sur Fraction"""
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertTrue(Fraction(3, 3) == Fraction(3, 3))

    def test_float(self):
        """Test de conversion d'une fraction en float"""
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(1, 4)), 0.25)

    def test_zero(self):
        """Test si Fraction == 0"""
        self.assertTrue(Fraction(0, 20).is_zero())
        self.assertFalse(Fraction(4, 4).is_zero())
    
    def test_int(self):
        """Teste si la valeur de la fraction est un int"""
        self.assertTrue(Fraction(5).is_integer())
        self.assertFalse(Fraction(4, 5).is_integer()) 

    def test_proper(self):
        """Teste si la valeur absolue d'une fraction est < 1"""
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_unit(self):
        """Test si le numérateur de la fraction == 1"""
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 9).is_unit())    

    def test_adjacent(self):
        """Test if the difference between two Fraction is a unit"""
        #self.assertFalse(Fraction(4, 3).is_adjacent_to(2))

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    cov.stop()
    cov.report()