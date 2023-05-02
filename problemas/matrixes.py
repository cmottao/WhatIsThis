from utils import (suma_diagonal_uno, suma_diagonal_dos, cofactor, matriz_por_vector, matriz_transpuesta, 
                   cofactores, matriz_adjunta, dividir_matriz)

'''
    50. Develop an algorithm that allows the addition of two matrices of real numbers (integers).
'''

def sumMatrix(a, b):
    n = len(a)
    m = len(a[0])
    c = []
    for i in range(n):
        f = [] 
        for j in range(m):
            f.append(a[i][j] + b[i][j])  
        c.append(f) 
    return c

'''
    51. Develop an algorithm that allows multiplying two matrices of real numbers (integers).
'''

def multiplicacionMatrix(a, b):
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
    52. Develop a program that adds the elements of a given column of a matrix.
'''

def columnSum(a, k):
    n = len(a)
    s = 0 
    for i in range(n):
        s += a[i][k] 
    return s

'''
    53. Develop a program that adds the elements of a given row of a matrix.
'''

def rowSum(a, k):
    m = len(a[0])
    s = 0 
    for j in range(m):
        s += a[k][j]
    return s

'''
    54. Develop an algorithm that determines if a matrix is magic. A matrix is said to
    square is magical if the sum of each of its rows, of each of its columns and of
    each diagonal is equal.
'''

def magicMatrix(a):
    n = len(a)
    x = rowSum(a, 0)
    y = columnSum(a, 0)
    s = True
    for i in range(1, n):
        s = s and (rowSum(a, i) == x)
    for j in range(1, n):
        s = s and (columnSum(a,j) == y) 
    s = s and (x == y)
    s = s and (trace(a) == x)
    s = s and (secondaryTrace(a) == x) 
    return s

'''
    55. Develop an algorithm that, given an integer, replaces all numbers in a matrix
    greater than a given number by a one and all those less than or equal by a zero.
'''

def replace(a, x):
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
    56. Develop a program that calculates the determinant of a square matrix.
'''

def determinant(a):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2: 
        return (a[0][0]*a[1][1])-(a[0][1]*a[1][0])
    else:
        s = 0 
        for j in range(n):
            s += (-1)**(j)*a[0][j]*(determinant(cofactor(a,j))) 
        return s

'''
    57. Desarrollar un programa que dadas una matriz cuadrada A y un arreglo de números reales
    del mismo tamaño B, calcule una solución x para el sistema de ecuaciones lineales Ax = B.
'''

def solucion_axb(a,b):
    return matriz_por_vector(matriz_inversa(a),b)

'''
    58. Desarrollar un programa que calcule la inversa de una matriz cuadrada.
'''

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