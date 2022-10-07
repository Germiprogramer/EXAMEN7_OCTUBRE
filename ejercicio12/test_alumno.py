#CREACION ALUMNOS

import unittest
from classes.alumno import Alumno

class Test(unittest.TestCase):
    def test_creacion(self):
        carlos = Alumno("Carlos", 10)
        german = Alumno("Germi", 0)
        self.assertIsNotNone(carlos)
        self.assertIsNotNone(german)

    def calificacion(self):
        carlos = Alumno("Carlos", 10)
        self.assertEqual(carlos.calificacion,"aprobado")

    def str(self):
        carlos = Alumno("Carlos", 10)
        self.assertEqual(carlos, "Carlos", 10)

if __name__ == '__main__':
    unittest.main()
