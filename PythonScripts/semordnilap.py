def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    n2 = len(str2) 
    n1 = len(str1)
    
    #if the length is zero then they aren't right either
    if n1 == '' or n2 == '':
        return False
    
    #If the end of str1 matches begining of string 2 proceed
    elif str1[n2-1] == str2[0]:
        #if this is the last letter then your done and its a semordnilap
        if n1 == 1 and n2 == 1:
            return True
        #if its not the last letter than redo but pick off the last and the first letter of each str respectively
        elif n1 == n2:
            return semordnilap(str1[:n1-1],str2[1:n2])
        else: 
            return False
    else:
        return False

semordnilapWrapper('abc', 'cba')
