import unittest
from calculator import Calculator

class TestCalculator (unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_initial_version(self):
        self.assertEqual(self.calc.value,0)

    def add_metod (self): 
        self.calc.add(1,3)
        self.assertEqual(self.calc.value,4)
