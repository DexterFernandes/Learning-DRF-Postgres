from django.test import TestCase

from app.calc import add, multiply, subtract

class CalcTests(TestCase):
    
    def test_add_numbers(self):
        """Should return the correct sum of two numbers"""
        self.assertEqual(add(9, 12), 21)

    def test_multiply_numbers(self):
        """Should return the correct product of three numbers"""
        self.assertEqual(multiply(12, 13, 14), 2184)
    
    def test_subtract_numbers(self):
        """Should return the correct subtraction between four numbers"""
        self.assertEqual(subtract(8, 4, 11, -14), 7)