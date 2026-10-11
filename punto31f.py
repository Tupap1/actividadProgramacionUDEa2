number = input('Ingresa un numero para saber cuantos digitos tiene: ')

#esta es la manera obvia pero no se si es valida
print('El numero tiene',len(number), 'cifras')

#este es el algoritmo de forma logica
counter = 1
divider = 10
number = float(number)
while number >  1:
    counter += 1
    number =  number / divider
    divider = divider * 10

print('El numero tiene:', counter, 'cifras' )


