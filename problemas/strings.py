'''
    71. Develop an algorithm that receives a character as input and outputs the number of
    occurrences of that character in a character string.
'''

def countOcurrences(a, b):
    s = 0 
    for x in b:
        if a == x:
            s += 1
    return s

'''
    72. Develop an algorithm that takes two strings as input and determines if the first is
    substring of the second. (Do not use language-specific substring operations of programming).
'''

def substring(a, b):
    n = len(a)
    m = len(b)
    if n > m:
        return False
    else:
        s = False 
        for i in range(m - n + 1):
            s2 = True 
            for j in range(n):
                s2 = s2 and (b[i + j] == a[j])
            s = s or s2
        return s

'''
    73. Develop an algorithm that receives two character strings and determines if the first one is
    included in the second. A string is said to be included in another if all characters (with repetitions) 
    of the string is in the second string regardless of the order of the characters.
'''

def included(a, b):
    n = len(a)
    m = len(b)
    if n > m:
        return False
    else:
        s = True 
        for x in a:
            s = s and (countOcurrences(x, a) <= countOcurrences(x, b))
        return s

'''
    74. Develop an algorithm that reverses a string of characters.
'''

def reverseStringAux(a, n):
    if n == 1:
        return a[0] 
    else:
        return a[n - 1] + reverseStringAux(a, n - 1) 

def reverseString(a):
    return reverseStringAux(a, len(a))

'''
    75. Develop an algorithm that determines if a character string is a palindrome. A string
    it is called a palindrome if when inverted it is equal to itself.
'''

def palindrome(a):
    n = len(a)
    s = True
    for i in range(n // 2):
        s = s and (a[i] == a[n-1-i]) 
    return s

'''
    76. Develop an algorithm that determines if a character string is a palindrome sentence. A
    string is called a palindrome phrase if the string is palindrome when removing the spaces.
'''

def removeSpacesAux(a, n): 
    if n == 1:
        return a[0] 
    elif a[n - 1] == " ":
        return removeSpacesAux(a, n - 1) 
    else:
        return removeSpacesAux(a, n - 1) + a[n - 1] 

def removeSpaces(a):
    return removeSpacesAux(a, len(a))

def frase_palindrome(a):
    return palindrome(removeSpaces(a))

'''
    77. Develop an algorithm that performs the circular shift to the left of a string of
    characters. Circular leftshift is passing the first character of a string as
    last character of it.
'''

def corrimiento_izquierda_aux(a,n,i):
    if n-1 == i:
        return a[0]
    else:
        return a[i-n+1]+corrimiento_izquierda_aux(a,n,i+1)

def corrimiento_izquierda(a):
    return corrimiento_izquierda_aux(a, len(a),0)

'''
    78. Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de caracteres.
    El corrimiento circular a derecha de una cadena es poner el último carácter de la cadena como primer 
    carácter de la misma.
'''

def corrimiento_derecha_aux(a,n):
    if n == 1:
        return a[n-2]
    else:
        return corrimiento_derecha_aux(a,n-1)+a[n-2]

def corrimiento_derecha(a):
    return corrimiento_derecha_aux(a, len(a))

'''
    79. Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de
    correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
    carácter el carácter equivalente para el carácter "a", el segundo carácter para la "b"y así 
    sucesivamente hasta la "z". No se tiene traducción para las mayúsculas ni para la "ñ".
'''

def codificar(a,b):
    abc = "abcdefghijklmnopqrstuvwxyz"
    c = ""
    for i in a:
        if i not in abc:
            c += i
        else:
            x = abc.find(i)
            c += b[x]
    return c

'''
    80. Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de
    correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
    carácter el carácter equivalente para el carácter "a", el segundo carácter para la "b" y 
    así sucesivamente hasta la "z". No se tiene traducción para las mayúsculas ni para la "ñ".
'''

def decodificar(a,b):
    abc = "abcdefghijklmnopqrstuvwxyz"
    c = ""
    for i in a:
        if i not in abc:
            c += i
        else:
            x = b.find(i)
            c += abc[x]
    return c 