'''
    71. Given a character and a string, determine how many ocurrences of that character there are in the string.
'''

def countOcurrences(a, b):
    s = 0 
    for x in b:
        if a == x:
            s += 1
    return s


'''
    72. Given two strings, determine if the first is substring of the second.
'''

def substring(a, b):
    n = len(a)
    m = len(b)
    s = False 
    for i in range(m - n + 1):
        s2 = True 
        for j in range(n):
            s2 = s2 and (b[i + j] == a[j])
        s = s or s2
    return s


'''
    73. Given two strings, determine if the first one is included in the second. A string is said to be included in another if all characters (with repetitions) 
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
    74. Develop an algorithm that reverses a string.
'''

def reverseStringAux(a, n):
    if n == 1:
        return a[0] 
    else:
        return a[n - 1] + reverseStringAux(a, n - 1) 

def reverseString(a):
    return reverseStringAux(a, len(a))


'''
    75. Determine if a character string is a palindrome.
'''

def palindrome(a):
    n = len(a)
    s = True
    for i in range(n // 2):
        s = s and (a[i] == a[n-1-i]) 
    return s


'''
    76. Determine if a character string is a palindrome sentence. A string is called a palindrome phrase if the 
    string is palindrome when removing the spaces.
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

def palindromeSentence(a):
    return palindrome(removeSpaces(a))


'''
    77. Perform the circular shift to the left of a string. Circular left shift is passing the first character of
    a string as last character of it.
'''

def leftShiftAux(a, n, i):
    if n - 1 == i:
        return a[0]
    else:
        return a[i - n + 1] + leftShiftAux(a, n, i + 1)

def leftShift(a):
    return leftShiftAux(a, len(a), 0)


'''
    78. Perform the circular shift to the right of a string. Circular right shift is passin the last character of
    a string as first character of it.
'''

def rightShiftAux(a, n):
    if n == 1:
        return a[n - 2]
    else:
        return rightShiftAux(a, n - 1) + a[n - 2]

def rightShift(a):
    return rightShiftAux(a, len(a))


'''
    80. Encode a string using a given string of correspondences. The string of correspondences has as the first
    character the equivalent character for the character "a", the second character for "b" and so on up to "z". 
    There is no translation for capital letters and "ñ".
'''

def encode(a,b):
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
    80. Decode a string using a given string of correspondences. The string of correspondences has as the first
    character the equivalent character for the character "a", the second character for "b" and so on up to "z". 
    There is no translation for capital letters and "ñ".
'''

def decode(a,b):
    abc = "abcdefghijklmnopqrstuvwxyz"
    c = ""
    for i in a:
        if i not in abc:
            c += i
        else:
            x = b.find(i)
            c += abc[x]
    return c 