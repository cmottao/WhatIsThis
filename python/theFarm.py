'''
    1. If a cow needs M square meters of grass to produce X liters of milk, how many liters of milk are produced 
    on the farm?
'''

def milkProduction(n, m, g, l):
    return (n * m * l) / g 


'''
    2. If 1/3 of the birds on the farm are chickens, and half of the chickens lay 1 egg every 3 days and the 
    other half 1 egg every 5 days, in a month how many eggs do they produce? (1 month ≡ 30 days).
'''

def eggProduction(b):
    return int(b * (8 / 3))


'''
    3. If the scorpions from the farm are sold to China, and there are scorpions of three different sizes: small
    (with a weight of 20 grams), medium (with a weight of 30 grams) and large (with weighing 50 grams), how many 
    kilos of scorpions can be sold without decreasing the population to less than 2/3?
'''

def scorpions(s, m, b):
    return ((s * 0.02) + (m * 0.03) + (b * 0.05)) / 3


'''
    4. The farmer's corral was damaged and he doesn't know whether to re-enclose the corral with wood, wire or 
    put a metal fence. If you are going to fence with wood you should put 4 rows of boards, with rod 8 rows and 
    with wire only 5 rows, he wants to know what is the least expensive for fencing if you know that the barbed 
    wire is worth P per meter, the boards at Q per meter and the rods S per meter. Given the size of the pen and 
    the prices of the elements, what enclosure is the most economical?
'''

def economical(n, m, w, b, r):
    p = 2 * (n + m) 
    wc = 5 * w * p
    bc = 4 * b * p
    rc = 8 * r * p
    if (wc < bc) and (wc < rc):
        return "Wire"
    elif (bc < wc) and (bc < rc):
        return "Board"
    else:
        return "Rod"