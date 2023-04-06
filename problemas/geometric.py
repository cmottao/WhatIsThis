'''
    14. Given the slope and the point of intersection of two lines, determine if they are parallel, 
    perpendicular or none of the above.
'''

def lines(m1, m2, b1, b2):
    if m1 == m2 and b1 != b2: 
        return "Parallel"
    elif m1 * m2 == -1: 
        return "Perpendicular"
    else:
        return "Neither"

'''
    15. Given the slope and the point of intersection of two lines, determine the points of intersection 
    at origin.
'''

def intersectionPoint(m1, m2, b1, b2):
    x = (b2 - b1) / (m1 - m2)
    if m1 != m2:
        return (x, b1 + m1 * x)
    else:
        return None

'''
    16. Given the radius of a circle, calculate the area of the triangle that circumscribes the circle 
    (triangle outside).
'''

def areaTriangle(r):
    b = r * 4
    h = r * 12**0.5
    return (b * h) / 2

'''
    17. Given the radius of a circle, calculate the area and perimeter of the square, pentagon, and 
    hexagon inside (inscribed in a circle) and outside (inscribed in the circle).
'''

def squarePerimeterInside(r):
    l = r * (2**0.5)
    return l * 4

def squareAreaInside(r):
    l = r * (2**0.5)
    return l ** 2

def squarePerimeterOutside(r):
    l = r * 2
    return l * 4

def squareAreaOutside(r):
    l = r * 2
    return l ** 2

def pentagonPerimeterInside(r):
    k = r / 4
    l = k * 2 * (10-2*(5**0.5))**0.5 
    return l * 5

def pentagonAreaInside(r):
    k = r / 4
    apo = k * ((5**0.5)+1)
    return (pentagonPerimeterInside(r) * apo) / 2

def pentagonPerimeterOutside(r):
    k = r / ((5**0.5)+1)
    l = k * 2 * (10-2*(5**0.5))**0.5
    return l * 5

def pentagonAreaOutside(r):
    apo = r
    return (pentagonPerimeterOutside(r) * apo) / 2

def hexagonPerimeterInside(r):
    l = r
    return l * 6

def hexagonAreaInside(r):
    k = r / 2
    apo = k * (3**0.5)
    return (hexagonPerimeterInside(r) * apo) / 2

def hexagonPerimeterOutside(r):
    k = r / (3**0.5)
    l = k * 2
    return l * 6

def hexagonAreaOutside(r):
    apo = r
    return (hexagonPerimeterOutside(r) * apo) / 2

'''     
    18. If a spider uses a regular hexagon pattern for its cobweb, and each hexagon is separated from 
    the other by 1cm, and the spider wants to make a web of πr2, how much cobweb does the spider require?
'''

def cobweb(r):
    return 6*r + (3*r*(r + 1))