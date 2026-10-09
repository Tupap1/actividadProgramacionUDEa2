""" userInputNumA = float(input('Ingresa el numero A'))
userInputNumB = float(input('Ingresa el numero B'))


userInputOperation = int(input('Ingresa la operacion que quieres realizar: \n  1. Multiplicacion \n  2. Residuo de A/B \n 3. A**B \n 4. mayor de los dos numeros \n 5. Salir'))
 """
def calculadora(operation, numberA, numberB):
    result = None
    operation = int(operation)
    if operation == 1:
        result = numberA* numberB
    elif operation == 2:
        result = numberA % numberB
    elif operation == 3:
        result = numberA ** numberB
    elif operation == 4:
        if numberA > numberB:
            result = numberA
        else:
            result = numberB
    return result

while True:
    userInputNumA = float(input('Ingresa el numero A: '))
    userInputNumB = float(input('Ingresa el numero B: '))
    userInputOperation = input('1. Multiplicacion \n2. Residuo de A/B \n3. A**B \n4. mayor de los dos numeros \n5. Salir \nIngresa la operacion que quieres realizar:')

    if userInputOperation == '5':
        break
    while userInputOperation not in '1234':
        print('Ingresa una opcion valida')
        userInputOperation = input('Ingresa la operacion que quieres realizar: \n  1. Multiplicacion \n  2. Residuo de A/B \n A**B \n mayor de los dos numeros \n 5. Salir')
    print('El resultado de la operacion es: ',calculadora(userInputOperation, userInputNumA, userInputNumB))
    print('*********************************************')
