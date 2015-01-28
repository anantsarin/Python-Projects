# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    number =-1
    if name=="rock":
        number = 0 
    elif name=="Spock":
        number= 1
    elif name=="paper":
        number= 2
    elif name=="lizard":
        number = 3
    else:
        number = 4
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
    name =""
    if number == 0:
        name="rock"
         
    elif number== 1:
        name="Spock"
        
    elif number ==2:
        name="paper"
        
    elif number == 3:
        name="lizard"
        
    else:
        name = "scissors"
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
        
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "my choice ="+ player_choice
    # convert the player's choice to player_number using the function 
    num =name_to_number(player_choice)

    # compute random guess for comp_number using 
    ran =random.randrange(0,5)
   # ran = randrange(0,5)
   # print ran
    # convert comp_number to comp_choice using the function 
    com_choice = number_to_name(ran)
    
    print "computer ="+com_choice#comp_name
    # print out the message for computer's choice
    
    # compute difference of comp_number and player_number modulo five
    dif = (num-ran)%5
    #print dif
    if dif==0:
        print "tie"
    elif dif==1 or dif==2:
        print "player wins"
    else:
        print "computer wins"
    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

