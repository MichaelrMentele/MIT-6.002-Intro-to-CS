def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    n = int(len(aStr)/2)
    
    
    if aStr == '':
        return False
    elif aStr[n] == char:
        return True
    elif aStr[n] > char:
        return isIn(char, aStr[:n])
    elif aStr[n] < char:
        return isIn(char, aStr[n+1:])
    else:
        return 'Uh-Oh'
isIn('t', 'abc')
  