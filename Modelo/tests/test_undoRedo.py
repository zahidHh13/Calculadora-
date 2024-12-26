# Lab_8: Introducción a las pruebas unitarias 

#Testea si la secuencia es correspondiente a una igualda predefinida
import unittest
from Modelo.UndoRedo import UndoRedo

class TestUndoRedo(unittest.TestCase):
    def setUp(self):
        self.ur = UndoRedo()

    # def test_expression_simple(self):
    #     # Secuencia: {4 + 5} undo redo
    #     #{4+(5+6)-3*5 undo undo ^4}-5*9 undo undo redo 10 
    #     ops = ["{", "4", "+", "(", "5","+","6",")","-","3","*","5","UNDO","UNDO","^","4","}","-","5","*","9","UNDO","UNDO","REDO","10"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "{4+(5+6)-3^4}-5*10")

    # def test_expression_with_undo(self):
    #     # Secuencia: {4 + (5 - 6)} undo undo redo
    #     ops = ["4", "+", "(", "5", "-", "6", ")", "UNDO", "UNDO", "REDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "4+(")

    # def test_complex_expression_with_undo_redo(self):
    #     # Secuencia: {4+(5+6)-3*5 undo undo ^4}-5*9 undo undo redo 10
    #     ops = ["4", "+", "(", "5", "+", "6", ")", "-", "3", "*", "5", "UNDO", "UNDO", "^", "4", ")", "-", "5", "*", "9", "UNDO", "UNDO", "REDO", "10"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "4+(5+6)^4)-5*10")

    # def test_expression_with_multiple_undo(self):
    #     # Secuencia: {8 + 3 * 5 undo undo undo redo redo}
    #     ops = ["8", "+", "3", "*", "5", "UNDO", "UNDO", "UNDO", "REDO", "REDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "8+3*")

    # def test_expression_with_nested_undo_redo(self):
    #     # Secuencia: {12 * (4 - 2) undo undo redo undo}
    #     ops = ["12", "*", "(", "4", "-", "2", ")", "UNDO", "UNDO", "REDO", "UNDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "12*(")

    # def test_expression_with_partial_undo(self):
    #     # Secuencia: {7 * (3 + 2 undo} redo + 5 undo}
    #     ops = ["7", "*", "(", "3", "+", "2", "UNDO", ")", "REDO", "+", "5", "UNDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "7*(3+5")

    # def test_mixed_operations(self):
    #     # Secuencia: {15 / 3 undo * 9 redo undo - 5 undo}
    #     ops = ["15", "/", "3", "UNDO", "*", "9", "REDO", "UNDO", "-", "5", "UNDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "15*")

    # def test_long_expression_with_undo_redo(self):
    #     # Secuencia: {100 - 45 + (20 / 4 undo undo redo redo * 6 undo undo)}
    #     ops = ["100", "-", "45", "+", "(", "20", "/", "4", "UNDO", "UNDO", "REDO", "REDO", "*", "6", "UNDO", "UNDO", ")"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "100-45+(20")

    # def test_expression_with_full_undo(self):
    #     # Secuencia: {4 + 5 - 3 * 7 undo undo undo undo undo}
    #     ops = ["4", "+", "5", "-", "3", "*", "7", "UNDO", "UNDO", "UNDO", "UNDO", "UNDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "")

    # def test_expression_with_full_redo(self):
    #     # Secuencia: {6 + 2 undo undo redo redo}
    #     ops = ["6", "+", "2", "UNDO", "UNDO", "REDO", "REDO"]
    #     self.ur.simulate(ops)
    #     self.assertEqual(self.ur.show(), "6+2")
    
    def test_simple_undo_redo(self):
        # Secuencia: a b UNDO c REDO
        ops = ["a", "b", "UNDO", "c", "REDO"]
        self.ur.simulate(ops)
        self.assertEqual(self.ur.show(), "ac")

if __name__ == "__main__":
    unittest.main()
