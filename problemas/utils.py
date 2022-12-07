#Numéricos

def mcd(a,b): 
    if b > a: 
        return mcd(b, a)
    elif a % b == 0:
        return b 
    else:
        return mcd(b, a % b)

def mcm(a,b):
    return int((a*b) / mcd(a,b)) 

#Arreglos

def ordenar(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

#Polinomios

def agregar(b,c):
    for i in range(c):
        b.append(0)    
    return b

def igualar(p,q): 
    n = len(p)
    m = len(q)
    if n > m: 
        agregar(q,n-m)
    elif n < m: 
        agregar(p,m-n)

def limpiar_polinomio(p):
    n = len(p)
    while(n > 1 and p[n-1] == 0): 
        p.pop()
        n -= 1
    return p

def dividir_monomios(p,q):
    n = len(p)
    m = len(q)
    if m > n:
        return [0]
    else:
        r = []
        agregar(r,n-m)
        r.append(p[n-1]/q[m-1]) 
        return r

#Matrices 

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

def matriz_por_vector(a,b):
    n = len(a)
    c = []
    for i in range(n):
        s = 0 
        for j in range(n):
            s += a[i][j] * b[j] 
        c.append(s) 
    return c

def matriz_transpuesta(a): 
    n = len(a)
    m = len(a[0])
    b = []
    for i in range(m):
        f = [] 
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

#Relaciones binarias

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