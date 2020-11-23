import unittest 
from reciprocal import reciprocal

class testReciprocalFunction(unittest.TestCase):

    def test_types(self):
        self.assertRaises(TypeError, reciprocal, 'value')
        self.assertRaises(TypeError, reciprocal, 2 + 5j)
        self.assertRaises(TypeError, reciprocal, True)
    
    def test_values(self):
        self.assertRaises(ValueError, reciprocal, 0)
        