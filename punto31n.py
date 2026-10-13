piramydSize = input('ingresa un numero entero del tamaño que quieres que sea la piramide: ')


def printPyramid(size):
    numbers = ''
    for i in range(1, int(size)+1):
        numbers = numbers +  str(i) + ' '
        print(((int(size)  - i)*' ') + numbers)

isValid = True
for i in piramydSize:
    if i not in '1234567890':
        isValid = False

if not isValid or piramydSize == '' or int(piramydSize) < 1:
    print('ingresa una opcion valida')
else:
    printPyramid(piramydSize)