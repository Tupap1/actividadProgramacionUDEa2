userInputWorkedHours = int(input('Ingresa la cantidad de horas trabajadas: '))
userInputBranch = input('ingresa la sucursal: ')

def calculateSalary(workedHours, branch):
    salary = 0
    if branch == 'A':
        if workedHours < 40:
            salary = workedHours * 10
        else:
            salary = (39 * 10) + ((workedHours - 39) * 20)
        print('El salario semanal para', workedHours, 'y en la sucursal', branch, 'es de', salary )

    elif branch == 'B':
        if workedHours < 45:
            salary = workedHours * 12
        else:
            salary =  (44 * 12) + ((workedHours - 44) * 25)
        print('El salario semanal para', workedHours, 'y en la sucursal', branch, 'es de', salary )

if userInputBranch  in 'AB' and userInputWorkedHours >= 1:
    calculateSalary(userInputWorkedHours, userInputBranch)
else:
    print('Ingresa una opcion valida')