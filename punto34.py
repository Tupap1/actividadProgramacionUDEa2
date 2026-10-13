inputPass = input('Ingresa la contraseña: ')


def isPalindromus(word):
    original = word
    reverseWord = ''
    for i in range(-1, -len(word)-1, -1):
        reverseWord = reverseWord + word[i]
    return reverseWord == original

def verifyPass(passw):
    number = False
    letter = False
    if len(passw) <8 or len(passw)> 20:
        size = 'No OK'
    else:
        size = 'OK'

    for i in passw:
        if i in 'aeiouAEIOUbcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ':
            letter = True
    for i in passw :
        if i in '0123456789':
            number = True

    if letter and number:
        lettersNumbers = 'OK'
    else:
        lettersNumbers = 'No OK'

    for i in passw:
        if i in '!”#$%&/()=?+,*':
            specialChars = 'OK'
            break
        else:
            specialChars = 'No Ok'
    
    if isPalindromus(passw):
        palindromus = 'No OK'
    else:
        palindromus = 'OK'

    if size == 'OK' and lettersNumbers == 'OK' and specialChars == 'OK' and palindromus == 'OK':
        result = 'La contraseña se ha creado satisfactoriamente !!!'
    else: 
        result = 'La contraseña no cumple con los requisitos'

    print('Longitud correcta: ', size )
    print( 'Incluye letras y numeros: ', lettersNumbers)
    print('incluye caracteres especiales: ', specialChars)
    print('No es palindroma: ', palindromus)
    print(result)


if inputPass == '':
    print('Ingresa una contraseña valida')
else:    
    verifyPass(inputPass)