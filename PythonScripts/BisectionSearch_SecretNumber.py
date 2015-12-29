#Bisection Search for Secret number between 1 and 100

#Initialize Vars
start_point = 0
end_point = 100
guess = float()
feedback = str()

#Explanation to user to get started
print 'Please think of a number between 0 and 100!'

#Guess evaluation
while True:
    guess = (end_point + start_point) / 2
    print 'Is your secret number ' + str(int(guess)) + '?'
    feedback = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if feedback == 'c':
        break
    elif feedback == 'l':
        start_point = guess
    elif feedback == 'h':
        end_point = guess
    else:
        print 'Sorry, I did not understand your input.'

#End
print 'Game over. Your secret number was: ' + str(guess) 
