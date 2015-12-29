def myLog(x,b):
    '''
    Compute the logarithm of a number x relative to a base b. 
    Return the largest power of b such that it is still less than or equal to x.

    Assume x and b are positive and b is >= 2.
    
    Return an integer.
    '''
    
    #check initial conditions    
    if x == b:
        return 1
    elif x < b:
        return 0
    #if x is > b then the ans must be at least 1
    else:
        ans = 1
    
    n = 0
    #perform b^n+1 steps and then return b^n
    while True:
        if ans > x:
            return n-1
        else:
            ans *= b
            n += 1
        
    
def laceStrings(s1, s2):
    '''
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    '''
    
    len1 = len(s1)
    len2 = len(s2) 
    
    if len2 < len1:
        end = s1[(len(s2)):]
        small = s2
       
    elif len2 > len1:
        end = s2[len1:]
        small = s1
        
    else:
        end = ''
        small = s1
    
    new = ''
    for index in range(len(small)):
        new += s1[index] + s2[index]
            
    return new + end
    
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0] + s2[0] + helpLaceStrings(s1[1:],s2[1:], out)
    return helpLaceStrings(s1, s2, '')

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
   
    while n > 0: 
        if n >= 6 and n % 3 == 0:
            return True
        elif (n - 26) >= 0  and (n - 26) % 3 == 0:
            return True
        else: 
            n -= 20
                
    return False 
    
    #6, 9, 12, 15, 18, 20, 21, 24, 26, 27, 30 
    
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def sqrt1(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)
    
def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt2(a):
    return fixedPoint(babylon(a), 0.0001)




    

