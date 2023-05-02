'''    
    19. If in the UN they are pruning trees and each branch has P leaves, and they removed K from 
    each tree branches, how many trees must be pruned to obtain T leaves?
'''

def treeTriming(p, k, t):
    return int(t / (p * k)) 

'''
    20. If a friend, not such a friend, lends me K pesos at i pesos of daily interest, how much 
    will I pay him? in a week if the interest is simple? And how much if the interest is compound?
'''

def simpleInterest(k, i):
    return k * (1 + (i / 100) * 7)

def compoundInterest(k, i):
    return k * (1 + (i / 100)) ** 7 

'''
    21. A child spent his time playing with lego tiles, he had two types of lego tiles, 1 × 1 
    squares (red) and 2 × 1 square tiles (blue), and given a base of 1 × n little squares, in 
    how many different ways can you place the red and blue tiles on the base? What if they 
    give you a yellow 1 × 3 tile?
'''

def twoLego(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return twoLego(n - 1) + twoLego(n - 2)

def threeLego(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return threeLego(n - 1) + threeLego(n - 2) + threeLego(n - 3)