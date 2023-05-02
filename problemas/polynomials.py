from utils import agregar, igualar, limpiar_polinomio, dividir_monomios

'''    
    43. Evalauate: Reads a real and prints the evaluation of the two polynomials in said data.
'''

def evaluate(p, x):
    n = len(p)
    s = 0 
    for i in range(n):
        s += p[i] * x ** i
    return s

'''    
    44. Add: Calculates the sum polynomial and prints it.
'''

def sumar_polinomios(p,q):
    n = len(p)
    igualar(p,q) 
    r = []
    for i in range(n):
        r.append(p[i]+q[i]) 
    limpiar_polinomio(r) 
    return r

'''
    45. Resta: Calcula el polinomio resta y lo imprime.
'''

def restar_polinomios(p,q):
    n = len(p)
    igualar(p,q) 
    r = []
    for i in range(n):
        r.append(p[i]-q[i]) 
    limpiar_polinomio(r) 
    return r

'''
    46. Multiplicar: Calcula el polinomio multiplicación y lo imprime:
'''

def multiplicar_polinomios(p,q):
    n = len(p)
    m = len(q)
    limpiar_polinomio(p) 
    limpiar_polinomio(q)
    productos = []
    for i in range(n):
        for j in range(m): 
            termino = []
            termino.append(p[i]*q[j]) 
            termino.append(i+j) 
            productos.append(termino)
    r = []
    max_grado = (n + m)-1 
    for i in range(0,max_grado): 
        s = 0
        for j in range(len(productos)):
            if productos[j][1] == i: 
                s += productos[j][0] 
        r.append(s) 
    return r

'''
     47. Dividir: Calcula el polinomio división del primer polinomio por el segundo y lo imprime.
'''

def dividir_polinomios(p,q):
    n = len(p)
    m = len(q)
    if m > n: 
        return [0]
    else:
        r = []
        while(n>=m): 
            x = dividir_monomios(p, q) 
            p = restar_polinomios(p, multiplicar_polinomios(x,q)) 
            r = [x[len(x)-1]] + r 
            n = len(p) 
        limpiar_polinomio(r) 
        return r 

'''
     48. Residuo: Calcula el polinomio residuo de la división del primero por el segundo y lo imprime.
'''

def residuo_dividir_polinomios(p,q):
    n = len(p)
    m = len(q)
    if m > n: 
        return [0]
    else:
        r = []
        while(n>=m): 
            x = dividir_monomios(p, q) 
            p = restar_polinomios(p, multiplicar_polinomios(x,q)) 
            r = [x[len(x)-1]] + r 
            n = len(p) 
        limpiar_polinomio(r) 
        return p 