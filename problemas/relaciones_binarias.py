'''
    60. Unión: Calcula e imprime la relación unión.
'''

def union_relaciones(a,b):
    n = len(a)
    m = len(a[0])
    c = []
    for i in range(n):
        f = [] 
        for j in range(m):
            if a[i][j] or b[i][j] == 1: 
                f.append(1)
            else: 
                f.append(0) 
        c.append(f) 
    return c

'''
    61. Intersección: Calcula e imprime la relación intersección.
'''

def interseccion_relaciones(a,b):
    n = len(a)
    m = len(a[0])
    c = []
    for i in range(n):
        f = [] 
        for j in range(m):
            if a[i][j] and b[i][j] == 1: 
                f.append(1)
            else: 
                f.append(0)
        c.append(f) 
    return c

'''
    62. Simetría: Determina si la primer relación es simétrica o no.
'''

def relacion_simetrica(a):
    n = len(a)
    s = True 
    for i in range(n):
        for j in range(n):
            s = s and (a[i][j] == a[j][i]) 
    return s

'''
    63. Reflexividad: Determina si la primer relación es reflexiva o no.
'''

def relacion_reflexiva(a):
    n = len(a)
    s = True 
    for i in range(n):
            s = s and (a[i][i] == 1)
    return s

'''
    64. Transitividad: Determina si la primer relación leída es transitiva o no.
'''

def multiplicar_relaciones(a,b): 
    n = len(a)
    m = len(b)
    l = len(b[0])
    c = []
    for i in range(n):
        f = [] 
        for j in range(l):
            s = 0 
            for k in range(m):
                s = s or (a[i][k] and b[k][j]) 
            f.append(s) 
        c.append(f) 
    return c

def relacion_transitiva(a): 
    n = len(a)
    m = len(a[0])
    b = multiplicar_relaciones(a, a)
    s = True  
    for i in range(n):
        for j in range(m):
            s = s and (b[i][j] <= a[i][j]) 
    return s

'''
    65. Orden: Determina si la primer relación leída es relación de orden o no.
'''

def relacion_orden(a): 
    return relacion_reflexiva(a) and relacion_transitiva(a) and not relacion_simetrica(a)

'''
    66. Equivalencia: Determina si la primer relación leída es una relación de equivalencia.
'''

def relacion_equivalencia(a):
    return relacion_reflexiva(a) and relacion_transitiva(a) and relacion_simetrica(a)

'''
    67. Función: Determina si la relación es una función o no.
'''

def relacion_funcion(a):
    n = len(a)
    m = len(a[0])
    s = True 
    for i in range(n):
        s2 = 0 
        for j in range(m):
            s2 += a[i][j]
        s = s and (s2 <= 1) 
    return s

'''
    68. Inyectividad: Determina si la relación es una función inyectiva.
'''

def funcion_inyectiva(a):
    n = len(a)
    m = len(a[0])
    s = True 
    for j in range(m):
        s2 = 0 
        for i in range(n):
            s2 += a[i][j]
            s = s and (s2 <= 1) 
    return s and relacion_funcion(a) 

'''
    69. Sobreyectividad: Determina si la relación es una función sobreyectiva.
'''

def funcion_sobreyectiva(a):
    n = len(a)
    m = len(a[0])
    s = True 
    for j in range(m):
        s2 = False 
        for i in range(n):
            s2 = s2 or (a[i][j] == 1) 
        s = s and s2 
    return s and relacion_funcion(a) 