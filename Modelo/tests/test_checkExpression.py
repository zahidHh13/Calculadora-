import unittest
from Modelo.stack import Stack
from Modelo.parentesis import is_correct_parenthesis  # Asegúrate de que el nombre del archivo sea correcto

class TestCheckExpression(unittest.TestCase):
    def test_valid_expressions(self):
        # Casos donde la expresión es válida
        self.assertTrue(is_correct_parenthesis("()"))
        self.assertTrue(is_correct_parenthesis("([])"))
        self.assertTrue(is_correct_parenthesis("({[]})"))
        self.assertTrue(is_correct_parenthesis("(5+3)*[2+3]"))
        self.assertTrue(is_correct_parenthesis("{[()]()}"))

    def test_invalid_expressions(self):
        # Casos donde la expresión es inválida
        self.assertFalse(is_correct_parenthesis("("))
        self.assertFalse(is_correct_parenthesis(")"))
        self.assertFalse(is_correct_parenthesis("([)]"))
        self.assertFalse(is_correct_parenthesis("((()))]"))
        self.assertFalse(is_correct_parenthesis("{[}]"))
        
if __name__ == '__main__':
    unittest.main()
