""" En una empresa el pago a sus trabajadores depende de las horas trabajadas a la
semana y la sucursal en la que se encuentran. En la sucursal A se paga $10/hora si se
trabajan menos de 40 horas, y en la sucursal B se paga $12/hora si se trabajan menos
de 45 horas. Las horas extra en la sucursal A se cobran a $20 y en la sucursal B a $25.
Calcule el salario semanal de acuerdo a las horas trabajadas y la sucursal ingresada por
el usuario. """

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
            salary =  (44 * 12) + ((workedHours - 44) * 20)
        print('El salario semanal para', workedHours, 'y en la sucursal', branch, 'es de', salary )

calculateSalary(userInputWorkedHours, userInputBranch)
