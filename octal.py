from decimal import decimal2binario
from binary import binario2hexadecimal

def octal2binario(octal):
    result = ''
    for i in range(len(octal)):
        digit = decimal2binario( int( octal[-(i + 1)] ) )
        
        while len(digit) < 3:
            digit = '0' + digit
        
        result = digit + result
    
    while result[0] == '0':
        result = result[1:]
    
    return result

def octal2decimal(octal):
    result = 0
    
    for i in range(len(octal)):
        result += int(octal[-(i + 1)]) * (8 ** i)
    
    return result

def octal2hexadecimal(octal):
    binary = octal2binario(octal)
    return binario2hexadecimal(binary)

if __name__ == '__main__':
    pass