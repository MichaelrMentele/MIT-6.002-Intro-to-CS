# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

import os.path
WORDLIST_FILENAME = os.path.join(os.path.dirname(__file__), "words.txt")

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
   




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ''
    
    for char in secretWord:
        if char in lettersGuessed:
             guess += char
        else:
             guess += ' _ '

    return guess


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

    

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    #print 'Welcome to Hangman, do you think you can beat a super genius computer like me?'
    #print 'The secret word is ' + str(len(secretWord)) +' letters long...'
    
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' +  str(len(secretWord)) + ' letters long'
    print '-----------'
    
    count = 8
    lettersGuessed = ''
    a= 0
    
    while True: 
        
        #Guesses left  
        print 'You have ' + str(count) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        
        #get Guess
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
            a = 1
            print '-----------'
        lettersGuessed += guess   
        
            
        
        #Guess cases
        if guess in secretWord and a == 0:
            print 'Good Guess: ' + str(getGuessedWord(secretWord, lettersGuessed))#'Lucky guess... you bum!'
            print '-----------'
            #Continue or game over?
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
                break
        elif a == 0: 
            print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed))
            
            print '-----------'
        
            count -= 1
            if count <= 0:
                print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) +'.' 
                break
                      
        a = 0
        
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
