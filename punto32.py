char = input('Ingresa un caracter para evaluar que es: ')


if char in 'aeiou':
    print('El caracter es una vocal y es minuscula')
elif char in 'AEIOU':
    print('El caracter es una vocal y es mayuscula')
elif char in 'bcdfghjklmnñpqrstvwxyz':
    print('El caracter es una consonante y es minuscula')
elif char in 'BCDFGHJKLMNÑPQRSTVWXYZ':
    print('El caracter es una consonante y es mayuscula')  
elif char in '0123456789':
    print('El caracter es un numero')
else:
    print('Caracter no identificado')  
