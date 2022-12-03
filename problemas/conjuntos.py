''' 
    35. Unión: Calcula en un arreglo la unión de los conjuntos y la imprime.
'''

def union_conjuntos(a,b):
    c = []
    for i in a: 
        c.append(i) 
    for i in b:
        if i not in c: 
            c.append(i)
    return c

''' 
    36. Intersección: Calcula en un arreglo la intersección de los conjuntos y la imprime.
'''

def interseccion_conjuntos(a,b):
    c = []
    for i in a:
        if i in b: 
            c.append(i)
    return c

'''
    37. Calcula en un arreglo la diferencia del primero con el segundo y la imprime.
'''

def diferencia_conjuntos(a,b):
    c = []
    for i in a:
        if i not in b: 
            c.append(i)
    return c

'''
    38. Diferencia simétrica: Calcula en un arreglo la diferencia simétrica de los conjuntos y la imprime.
'''

def dif_simetrica_conjuntos(a,b): 
    return union_conjuntos(diferencia_conjuntos(a, b), diferencia_conjuntos(b, a))

'''
    39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los
    conjuntos y lo imprime.
'''

def pertenece(a,n):
    s = False 
    for x in a:
        s = s or (x == n)
    return s

'''
    40. Contenido: Determina si el primer conjunto está contenido en el segundo y lo imprime.    
'''

def contenencia_conjuntos(a,b):
    return interseccion_conjuntos(a,b) == a 