binarynum = input('Ingresa el numero que quieres convertir de binario a decimal: ')


decimal = 0
power = 0
while True:
    for i in range(0, len(binarynum)):
        if binarynum[i] != '0' and binarynum[i] != '1':
            print('ingrese una opcion valida')
            binarynum = input('Ingresa el numero que quieres convertir de binario a decimal: ')
            break
    else:
        break


for i in range(-1, -len(binarynum), -1):
    print(decimal, binarynum[i])
    decimal = decimal + (int(binarynum[i]) * (2**power))
    power += 1
                
                
                
print('EL numero', binarynum, 'en decimal es: ', decimal)