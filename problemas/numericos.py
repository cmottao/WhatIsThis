'''
    5. Función potencia de un entero elevado a un entero.
'''

def potencia(b, e):
    if e == 0: 
        return 1
    else:
        return b * potencia(b,e-1) 

'''
    6. Una función que determine si un número es divisible por otro.
'''

def divisible(a, b):
    return a % b == 0

'''
    7. Determinar si un número es primo.
'''

def primo(n):
    s = True 
    for i in range(2,n):
        s = s and (n % i != 0) 
    return s

'''
    8. Dados dos naturales, determinar si son primos relativos.
'''

def mcd(a, b): 
    if b > a: 
        return mcd(b, a)
    elif a % b == 0:
        return b 
    else:
        return mcd(b, a % b)

def primos_relativos(a, b):
    return mcd(a, b) == 1

'''
    9. Determinar si un número es múltiplo de la suma de otros dos números.
'''

def divisible(a, b):
    return a % b == 0
    
def multiplo(x1, x2, a):
    return divisible(a, x1+x2)

'''
    10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado.
'''

def evaluar_pol(a, b, c, x):
    return a*x**2 + b*x + c 

'''
    11. Dados los coeficientes de un polinomio de grado dos, evaluar el coeficiente lineal de la derivada.
'''

def cf_lineal_derivada(a, b, c):
    return 2 * a

'''
    12. Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del
    polinomio en ese punto.
'''

def derivada_punto(a, b, x):
    return 2*a*x + b

'''
    13. Dado un natural, determinar si es un número de Fibonacci o no.
'''

def fibonacci(n):
    fib = [0,1]
    while(fib[-1] < n): 
        fib.append(fib[-1] + fib[-2])
    return n in fib 
