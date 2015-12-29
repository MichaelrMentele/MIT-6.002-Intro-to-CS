def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #make copy of all lower case letters
    result = 'abcdefghijklmnopqrstuvwxyz'
    
    #for each char in the alphabet check if it has been guessed
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in lettersGuessed:
            result = result.replace(char, '')
    
    return result
