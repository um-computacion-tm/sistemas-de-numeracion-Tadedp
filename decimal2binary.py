def decimal2binario(decimal):
    result = ''
    while decimal >= 2:
        result = str(decimal % 2) + result 
        decimal = decimal // 2
    
    result = str(decimal) + result
    while len(result) % 8 != 0:
        result = '0' + result
    return result

if __name__ == '__main__':
    pass