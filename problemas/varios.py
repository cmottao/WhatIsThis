'''    
    19. Si en la UN están podando árboles y cada rama tiene P hojas, y a cada árbol le quitaron K
    ramas, ¿cuántos árboles se deben podar para obtener T hojas?.
'''

def podar_arboles(p, k, t):
    return int(t / (p*k)) 

'''
    20. Si un amigo, no tan amigo, me presta K pesos a i pesos de interés diario, ¿cuánto le pagaré
    en una semana si el interés es simple?, ¿y cuánto si el interés es compuesto?.
'''

def interes_simple(k, i):
    return int(k * (1 + (i / 100) * 7)) 

def interes_compuesto(k, i):
    return int(k * (1 + (i / 100)) ** 7) 

'''
    21. Un niño se la pasó jugando con fichas de lego, tenia dos tipos de fichas de lego, fichas de
    cuadros de 1 x 1 (rojas) y fichas de cuadros de 2 x 1 (azules), y le dieron una base de 1 x n
    cuadritos, ¿de cuántas formas distintas puede ubicar las fichas rojas y azules sobre la base?,
    ¿y si le dan una ficha amarilla de 1 x 3?.
'''

def lego_dos(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return lego_dos(n - 1) + lego_dos(n - 2)

def lego_tres(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return lego_tres(n-1) + lego_tres(n-2) + lego_tres(n-3)