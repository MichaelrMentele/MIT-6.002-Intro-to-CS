def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    odd = 0
    
    while odd < len(aTup):
        if len(aTup) == 0:
            break
        newTup = newTup + (aTup[odd],)
        odd += 2
    
    return newTup
        
        
