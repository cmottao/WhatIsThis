'''
    71. Desarrollar un algoritmo que reciba como entrada un carácter y de como salida el número 
    de ocurrencias de dicho carácter en una cadena de caracteres.
'''

def contar_ocurrencias(a,b):
    s = 0 
    for x in b:
        if a == x:
            s += 1
    return s

'''
    72. Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es
    subcadena de la segunda.
'''

def subcadena(a,b):
    n = len(a)
    m = len(b)
    if n > m:
        return False
    else:
        s = False 
        for i in range(m-n+1):
            s2 = True 
            for j in range(n):
                s2 = s2 and (b[i+j] == a[j])
            s = s or s2
        return s

'''
    73. Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera está
    incluida en la segunda. 
'''

def incluida(a,b):
    n = len(a)
    m = len(b)
    if n > m:
        return False
    else:
        s = True 
        for x in a:
            s = s and (contar_ocurrencias(x,a) <= contar_ocurrencias(x, b))
        return s

'''
    74. Desarrollar un algoritmo que invierta una cadena de caracteres.
'''

def invertir_cadena_aux(a,n):
    if n == 1:
        return a[0] 
    else:
        return a[n-1]+invertir_cadena_aux(a, n-1) 

def invertir_cadena(a):
    return invertir_cadena_aux(a, len(a))

'''
    75. Desarrollar un algoritmo que determine si una cadena de caracteres es palíndrome. Una cadena
    se dice palíndrome si al invertirla es igual a ella misma.
'''

def cadena_palindrome(a):
    n = len(a)
    s = True
    for i in range(n//2):
        s = s and (a[i] == a[n-1-i]) 
    return s

'''
    76. Desarrollar un algoritmo que determina si una cadena de caracteres es frase palíndrome. Una
    cadena se dice frase palíndrome si la cadena al eliminarle los espacios es palíndrome.
'''

def quitar_espacios(a):
    b = []
    for i in a:
        if i != " ":
            b.append(i)
    return b

def frase_palindrome(a):
    return cadena_palindrome(quitar_espacios(a))

'''
    77. Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
    caracteres. El corrimiento circular a izquierda es pasar el primer carácter de una cadena como
    último carácter de la misma.
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