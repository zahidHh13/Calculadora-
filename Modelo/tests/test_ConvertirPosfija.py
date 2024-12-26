import unittest
from Modelo.evaluacionPost import EvalPost  # Asegúrate de tener el nombre correcto del archivo

class TestEvalPost(unittest.TestCase):
    def setUp(self):
        self.evaluator = EvalPost()

    def test_addition(self):
        self.assertEqual(self.evaluator.evalPostfija("20 3 + 5 30 10 -  +  + "), 48)
    
    def test_subtraction(self):
        self.assertEqual(self.evaluator.evalPostfija("25 3.50 + 50 2 15 + - + 40 50 - 25 15 - - - "), 81.5)

    def test_multiplication(self):
        self.assertEqual(self.evaluator.evalPostfija("6 7 *"), 42)
    
    def test_division(self):
        self.assertEqual(self.evaluator.evalPostfija("8 2 /"), 4)
    
    def test_power(self):
        self.assertEqual(self.evaluator.evalPostfija("2 3 **"), 8)

    def test_sqrt(self):
        self.assertEqual(self.evaluator.evalPostfija("9 sqrt"), 3)

    def test_combined_expression(self):
        self.assertEqual(self.evaluator.evalPostfija("3 4 + 2 *"), 14)
    
    def test_complex_expression(self):
        self.assertEqual(self.evaluator.evalPostfija("5 1 2 + 4 * + 3 -"), 14)

    def test_single_value(self):
        self.assertEqual(self.evaluator.evalPostfija("42"), 42)

    def test_decimal_numbers(self):
        self.assertEqual(self.evaluator.evalPostfija("5.5 4.5 +"), 10)

if __name__ == '__main__':
    unittest.main()
