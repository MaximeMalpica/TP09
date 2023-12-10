from main import Fraction
import unittest

class TestUnitaire(unittest.TestCase):

    def test_den_is_zero_error(self):
        """Test si ZeroDivisionError est raises"""
        with self.assertRaises(ZeroDivisionError) as zero_error:
            Fraction(1, 0)
        self.assertEqual(zero_error.exception.args[0], "Le dénominateur de la fraction ne peut pas être 0")

    def test_type_error(self):
        """Test si TypeError est raises"""
        with self.assertRaises(TypeError) as type_error:
            print(Fraction(2, 4) ** 'random')
        self.assertEqual(type_error.exception.args[0], 'Doit être un nombre entier')

    def test_declaration(self):
        """Test la déclaration de la fraction"""
        fraction1 = Fraction(1, 2)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
    
    
if __name__ == '__main__':
    unittest.main()