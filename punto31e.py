number = int(input('Ingresa el numero que quieres saber sus divisores: '))

divisores = ''


for i in range(1, number + 1):
    if number % i == 0:
        divisores = divisores +' '+ str(i) 


print(divisores)