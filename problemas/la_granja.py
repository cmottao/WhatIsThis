'''
    1. Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿Cuántos
    litros de leche se producen en la granja?.
'''

def leche_producida(l, c, n, m):
    return l * n * m / c

'''
    2. Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las gallinas ponen 1 huevo
    cada 3 días y la otra mitad 1 huevo cada 5 días, ¿en un mes cuántos huevos producen?
    (1 mes son 30 días).
'''

def huevos(a):
    g = a / 3 
    gt = g / 2 
    gc = g / 2 
    hmt = 10 
    hmc = 6 
    return int((gt * hmt)+(gc * hmc))

'''
    3. Si los escorpiones de la granja se venden a China, y hay escorpiones de tres diferentes tamaños:
    pequeños (con un peso de 20 gramos), medianos (con un peso 30 gramos) y grandes (con un peso de 50 gramos), 
    ¿cuántos kilos de escorpiones se pueden vender sin que decrezca la población a menos de 2/3?.
'''

def escorpiones(p, m, g):
    kp = 0.02 * p 
    km = 0.03 * m
    kg = 0.05 * g
    kgtotal = kp + km + kg 
    return kgtotal / 3 

'''
    4. Al granjero se le dañó el corral y no sabe si volver a cercar el corral con madera, alambre de
    púas o poner reja de metal. Si va a cercar con madera debe poner 4 hileras de tablas, con
    varilla 8 hileras y con alambre solo 5 hileras, él quiere saber que es lo menos costoso para
    cercar si sabe que el alambre de púaas vale P por metro, las tablas a Q por metro y las varillas
    S por metro. Dado el tamañoo del corral y los precios de los elementos, ¿Cuál cerramiento es
    el más económico?.
'''

def economia(n, m, a, t, v):
    per = 2 * (n + m) 
    ca = 5 * a * per 
    ct = 4 * t * per
    cv = 8 * v * per
    if ca < ct and ca < cv:
        return "Alambre"
    elif ct < ca and ct < cv:
        return "Tabla"
    else:
        return "Varilla"