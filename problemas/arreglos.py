'''
    22. Implementar la criba de Eratostenes para calcular los números primos en el rango 1 a n, donde
    n es un número natural dado por el usuario.
'''

def eratostenes(n):
    primos = []
    no_primos = []
    for i in range(2,n+1):
        if i not in no_primos: 
            primos.append(i)
            for j in range(i * i,n+1,i): 
                no_primos.append(j)
    return primos

'''
    23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de números enteros
    (reales).
'''

def suma_arreglo(a):
    s = 0 
    for x in a: 
        s += x
    return s

'''
    24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).
'''

def promedio_arreglo(a):
    n = len(a)
    s = 0 
    for x in a: 
        s += x
    return s / n

'''
    25. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de enteros (reales) de
    igual tamaño.
'''

def producto_punto(v,w):
    n = len(v)
    p = 0 
    for i in range(n):
        p += v[i]*w[i]
    return p

'''
    26. Desarrollar un algoritmo que calcule el mínimo de un arreglo de números enteros (reales).
'''

def min(a,b):
    if a <= b:
        return a
    else:
        return b

def minimo_arreglo_aux(a,n):
    if n == 1:
        return a[0] 
    else:
        return min(a[n-1],minimo_arreglo_aux(a,n-1)) 

def minimo_arreglo(a):
    return minimo_arreglo_aux(a,len(a))

'''
    27. Desarrollar un algoritmo que calcule el máximo de un arreglo de números enteros (reales).
'''

def max(a,b):
    if a >= b:
        return a
    else:
        return b

def maximo_arreglo_aux(a,n):
    if n == 1:
        return a[0] 
    else:
        return max(a[n-1],maximo_arreglo_aux(a,n-1)) 

def maximo_arreglo(a):
    return maximo_arreglo_aux(a,len(a))

'''
    28. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de
    igual tamaño.
'''

def producto_directo(v,w):   
    n = len(v)
    x = []
    for i in range(n):
        x.append(v[i] * w[i])
    return x

'''
    29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La
    mediana es el número que queda en la mitad del arreglo después de ser ordenado.
'''

def ordenar(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def mediana_arreglo(a):
    ordenar(a) 
    n = len(a)
    if n % 2 != 0: 
        return a[n//2]
    else: 
        return (a[n//2]+a[n//2-1]) / 2

'''
    30. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan
    en dicho arreglo.
'''
   
def contar(a): 
    c = 0
    for i in a:
        if i == 0:
            c += 1
    return c

def remover(a): 
    b = [] 
    for i in a:
        if i != 0:
            b.append(i)
    return b

def agregar(b,c): 
    for i in range(c):
        b.append(0)    
    return b

def mover_ceros_arreglo(a):
    return agregar(remover(a),contar(a))

''' 
    31. Suponga que un arreglo de enteros esta lleno de unos y ceros y que el arreglo representa un
    número binario al revés. Hacer un algoritmo que calcule los números en decimal que representa
    dicho arreglo de unos y ceros.
'''

def bad(a):
    n = len(a)
    s = 0 
    for i in range(n):
        s += a[i]*2**i
    return s

''' 
    32. Hacer un algoritmo que dado un número entero no negativo, cree un arreglo de unos y ceros
    que representa el número en binario al revés.
'''

def dab(n):
  if n < 2:
    return [n] 
  else:
    return [n % 2] + dab(n // 2)

'''
    33. Hacer un algoritmo que calcule el Máximo Común Divisor (MCD) para un arreglo de enteros
    positivos.
'''

def mcd(a,b):
    if b > a: 
        return mcd(b,a) 
    elif a % b == 0:
        return b
    else:
        return mcd(b, a % b)

def mcd_arreglo_aux(a,n):
    if n == 1:
        return a[0] 
    else:
        return mcd(a[n-1],mcd_arreglo_aux(a,n-1))

def mcd_arreglo(a):
    return mcd_arreglo_aux(a,len(a)) 

''' 
    34. Hacer un algoritmo que calcule el Mínimo Común Múltiplo (MCM) para un arreglo de enteros
    positivos.
'''

def mcm(a,b):
    return int((a*b) / mcd(a,b)) 

def mcm_arreglo_aux(a,n):
    if n == 1:
        return a[0] 
    else: 
        return mcm(a[n-1],mcm_arreglo_aux(a,n-1)) 

def mcm_arreglo(a):
    return mcm_arreglo_aux(a,len(a))