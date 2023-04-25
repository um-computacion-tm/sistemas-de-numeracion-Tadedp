import unittest
from binary import binario2octal, binario2decimal, binario2hexadecimal
from octal import octal2binario, octal2decimal, octal2hexadecimal
from decimal import decimal2binario, decimal2octal, decimal2hexadecimal
from hexadecimal import hexadecimal2binario, hexadecimal2octal, hexadecimal2decimal

class TestNumeracion(unittest.TestCase):
    def test_binario2octal(self) :
        self.assertEqual(binario2octal('1011111010101'), '13725')
    
    def test_binario2octal2(self):
        self.assertEqual(binario2octal('011101001110101'), '35165')
    
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'), 92)
        
    def test_binario2decimal2(self):
        self.assertEqual(binario2decimal('01100001'), 97)
    
    def test_binario2hexadecimal(self):
        self.assertEqual(binario2hexadecimal('11101100101001'), '3B29')
    
    def test_binario2hexadecimal2(self):
        self.assertEqual(binario2hexadecimal('1001110100011010'), '9D1A')
    
    def test_octal2binario(self):
        self.assertEqual(octal2binario('255363'), '10101101011110011')
    
    def test_octal2binario2(self):
        self.assertEqual(octal2binario('123334'), '1010011011011100')
    
    def test_octal2decimal(self):
        self.assertEqual(octal2decimal('1332'), 730)
    
    def test_octal2decimal2(self):
        self.assertEqual(octal2decimal('263'), 179)
    
    def test_octal2hexadecimal(self):
        self.assertEqual(octal2hexadecimal('13725'), '17D5')
        
    def test_octal2hexadecimal2(self):
        self.assertEqual(octal2hexadecimal('7654'), 'FAC')
    
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97), '1100001')
    
    def test_decimal2binario2(self):
        self.assertEqual(decimal2binario(92), '1011100')
    
    def test_decimal2octal(self):
        self.assertEqual(decimal2octal(730), '1332')
    
    def test_decimal2octal2(self):
        self.assertEqual(decimal2octal(179), '263')
        
    def test_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(500), '1F4')
        
    def test_decimal2hexadecimal2(self):
        self.assertEqual(decimal2hexadecimal(8372283), '7FC03B')

    def test_hexadecimal2binario(self):
        self.assertEqual(hexadecimal2binario('A6DC'), '1010011011011100')
    
    def test_hexadecimal2binario2(self):
        self.assertEqual(hexadecimal2binario('15AF3'), '10101101011110011')
        
    def test_hexadecimal2octal(self):
        self.assertEqual(hexadecimal2octal('17A'), '572')
    
    def test_hexadecimal2octal2(self):
        self.assertEqual(hexadecimal2octal('CD5'), '6325')   

    def test_hexadecimal2decimal(self):
        self.assertEqual(hexadecimal2decimal('7FC03B'), 8372283)
    
    def test_hexadecimal2decimal2(self):
        self.assertEqual(hexadecimal2decimal('1F4'), 500)

if __name__ == '__main__':
    unittest.main()