from decimal import decimal2binario
from binary import binario2octal

def hexadecimal2binario(hexadecimal):
    result = ''
    for i in range(len(hexadecimal)):
        digit = hexadecimal[-(i + 1)]
        
        if digit == 'A':
            digit = 10
        elif digit == 'B':
            digit = 11
        elif digit == 'C':
            digit = 12
        elif digit == 'D':
            digit = 13
        elif digit == 'E':
            digit = 14
        elif digit == 'F':
            digit = 15    
        digit = decimal2binario(int(digit))
        
        while len(digit) < 4:
            digit = '0' + digit  
        result = digit + result
    
    while result[0] == '0':
        result = result[1:]
    
    return result

def hexadecimal2octal(hexadecimal):
    binary = hexadecimal2binario(hexadecimal)
    return binario2octal(binary)

def hexadecimal2decimal(hexadecimal):
    result = 0
    for i in range(len(hexadecimal)):
        digit = hexadecimal[-(i + 1)]
        
        if digit == 'A':
            digit = 10
        elif digit == 'B':
            digit = 11
        elif digit == 'C':
            digit = 12
        elif digit == 'D':
            digit = 13
        elif digit == 'E':
            digit = 14
        elif digit == 'F':
            digit = 15
        
        result += int(digit) * (16 ** i)
    
    return result

if __name__ == '__main__':
    pass