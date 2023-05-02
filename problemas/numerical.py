from utils import gcd

'''
    5. Function power of an integer raised to an integer.
'''

def power(b, e):
    if e == 0: 
        return 1
    else:
        return b * power(b, e-1) 

'''
    6. A function that determines whether one number is divisible by another.
'''

def divisible(a, b):
    return a % b == 0

'''
    7. Determine if a number is prime.
'''

def prime(n):
    s = True 
    for i in range(2, int(n ** 0.5) + 1):
        s = s and (n % i != 0) 
    return s

'''
    8. Given two natural, determine if they are relative primes.
'''

def relativePrimes(a, b):
    return gcd(a, b) == 1

'''
    9. Determine if a number is a multiple of the sum of two others.
'''
    
def multiple(a, x, y):
    return divisible(a, x + y)

'''
    10. Given the coefficients of a polynomial of degree two, evaluate the polynomial at a given value.
'''

def evaluate(a, b, c, x):
    return a*x**2 + b*x + c 

'''
    11. Given the coefficients of a polynomial of degree two, calculate the linear coefficient of the derivative.
'''

def coefficientLinearDerivate(a):
    return 2 * a

'''
    12. Given the coefficients of a polynomial of degree two and a real number, evaluate the derivative of
    polynomial in that number.
'''

def evaluateDerivate(a, b, x):
    return 2*a*x + b

'''
    13. Given a natural, determine if it is a Fibonacci number or not.
'''

def fibonacciAux(n, a, b):
    if n == a:
        return True
    elif n < a:
        return False
    else:
        return fibonacciAux(n, b, a + b)
    
def fibonacci(n):
    return fibonacciAux(n, 0, 1)