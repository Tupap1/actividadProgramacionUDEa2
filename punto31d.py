usedWater = input('Ingresa la cantida de m3 consumidos: ')
economicTier = input('Ingresa el estrato: ')

while True:
    if float(usedWater) < 0:
        print('ingresa una opcion valida')
        usedWater = input('Ingresa la cantida de m3 consumidos: ')
    elif economicTier not in '123456':
        print('ingresa una opcion valida')
        economicTier = input('Ingresa el estrato: ')
    else:
        break

total = 0
def calculateTotal(usedWater, economicTier):
    total = 0
    if usedWater <= 9:
        total = usedWater * 6
    elif usedWater <= 13:
        total = usedWater * 5
    else:
        total = usedWater * 9
    if economicTier in '12':
        total = total * 0.80
    return total + 50

print('El total a pagar es de: ', calculateTotal(float(usedWater), economicTier))
