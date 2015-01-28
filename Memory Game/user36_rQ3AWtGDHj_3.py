# implementation of card game - Memory

import simplegui
import random
turns =0
numbers_list =[]
state =0
exposed= []

# helper function to initialize globals
def new_game():
    global turns,numbers_list,exposed
    global state
    state = 0
    exposed = []
    l1 = [0,1,2,3,4,5,6,7]
    numbers_list = l1+l1
    turns = 0
    label.set_text("Turns = "  + str(turns))
    #for x in range(1,9):
     #   numbers_list.append(random.randint(0,9))
    random.shuffle(numbers_list)
    print numbers_list
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turns , numbers_list , exposed, state
    turns +=1
    label.set_text("Turns = "  + str(turns))
    card_no = pos[0]/50
    
    print pos[0]/50
    if not(card_no in exposed):
        if state == 0:
            exposed.append(card_no)
            state = 1
        elif state == 1:
            exposed.append(card_no)
            state = 2
            if numbers_list[exposed[-1]] == numbers_list[exposed[-2]] :
                state = 0
        else:
            exposed.pop()
            exposed.pop()
            exposed.append(card_no)
            state = 1
    print exposed                    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers_list,exposed
    #print numbers_list
    for x in range(16):
        #print numbers_list[x-1]
        canvas.draw_line((50*x,0 ), (50*x,100),2, 'Red')
        if not(x==16):
            if x in exposed:
                num = str(numbers_list[x])
                canvas.draw_text(num,(50*x+10,60),40,"Red")
            else:
                canvas.draw_polygon([(50*x,0 ),(50*x+49,0), (50*x+49,100),(50*x,100)],2, 'Yellow','Green')
                

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+ str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric