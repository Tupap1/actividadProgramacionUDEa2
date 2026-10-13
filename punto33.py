string = input('Ingresa la frase que quieras cambiar espacios por "-": ')


newString = ''
for i in range(0, len(string)):
    if string[i] == ' ':
        newString = newString + '-'
    else:
        newString = newString + string[i]

print(newString)