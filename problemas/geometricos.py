'''
    14. Dadas la pendiente y el punto de corte de dos rectas, determinar si son paralelas, perpendiculares
    o ninguna de las anteriores.    
'''

def rectas(m1, m2, b1, b2):
    if m1 == m2 and b1 != b2: 
        return "Paralelas"
    elif m1 * m2 == -1: 
        return "Perpendiculares"
    else:
        return "Ninguna"

'''
    15. Dadas la pendiente y el punto de corte de dos rectas, determinar los puntos de intersección al origen.
'''

def punto_interseccion(m1, m2, b1, b2):
    x = (b2-b1) / (m1-m2)
    if m1 != m2:
        return (x, b1 + m1*x)
    else:
        return None

'''
    16. Dado el radio de un círculo, calcular el área del triángulo que circunscribe el circulo (triangulo afuera).
'''

def area_triangulo(r):
    base = r * 4
    altura = r * 12**0.5
    return (base*altura) / 2

'''
    17. Dado el radio de un círculo, calcular el área y perímetro del cuadrado, pentágono y hexágono
    adentro (inscrito en un círculo) y afuera (inscribiendo al círculo).
'''

def per_cua_adentro(r):
    l = r * (2**0.5)
    return l * 4

def area_cua_adentro(r):
    l = r * (2**0.5)
    return l ** 2

def per_cua_afuera(r):
    l = r * 2
    return l * 4

def area_cua_afuera(r):
    l = r * 2
    return l ** 2

def per_pen_adentro(r):
    k = r / 4
    l = k * 2 * (10-2*(5**0.5))**0.5 
    return l * 5

def area_pen_adentro(r):
    k = r / 4
    apo = k * ((5**0.5)+1)
    return per_pen_adentro(r) * apo / 2

def per_pen_afuera(r):
    k = r / ((5**0.5)+1)
    l = k * 2 * (10-2*(5**0.5))**0.5
    return l * 5

def area_pen_afuera(r):
    apo = r
    return per_pen_afuera(r) * apo / 2

def per_hex_adentro(r):
    l = r
    return l * 6

def area_hex_adentro(r):
    k = r / 2
    apo = k * (3**0.5)
    return per_hex_adentro(r) * apo / 2

def per_hex_afuera(r):
    k = r / (3**0.5)
    l = k * 2
    return l * 6

def area_hex_afuera(r):
    apo = r
    return per_hex_afuera(r) * apo / 2

'''     
    18. Si una araña utiliza un patrón de hexágono regular para su telaraña, y cada hexágono está
    separado del otro por 1cm, y la araña quiere hacer una telaraña de pir2, ¿Qué cantidad de
    telaraña requiere la araña?
'''

def telaraña(r):
    return 6*r + 3*r*(r+1)