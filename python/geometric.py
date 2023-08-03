'''
    Useful functions.
'''

def sqrt(n):
    return n ** 0.5


'''
    14. Given the slope and the point of intersection of two lines, determine if they are parallel, 
    perpendicular or none of the above.
'''

def lines(m1, m2, b1, b2):
    if (m1 == m2) and (b1 != b2): 
        return "Parallel"
    elif m1 * m2 == -1: 
        return "Perpendicular"
    else:
        return "Neither"
    

'''
    15. Given the slope and the point of intersection at the origin of two lines, determine the point of 
    intersection beetwen the lines.
'''

def intersectionPoint(m1, m2, b1, b2):
    x = (b2 - b1) / (m1 - m2)
    if m1 != m2:
        return (x, (m1 * x) + b1)
    else:
        return None
    

'''
    16. Given the radius of a circle, calculate the area of the triangle that circumscribes the circle 
    (triangle outside).
'''

def triangleArea(r):
    return 3 * sqrt(3) * (r ** 2)


'''
    17. Given the radius of a circle, calculate the area and perimeter of the square inside (inscribed in a 
    circle) and outside (inscribed in the circle).
'''

def squarePerimeterInside(r):
    return 4 * sqrt(2) * r

def squareAreaInside(r):
    return 2 * (r ** 2)

def squarePerimeterOutside(r):
    return 8 * r

def squareAreaOutside(r):
    return 4 * (r ** 2)


'''     
    18. If a spider uses a regular hexagon pattern for its cobweb, and each hexagon is separated from the other 
    by 1cm, and the spider wants to make a web of πr2, how much cobweb does the spider require?
'''

def cobweb(r):
    return (6 * r) + (3 * r * (r + 1))