'''
    Useful functions.
'''

def arr(n):
    return [0] * n

def gcd(a, b): 
    if b > a: 
        return gcd(b, a)
    elif a % b == 0:
        return b 
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return int((a * b) / gcd(a, b)) 


'''
    23. Develop an algorithm that calculates the sum of the elements of an array of real numbers.
'''

def sumArray(a):
    s = 0 
    for x in a: 
        s += x
    return s


'''
    24. Develop an algorithm that calculates the average of the elements of an array of real numbers.
'''

def averageArray(a):
    n = len(a)
    return sumArray(a) / n


'''
    25. Develop an algorithm that calculates the dot product of two arrays of real numbers of equal size.
'''

def dotProduct(v, w):
    n = len(v)
    s = 0 
    for i in range(n):
        s += v[i] * w[i]
    return s


'''
    26. Develop an algorithm that calculates the minimum of an array of real numbers.
'''

def minArrayAux(a, n):
    if n == 1:
        return a[0] 
    else:
        return min(a[n - 1], minArrayAux(a, n - 1)) 

def minArray(a):
    return minArrayAux(a, len(a))


'''
    27. Develop an algorithm that calculates the maximum of an array of real numbers.
'''

def maxArrayAux(a, n):
    if n == 1:
        return a[0] 
    else:
        return max(a[n - 1], maxArrayAux(a, n - 1)) 

def maxArray(a):
    return maxArrayAux(a, len(a))


'''
    28. Develop an algorithm that calculates the direct product of two arrays of real numbers of same size. 
'''

def directProduct(v, w):   
    n = len(v)
    u = arr(n)
    for i in range(n):
        u[i] = v[i] * w[i]
    return u


'''
    29. Develop an algorithm that determines the median of an array of real numbers. The median is the 
    number that remains in the middle of the array after being sorted.
'''

def medianArray(a):
    n = len(a)
    a.sort() 
    if n % 2 != 0: 
        return a[n // 2]
    else: 
        return (a[n // 2] + a[n // 2 - 1]) / 2
    

'''
    30. Make an algorithm that counts all the zeros that appeared in said array.
'''
   
def countZeros(a): 
    n = len(a)
    s = 0
    for i in range(n):
        if a[i] == 0:
            s += 1
    return s


''' 
    31. Suppose that an array of integers is full of 1's and 0's and that the array represents a backwards 
    binary number. Make an algorithm that calculates the numbers in decimal that represents said array of 
    ones and zeros.
'''

def binaryToDecimal(a):
    n = len(a)
    s = 0 
    for i in range(n):
        s += a[i] * (2 ** i)
    return s


''' 
    32. Make an algorithm that, given a nonnegative integer, creates an array of ones and zeros which 
    represents the number in binary backwards.
'''

def decimalToBinary(n):
    if n < 2:
        return [n] 
    else:
        return [n % 2] + decimalToBinary(n // 2)
    

'''
    33. Make an algorithm that calculates the Greatest Common Divisor (GCD) for an array of integers positives.
'''

def gcdArrayAux(a, n):
    if n == 1:
        return a[0] 
    else:
        return gcd(a[n - 1], gcdArrayAux(a, n - 1))

def gcdArray(a):
    return gcdArray(a, len(a)) 


''' 
    34. Make an algorithm that calculates the Least Common Multiple (LCM) for an array of integers positives.
'''

def lcmArrayAux(a, n):
    if n == 1:
        return a[0] 
    else: 
        return lcm(a[n - 1], lcmArrayAux(a, n - 1)) 

def lcmArray(a):
    return lcmArrayAux(a, len(a))