def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    i = exp
    result = base
  
    while i >= 0:
        i -= 1
        if exp == 0 and base != 0:
            result = 1
            break
        elif i == 0:
            break
        else:
            result = base * result
           
      
    return result
