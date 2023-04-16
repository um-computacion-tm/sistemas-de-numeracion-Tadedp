def binario2decimal(binario):
    result = 0
    for i in range(len(binario)):
        result += int(binario[-(i + 1)]) * (2 ** i)
    return result

if __name__ == '__main__':
    pass