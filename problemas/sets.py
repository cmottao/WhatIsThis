''' 
    35. Union: Calculates the union of the sets in an array and prints it.
'''

def unionSet(a, b):
    a = set(a)
    b = set(b)
    c = []
    for i in a: 
        c.append(i) 
    for i in b:
        if i not in c: 
            c.append(i)
    return c

''' 
    36. Intersection: Calculates the intersection of the sets in an array and prints it.
'''

def intersectionSet(a, b):
    a = set(a)
    b = set(b)
    c = []
    for i in a:
        if i in b: 
            c.append(i)
    return c

'''
    37. Difference: Calculates in an array the difference of the first with the second and prints it.
'''

def differenceSet(a, b):
    a = set(a)
    b = set(b)
    c = []
    for i in a:
        if i not in b: 
            c.append(i)
    return c

'''
    38. Symmetric difference: Calculates in an arrangement the symmetric difference of the sets and 
    the prints it.
'''

def symmetricDifferenceSet(a, b): 
    return unionSet(differenceSet(a, b), differenceSet(b, a))

'''
    39. Belongs: Reads an integer and determines whether or not the element belongs to each of the
    sets and prints it.
'''

def belongs(a, n):
    a = set(a)
    s = False 
    for x in a:
        s = s or (x == n)
    return s

'''
    40. Content: Determines if the first array is contained in the second and prints it.    
'''

def content(a, b):
    return intersectionSet(a, b) == a 