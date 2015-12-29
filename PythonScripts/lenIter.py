def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    assert type(aStr) == str
    for char in aStr:
        count += 1
    return count

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])
