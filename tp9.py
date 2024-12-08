import unittest
from unittest import TestCase

from tp7 import Fraction

class TestFraction(TestCase):

    def test_init(self):

        f = Fraction(1, 2)
        self.assertEqual(f.numerator, 1, "normal numerator test")
        self.assertEqual(f.denominator, 2, "normal denominator test")

        with self.assertRaises(TypeError, msg="num doit etre int"):
            Fraction("1", 2)
        with self.assertRaises(TypeError, msg="den doit etre int"):
            Fraction(1, "2")

        with self.assertRaises(TypeError, msg="num doit etre int"):
            Fraction(1.5, 2)
        with self.assertRaises(TypeError, msg="den doit etre int"):
            Fraction(1, 1.5)


        with self.assertRaises(TypeError, msg="num doit etre int"):
            Fraction(None, 2)
        with self.assertRaises(TypeError, msg="den doit etre int"):
            Fraction(1, None)


        f_neg = Fraction(-1, -2)
        self.assertEqual(f_neg.numerator, 1, "tout negatif")
        self.assertEqual(f_neg.denominator, 2, "tout negatif")

        f_neg = Fraction(-1, 2)
        self.assertEqual(f_neg.numerator, -1, "num negatif")
        self.assertEqual(f_neg.denominator, 2, "den positif")


        with self.assertRaises(ValueError, msg="denominator cannot be zero"):
            Fraction(1, 0)

        with self.assertRaises(TypeError, msg="test none"):
            Fraction(None, None)

    def test_string(self):
        f = Fraction(1, 2)
        self.assertEqual(str(f), "1/2", "Test normal")

        f_neg_num = Fraction(-1, 2)
        self.assertEqual(str(f_neg_num), "-1/2", "Test negative numerator")

        f_neg_den = Fraction(1, -2)
        self.assertEqual(str(f_neg_den), "-1/2", "Test negative denominator")

        f_float = Fraction(1, 5)
        self.assertEqual(str(f_float), "1/5", "Test float version")

        f_int = Fraction(2, 1)
        self.assertEqual(str(f_int), "2", "Test integer version")

    def test_as_mixed(self):
        f = Fraction(7,3)
        self.assertEqual(f.as_mixed_number(), "2 1/3", "Test mixed number normal")

        f = Fraction(4,2)
        self.assertEqual(f.as_mixed_number(), "2", "fraction entière")

        f = Fraction(0, 5)
        self.assertEqual(f.as_mixed_number(), "0", "test à zero")

        f = Fraction(5,1)
        self.assertEqual(f.as_mixed_number(), "5", "dénominateur à 1")

        f = Fraction(-7,3)
        self.assertEqual(f.as_mixed_number(), "-2 1/3", "fraction négatives")



    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5, "Numérateur add")
        self.assertEqual(result.denominator, 6, "Dénominateur add")


        f1 = Fraction(3,4)
        f2 = 1
        result = f1 + f2
        self.assertEqual(result.numerator, 7, "Numérateur add ent")
        self.assertEqual(result.denominator, 4, "Dénominateur add ent")

        f1 = Fraction(0, 2)
        f2 = Fraction(3, 4)
        result = f1 + f2
        self.assertEqual(result.numerator, 3, "Numérateur add zero")
        self.assertEqual(result.denominator, 4, "Dénominateur add zero")

        f1 = Fraction(-1, 4)
        f2 = Fraction(1, 2)
        result = f1 + f2
        self.assertEqual(result.numerator, 1, "Numérateur add neg")
        self.assertEqual(result.denominator, 4, "Dénominateur add neg")

        f1 = Fraction(5, 1)
        f2 = Fraction(3, 4)
        result = f1 + f2
        self.assertEqual(result.numerator, 23, "Numérateur add à un ")
        self.assertEqual(result.denominator, 4, "Dénominateur add à un")

        f1 = Fraction(1, 2)
        result = f1 + (-1)
        self.assertEqual(result.numerator, -1, "Numérateur add ent neg")
        self.assertEqual(result.denominator, 2, "Dénominateur add ent neg")

        f = Fraction(1, 2)
        with self.assertRaises(TypeError, msg="test float"):
            f + 1.2

    def test_div(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 9, "num division ")
        self.assertEqual(result.denominator, 8,"den division")

        result = f1 / 2
        self.assertEqual(result.numerator, 3, "num division ent")
        self.assertEqual(result.denominator, 8, "den division ent")

        f3 = Fraction(-1, 2)
        result = f1 / f3
        self.assertEqual(result.numerator, -3, "num division neg")
        self.assertEqual(result.denominator, 2, "den division neg")

        with self.assertRaises(ValueError, msg="test zero division"):
            result = f1 / 0

        with self.assertRaises(TypeError, msg="test string"):
            result = f1 / "string"

        with self.assertRaises(TypeError, msg="test float"):
            result = f1 / 1.2

    def test_sub(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        result = f1 - f2
        self.assertEqual(result.numerator, 1, "Numérateur sub normal")
        self.assertEqual(result.denominator, 2, "Dénominateur sub normal")

        f3 = Fraction(-1, 3)
        result = f1 - f3
        self.assertEqual(result.numerator, 13, "Numérateur sub neg")
        self.assertEqual(result.denominator, 12, "Dénominateur sub neg ")

        f4 = Fraction(-2, 3)
        result = f4 - f2
        self.assertEqual(result.numerator, -11, "Numérateur sub neg to pos")
        self.assertEqual(result.denominator, 12, "Dénominateur sub neg to pos")

        result = f4 - f3
        self.assertEqual(result.numerator, -1, "Numérateur sub neg neg")
        self.assertEqual(result.denominator, 3, "Dénominateur sub neg neg")

        result = f1 - 1
        self.assertEqual(result.numerator, -1, "Numérateur sub ent")
        self.assertEqual(result.denominator, 4, "Dénominateur sub ent")

        result = f1 - 0
        self.assertEqual(result.numerator, 3, "Numérateur sub 0")
        self.assertEqual(result.denominator, 4, "Dénominateur sub 0")

        result = f1 - f1
        self.assertEqual(result.numerator, 0, "Numérateur sub res null")
        self.assertEqual(result.denominator, 1, "Dénominateur sub res null")


        with self.assertRaises(TypeError, msg="test float sub"):
            f1 + 1.2

    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2,"égalité normale simplification")

        f3 = Fraction(1, 3)
        self.assertFalse(f1 == f3,"pas d'égalité")

        f4 = Fraction(4, 2)
        self.assertTrue(f4 == 2,"égalité avec un entier")

        f5 = Fraction(-3, 1)
        self.assertTrue(f5 == -3,"égalité avec entier négatif")

        f6 = Fraction(0, 1)
        self.assertTrue(f6 == 0,"égalité à 0")

        f7 = Fraction(1, 2)
        self.assertFalse(f7 == 0,"pas d'égalité à 0")

        f8 = Fraction(-1, 2)
        f9 = Fraction(1, -2)
        self.assertTrue(f8 == f9,"égalité signe")
        self.assertFalse(f8 == f1,"pas d'égalité signe")

        self.assertFalse(f1 == "1/2","pas d'égalité avec une string ")
        self.assertTrue(f1 == 0.5,"peut etre égale à un float")


    def test_is_integer(self):
        f = Fraction(4, 2)
        self.assertTrue(f.is_integer(),"fraction entiere")

        f = Fraction(3, 2)
        self.assertFalse(f.is_integer(), "fraction non entiere")

        f = Fraction(0, 5)
        self.assertTrue(f.is_integer(), "fraction num null")

        f = Fraction(-4, 2)
        self.assertTrue(f.is_integer(), "fraction négative entiere")

        f = Fraction(-3, 2)
        self.assertFalse(f.is_integer(), "fraction négative non entière")

        f = Fraction(5,1)
        self.assertTrue(f.is_integer(), "fraction entière den à un")



    def test_is_proper(self):
        f1 = Fraction(1,2)
        self.assertTrue(f1.is_proper(),"fraction propre")

        f2 = Fraction(-1,2)
        self.assertTrue(f2.is_proper(),"fraction propre négative")

        f3 = Fraction(1,1)
        self.assertFalse(f3.is_proper(), "fraction égale à un ")

        f4 = Fraction(-1,1)
        self.assertFalse( f4.is_proper(), "fraction égale à -1")

        f5 = Fraction(3,2)
        self.assertFalse(f5.is_proper(), "fraction impropre")

        f6 = Fraction(-3,2)
        self.assertFalse(f6.is_proper(), "fraction impropre négative")

        f7 = Fraction(0,5)
        self.assertTrue(f7.is_proper(), "fraction propre à 0")

        f8 = Fraction(-1,-2)
        self.assertTrue(f8.is_proper(), "fraction propre à termes neg")

    def test_is_adjacent(self):

        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1.is_adjacent_to(f2),"adjacentes")

        f3 = Fraction(-1, 2)
        f4 = Fraction(-1, 3)
        self.assertTrue(f3.is_adjacent_to(f4),"adjacentes négatives")

        f5 = Fraction(1, 2)
        f6 = Fraction(1, 4)
        self.assertFalse(f5.is_adjacent_to(f6),"non adjacentes")

        f7 = Fraction(1, 1)
        f8 = Fraction(2, 3)
        self.assertTrue(f7.is_adjacent_to(f8),"adjacentes avec entier frac")

        f9 = Fraction(1, 1)
        f10 = Fraction(2,1)
        self.assertFalse(f9.is_adjacent_to(f10),"non adjacentes avec entier frac")

        with self.assertRaises(TypeError):
            f1.is_adjacent_to("not a fraction")

if __name__ == "__main__":
    unittest.main()