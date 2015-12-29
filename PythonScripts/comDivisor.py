def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b < a:
        mini = b
    else:
        mini = a
        
    while mini > 1:
        if a % mini == 0 and b % mini == 0:
            break
        else: 
            mini -= 1
        
            
    return mini
        
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
