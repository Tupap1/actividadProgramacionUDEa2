secret = input('Ingresa la palabra que quieres ocultar: ')


def scramblePhrase(word):
    evens = ''
    unevens = ''
    for i in range(0, len(word)):
        if i % 2 == 0:
            evens = evens + word[i]
        else:
            unevens = unevens + word[i]
    return evens + unevens

def replaceVowels(word):
    result = ''
    for i in word:
        if i in 'aA':
            result = result + '1'
        elif i in 'eE':
            result = result + '2'
        elif i in 'iI':
            result = result + '3'
        elif i in 'oO':
            result = result + '4'
        elif i in 'uU':
            result = result + '5'
        else: 
            result= result + i 

    return result

def doAll(word):
    scrambled = scramblePhrase(word)
    return replaceVowels(scrambled)

finalPhrase = ''
palabra = ''

for i in secret:
    if i != ' ':
        palabra = palabra + i
    else:
        
        finalPhrase = finalPhrase + doAll(palabra) + ' '
        palabra = ''

finalPhrase = finalPhrase + doAll(palabra) 


print(finalPhrase)
        
