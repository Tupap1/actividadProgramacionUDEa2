piramydSize = input('ingresa un numero entero del tamaño que quieres que sea la piramide: ')


def printPyramid(size):
    numbers = ''
    for i in range(1, int(size)+1):
        numbers = numbers +  str(i) + ' '
        print(((int(size)  - i)*' ') + numbers)

        
if piramydSize not in '1234567890' or piramydSize < 1 or piramydSize == '':
    print('ingresa una opcion valida')
else:
    printPyramid(piramydSize)