'''
    The farm.
'''

def floor(x):
    if (x < 0) and (x != int(x)):
        return int(x) - 1
    else:
        return int(x)