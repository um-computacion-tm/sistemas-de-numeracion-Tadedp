import unittest
from binary2decimal import binario2decimal
from decimal2binary import decimal2binario

class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'), 92)
    
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')
        
if __name__ == '__main__':
    unittest.main()