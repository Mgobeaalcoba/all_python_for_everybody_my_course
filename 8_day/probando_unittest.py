import unittest
import mimodulo

class NombrePrueba(unittest.TestCase):
    def test_prueba(self):
        primer_valor = 4
        segundo_valor = mimodulo.suma(2,2)
        self.assertEqual(primer_valor, segundo_valor, "Ambos valores son iguales")

if __name__ == '__main__':
    unittest.main()

# Ejecuto el file con python probando_unittest.py

"""
Output de falla del test: 

C:\Users\mgobea\Documents\develop\python_total\8_day(main -> origin)
(venv) λ python probando_unittest.py
F
======================================================================
FAIL: test_prueba (__main__.NombrePrueba.test_prueba)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\mgobea\Documents\develop\python_total\8_day\probando_unittest.py", line 8, in test_prueba
    self.assertEqual(primer_valor, segundo_valor, "Ambos valores son iguales")
AssertionError: 4 != 5 : Ambos valores son iguales

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

Output de acierto del test: 

C:\Users\mgobea\Documents\develop\python_total\8_day(main -> origin)
(venv) λ python probando_unittest.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

"""