# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



# initialize global variables used in your code
import simplegui
import math
import random

num_range = 100
randi = 0
chances = 7
# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    global randi
    print "start new game"
    print "Num range from 1 to " + str(num_range) 
    randi = random.randint(1,num_range)
    print ""
    


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    # remove this when you add your code
    global num_range , chances 
    num_range = 100
    new_game()
    chances = 7 
    print "chance = " + str(chances)

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range , chances
    num_range = 1000
    new_game()
    chances = 10 
    print "chance = " + str(chances)
    
def input_guess(guess):
    # main game logic goes here	
    global num_range , randi , chances
    print 'Guess is '+guess
    
    g = int(guess)
    if chances >= 0:
        if g > randi:
            print 'lower'
        if g < randi:
            print 'higher'
        if g == randi:
            print 'correct guess'
            chances = 0
        chances -= 1
    print "number of chances left = " + str(chances)
    print ""
        
# create frame

f  = simplegui.create_frame("guess the num",200,200)
f.add_button('range 1-100',range100)
f.add_button('range 1-1000',range1000)
f.add_input('input guess',input_guess,200)
# register event handlers for control elements



# call new_game and start frame
new_game()
f.start()

# always remember to check your completed program against the grading rubric
