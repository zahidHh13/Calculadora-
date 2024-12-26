from Modelo.funciones import calcula_media 
from Modelo.funciones import al_cubo
from Modelo.funciones import es_par
from Modelo.funciones import decir_hola

import unittest 

class TestFunciones(unittest.TestCase):
    def test_calcula_media(self):
        resultado = calcula_media([10, 10 ,10])
        self.assertEqual(resultado,10)

        self.assertEqual(calcula_media([5,3,4]),4)
        self.assertEqual(calcula_media([6,8,4]),6)
        self.assertEqual(calcula_media([2,8,5]),5)
    
    def test_al_cubo(self):
        self.assertEqual(al_cubo(2),8)
        self.assertEqual(al_cubo(-2),-8)
        self.assertNotEqual(al_cubo(2),4)
        self.assertNotEqual(al_cubo(-3),27)
    
    def test_es_par(self):
        self.assertFalse(es_par(5))
        self.assertTrue(es_par(2))
        self.assertTrue(es_par(8))
        self.assertFalse(es_par(7))
        self.assertFalse(es_par(13))
        self.assertTrue(es_par(72))
        
    def test_decir_hola(self):
        self.assertEqual(decir_hola("Pedro"), "Hola Pedro")
        self.assertEqual(decir_hola("Juan"), "Hola Juan")  
        self.assertNotEqual(decir_hola("Carlos"), "Hola Carlo")  
        self.assertNotEqual(decir_hola("Ruben"), "Hola Rube")  

if __name__ == "__main__":
    unittest.main()
