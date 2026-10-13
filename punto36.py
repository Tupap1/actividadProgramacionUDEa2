word = input('Ingresa una frase o palabra para verificar si es palindroma: ')


def cleanPhrase(phrase):
    phraseToClean = phrase.lower()
    cleanedPhrase = ''
    for i in phraseToClean:
        if i == 'á':
            cleanedPhrase = cleanedPhrase + 'a'
        elif i == 'é':
            cleanedPhrase = cleanedPhrase + 'e'
        elif i == 'í':
            cleanedPhrase = cleanedPhrase + 'i'
        elif i == 'ó':
            cleanedPhrase = cleanedPhrase + 'o'
        elif i == 'ú':
            cleanedPhrase = cleanedPhrase + 'u'
        elif i in 'abcdefghijklmnñopqrstuvwxyz0123456789':
            cleanedPhrase = cleanedPhrase + i
    return cleanedPhrase


while True:
    if word == 'Me voy':
        print('Hasta luego...')
        break
    else:
        phrase = cleanPhrase(word)
        reversedWord = ''
        for i in range(-1, -len(phrase)-1, -1):
                reversedWord = reversedWord + phrase[i]

        if reversedWord == phrase:
            print('la palabra o frase es palindroma')
        else:
            print('la palabra o frase NO es palindroma')
        print('.......................................................')
        word = input('Ingresa una frase o palabra para verificar si es palindroma: ')
         