binarynum = input('Ingresa el numero que quieres convertir de binario a decimal: ')

decimal = 0
power = 0
isValid = False
while not isValid:
    isValid = True
    for i in binarynum:
        if i != '0' and i != '1':
            isValid = False
    if not isValid:
        print('ingrese una opcion valida')
        binarynum = input('Ingresa el numero que quieres convertir de binario a decimal: ')

for i in range(-1, -len(binarynum)-1, -1):
    decimal = decimal + (int(binarynum[i]) * (2**power))
    power += 1
                      
print('EL numero', binarynum, 'en decimal es: ', decimal)