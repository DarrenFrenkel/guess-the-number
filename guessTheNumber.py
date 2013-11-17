# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import math
import random
import simpleguitk as simplegui

# initialize global variables used in your code

secret_number = 0
num_range = 0
n = 0



# helper function to start and restart the game
def new_game():
    global secret_number
    global n
    if num_range == 1:
        secret_number = random.randrange(0, 101)
        print ("New Game. Guess a number between 0 & 100." )
        print ("You have 7 guesses")
        #print secret_number  
    elif num_range == 2:
        secret_number = random.randrange(0, 1001)
        print ("New Game. Guess a number between 0 & 1000. You have 10 guesses")
        #print secret_number 
    else:
        secret_number = random.randrange(0, 101)
        print ("New Game. Guess a number between 0 & 100. You have 7 guesses")
        #print secret_number
        n = 7
    # remove this when you add your code
    pass

# define event handlers for control panel
def range100():
    global num_range
    global n
    n = 7
    num_range = 1
    new_game()
    
    # remove this when you add your code    
    pass

def range1000():
    global num_range
    global n
    n = 10
    num_range = 2
    new_game()
    pass
    
    
def input_guess(guess):
    global n
    guess = int(guess)
    n = n - 1
    if n == 0:
        print ("Sorry, you lost the number is " + str(secret_number) + ".")
        new_game()
    else:     
        if guess == secret_number:
            print (str(guess) + " is correct! Congrats,you won")
            new_game()
        elif guess > secret_number:
            print (str(guess) + " is too high, try a lower number") 
            print ("You have " + str(n) + " guesses left")
        else:
            print (str(guess) + " is too low, try a higher number")
            print ("You have " + str(n) + " guesses left")
            
        
    pass

    
# create frame

frame = simplegui.create_frame('guess_the_number', 500, 500,100)


# register event handlers for control elements
frame.add_input("Enter Number", input_guess , 100)
frame.add_button( "0 - 100" , range100, 100)
frame.add_button( "0 - 1000", range1000, 100)


# call new_game and start frame
new_game()
frame.start()





# always remember to check your completed program against the grading rubric







