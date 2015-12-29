def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    done = len(secretWord)
    
    for char in secretWord:
        if char in lettersGuessed:
            count += 1   
            if count == done:
                return True
        else:
            return False
   
