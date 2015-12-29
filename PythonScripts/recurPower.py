def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    res = base
    if exp == 0:
        return 1
    else:    
        return res * recurPower(res, exp - 1)


def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^EXP
    '''
    
    if exp == 0:
        return 1
        
    elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base * base, exp/2)
    elif exp > 0 and exp % 2 == 1:
        return base * recurPowerNew(base, exp - 1)