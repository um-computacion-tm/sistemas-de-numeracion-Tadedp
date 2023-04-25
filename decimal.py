def decimal2binario(decimal):
    result = ''
    
    while decimal >= 2:
        result = str(decimal % 2) + result 
        decimal = decimal // 2
    
    result = str(decimal) + result
    return result

def decimal2octal(decimal):
    result = ''
    
    while decimal >= 8:
        result = str(decimal % 8) + result 
        decimal = decimal // 8
    
    result = str(decimal) + result
    return result

def decimal2hexadecimal(decimal):
    result = ''
    
    while decimal >= 16:
        modulo = decimal % 16
        
        if modulo > 9:
            if modulo == 10:
                modulo = 'A'
            if modulo == 11:
                modulo = 'B'
            if modulo == 12:
                modulo = 'C'
            if modulo == 13:
                modulo = 'D'
            if modulo == 14:
                modulo = 'E'
            if modulo == 15:
                modulo = 'F'
        
        result = str(modulo) + result 
        decimal = decimal // 16
    
    result = str(decimal) + result
    return result

if __name__ == '__main__':
    pass