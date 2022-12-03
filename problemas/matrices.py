
'''
    50. Desarrollar un algoritmo que permita sumar dos matrices de números reales (enteros).
'''

def suma_matrices(a,b):
    n = len(a)
    m = len(a[0])
    c = []
    for i in range(n):
        f = [] 
        for j in range(m):
            f.append(a[i][j]+b[i][j])  
        c.append(f) 
    return c

'''
    51. Desarrollar un algoritmo que permita multiplicar dos matrices de números reales (enteros).
'''

def multiplicar_matrices(a,b):
    n = len(a)
    m = len(b)
    l = len(b[0])
    c = []
    for i in range(n):
        f = [] 
        for j in range(l):
            s = 0 
            for k in range(m):
                s += a[i][k] * b[k][j] 
            f.append(s) 
        c.append(f) 
    return c

'''
    52. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
'''

def sumar_columna(a,k):
    n = len(a)
    s = 0 
    for i in range(n):
        s += a[i][k] 
    return s

'''
    53. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
'''

def sumar_fila(a,k):
    m = len(a[0])
    s = 0 
    for j in range(m):
        s += a[k][j]
    return s

'''
    54. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada 
    es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
'''

def suma_diagonal_uno(a):
    n = len(a)   
    s = 0 
    for i in range(n):
        s += a[i][i]
    return s

def suma_diagonal_dos(a):
    n = len(a)
    s = 0
    for i in range(n):
        s += a[i][n-i-1]
    return s

def matriz_magica(a):
    n = len(a)
    x = sumar_fila(a, 0)
    y = sumar_columna(a, 0)
    s = True
    for i in range(1,n):
        s = (sumar_fila(a,i) == x) and s 
        if not s: return s
    for j in range(1,n):
        s = (sumar_columna(a,j) == y) and s
        if not s: return s
    s = (x == y) and s 
    if not s: return s
    s = (suma_diagonal_uno(a) == x) and s 
    if not s: return s
    s = (suma_diagonal_dos(a) == x) and s 
    return s

'''
    55. Desarrollar un algoritmo que dado un entero, reemplace en una matriz todos los números
    mayores a un número dado por un uno y todos los menores o iguales por un cero.
'''

def reemplazar(a,x):
    n = len(a)
    m = len(a[0])
    b = []
    for i in range(n):
        f = [] 
        for j in range(m):
            if a[i][j] > x: 
                f.append(1)
            else: 
                f.append(0)
        b.append(f) 
    return b

'''
    56. Desarrollar un programa que calcule el determinante de una matriz cuadrada.
'''

def cofactor(a,x): 
    n = len(a)
    b = []
    for i in range(1,n): 
        f = [] 
        for j in range(n):
            if j != x: 
                f.append(a[i][j]) 
        b.append(f)
    return b

def determinante(a):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2: 
        return (a[0][0]*a[1][1])-(a[0][1]*a[1][0])
    else:
        s = 0 
        for j in range(n):
            s += (-1)**(j)*a[0][j]*(determinante(cofactor(a,j))) 
        return s

'''
    57. Desarrollar un programa que dadas una matriz cuadrada A y un arreglo de números reales
    del mismo tamaño B, calcule una solución x para el sistema de ecuaciones lineales Ax = B.
'''

def matriz_por_vector(a,b):
    n = len(a)
    c = []
    for i in range(n):
        s = 0 
        for j in range(n):
            s += a[i][j] * b[j] 
        c.append(s) 
    return c

def solucion_axb(a,b):
    return matriz_por_vector(matriz_inversa(a),b)

'''
    58. Desarrollar un programa que calcule la inversa de una matriz cuadrada.
'''

def matriz_transpuesta(a): 
    n = len(a)
    m = len(a[0])
    b = []
    for i in range(m):
        f = [] #Fila
        for j in range(n):
            f.append(a[j][i])
        b.append(f)
    return b

def cofactores(a,x,y): 
    n = len(a)
    b = []
    for i in range(n):
        if i != x: 
            f = [] 
            for j in range(n):
                if j != y: 
                    f.append(a[i][j]) 
            b.append(f) 
    return b

def matriz_adjunta(a): 
    n = len(a)
    m = len(a[0])
    b = []
    for i in range(n):
        f = [] 
        for j in range(m):
            f.append((-1)**(i+j)*determinante(cofactores(a,i,j))) 
        b.append(f) 
    return b

def dividir_matriz(a,x): 
    n = len(a)
    m = len(a[0])
    b = []
    for i in range(n):
        f = [] 
        for j in range(m):
            f.append(a[i][j]/x) 
        b.append(f) 
    return b

def matriz_inversa(a): 
    return dividir_matriz((matriz_adjunta(matriz_transpuesta(a))),determinante(a))

'''
    59. Desarrollar un programa que tome un arreglo de tamaño n² y llene en espiral hacia adentro
    una matriz cuadrada de tamaño n.
'''

def matriz_espiral(a):
    n = int(len(a)**0.5)
    b = []
    for i in range(n):
        f = []
        for j in range(n):
            f.append(0)
        b.append(f)

    indice_fila = 0
    tope_max_fila = n - 1
    tope_min_fila = 0
    indice_columna = 0
    tope_min_columna = 0
    tope_max_columna = n - 1
    indice_a = 0
    direccion = 'derecha' 
 
    for i in range(len(a)):
        b[indice_fila][indice_columna] = a[indice_a]
        if direccion == 'derecha':
            if indice_columna == tope_max_columna: 
                tope_min_fila = indice_fila + 1 
                direccion = 'abajo' 
                indice_fila += 1 
            else:
                indice_columna += 1
        elif direccion == 'abajo':
            if indice_fila == tope_max_fila:
                tope_max_columna = indice_columna - 1
                direccion = 'izquierda'
                indice_columna -= 1
            else:
                indice_fila += 1
        elif direccion == 'izquierda':
            if indice_columna == tope_min_columna:
                tope_max_fila = indice_fila - 1
                direccion = 'arriba'
                indice_fila -= 1
            else:
                indice_columna -= 1
        elif direccion == 'arriba':
            if indice_fila == tope_min_fila:
                tope_min_columna = indice_columna + 1
                direccion = 'derecha'
                indice_columna += 1
            else:
                indice_fila -= 1 
        indice_a += 1
    return b