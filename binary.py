def binario2octal(binario):
    result = ''
    while len(binario) >= 3:
        digit = str(binario2decimal(binario[-3:]))
        result = digit + result
        binario = binario[:-3]
    
    if len(binario) > 0:
        result = str(binario2decimal(binario)) + result 
    
    return result

def binario2decimal(binario):
    result = 0
    for i in range(len(binario)):
        result += int(binario[-(i + 1)]) * (2 ** i)
    
    return result

def binario2hexadecimal(binario):
    result = ''
    while len(binario) >= 4:
        digit = str(binario2decimal(binario[-4:]))
        
        if int(digit) > 9:
            if digit == '10':
                digit = 'A'
            elif digit == '11':
                digit = 'B'
            elif digit == '12':
                digit = 'C'
            elif digit == '13':
                digit = 'D'
            elif digit == '14':
                digit = 'E'
            elif digit == '15':
                digit = 'F'
        
        result = digit + result
        binario = binario[:-4]
    
    if len(binario) > 0:
        result = str(binario2decimal(binario)) + result 
    
    return result

if __name__ == '__main__':
    pass