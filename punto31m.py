inputPass = input('Ingresa la contraseña: ')

tries = 3
password = '123asd'

while True:
    if inputPass == password:
        print('acceso concedido')
        break
    else:
        while tries != 0:
            tries -= 1
            print('Contraseña incorrecta, tienes', tries+1, 'intentos mas.'  )
            inputPass = input('Ingresa la contraseña')
            if inputPass == password:
                print('acceso concedido')
                break
        print('agotaste el numero de intentos')
        break
