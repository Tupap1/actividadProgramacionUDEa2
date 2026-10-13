minValueInput = input('ingresa el numero de abajo de tu intervalo: ')
maxValueInput = input('ingresa el numero de arriba de tu intervalo: ')

def findPrimeNumbers(minValue, maxValue):
    primeNumbers = ''

    for i in range(minValue, maxValue+1):
        isPrime = True
        if i <= 1:
            isPrime = False
        for a in range(2, i):
            if i % a == 0:
                isPrime = False
        if isPrime:
            primeNumbers = primeNumbers+str(i)+' '
    return primeNumbers

print('Los numeros primos del intervalo ingresado son: ',findPrimeNumbers(int(minValueInput), int(maxValueInput)))

