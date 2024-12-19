import unittest
from main import Math
from func import Func

class CosineX(unittest.TestCase):
    def test_true_cosine(self):
        self.assertEqual(Math.cosine(0), 1)

    def test_negative_true(self):
        self.assertEqual(Math.cosine(-60), 0.5)

    def test_positive_true(self):
        self.assertEqual(Math.cosine(60), 0.5)

    def test_error(self):
        with self.assertRaises(TypeError): 
            Math.cosine('avd')

class SineX(unittest.TestCase):
    def test_true_sine(self):
        self.assertEqual(Math.sine(0), 0)

    def test_negative_true(self):
        self.assertEqual(Math.sine(-90), -1)

    def test_positive_true(self):
        self.assertEqual(Math.sine(90), 1)

    def test_error(self):
        with self.assertRaises(TypeError): 
            Math.sine('avd')

class naturalLogX(unittest.TestCase):
    def test_true_ln(self):
        self.assertEqual(Math.natural_log(1), 0)

    def test_typeerror(self):
        with self.assertRaises(TypeError): 
            Math.natural_log('w')

    def test_exception(self):
        with self.assertRaises(Exception): 
            Math.natural_log(-943939934)

    def test_true_natural_log(self):
        self.assertEqual(Math.natural_log(2), 0.7)

class modulX(unittest.TestCase):
    def test_typeerror(self):
        with self.assertRaises(TypeError): 
            Math.modul('avd')

    def test_positive_modul(self):
        self.assertEqual(Math.modul(2), 2)

    def test_negative_modul(self):
        self.assertEqual(Math.modul(-2), 2)

class func(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(Func(1), 0)

    def test_negative(self):
        self.assertEqual(Func(-20), 0.3)