def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    count = 0
    guess = ''
    
    for char in secretWord:
        if char in lettersGuessed:
             guess += char
        else:
             guess += ' _ '

    return guess
            
        