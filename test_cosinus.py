import unittest
from math import cos
from cosinus import cosinus

class testCosinusFunction(unittest.TestCase):

    def test_types(self):
        self.assertRaises(TypeError, cosinus, 'value')
        self.assertRaises(TypeError, cosinus, 2 + 5j)
        self.assertRaises(TypeError, cosinus, True)

    def test_equal(self):
        self.assertEqual(cosinus(90), 0)