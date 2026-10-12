inputPass = input('Ingresa la contraseña: ')

tries = 3
password = '123asd'

while True:
    if inputPass == password:
        print('La contraseña ingresada es correcta')
        break
    else:
        while tries > 0:
            tries -= 1
            print('Contraseña incorrecta, tienes', tries, 'intentos mas.'  )
            inputPass = input('Ingresa la contraseña')
        print('agotaste el numero de intentos')
        break
