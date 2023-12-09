"""Module to use math operations"""
import math

class Fraction:
    """Class representing a fraction and operations on it

    Author : M. Malpica Arana
    Date : 09/12/2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """Initialize a Fraction object with a numerator and denominator.

        PRE :
        - num : un int qui représente le numérateur d'une fraction
        - den : un int qui représente le dénominateur d'une fraction
        POST :
        - numerator : le numérateur réduit d'une fraction
        - denominator : le dénominateur réduit positif d'une fraction
        RAISES : ZeroDivisionError si den égal 0
        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur de la fraction ne peut pas être 0")

        abs_num = abs(num)
        if num / den < 0:
            num = -abs_num
        else:
            num = abs_num

        common_divisor = math.gcd(num, den)
        self.__numerator = num // common_divisor
        self.__denominator = abs(den) // common_divisor

    @property
    def numerator(self):
        """This gets the value of numerator.

        POST : Renvoie la valeur du numérateur.
        """
        return self.__numerator

    @property
    def denominator(self):
        """This gets the value of denominator.

        POST : Renvoie la valeur du dénominateur.
        """
        return self.__denominator

    @staticmethod
    def is_fraction(num: int):
        """A function to set a value to Fraction

        PRE : Une valeur numérique.
        POST : Renvoie la fraction de la valeur.
        RAISES : ValueError si num n'est pas un int ou une fraction
        """

        if isinstance(num, int):
            num = Fraction(num)
        if not isinstance(num, Fraction):
            raise ValueError("Doit être un int ou une fraction")
        return num
