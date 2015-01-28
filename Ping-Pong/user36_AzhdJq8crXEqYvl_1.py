# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
score1=0
score2=0
ball_vel = [0,0]
veloc = 1
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    r = random.randrange(1,3)
    if(r==1):
        veloc = -1*(random.randrange(50,180))
    else:
        veloc =(random.randrange(50,180))
    ball_vel = [veloc/60.0,  veloc / 60.0]
    if(not direction):
        ball_vel[0] = -ball_vel[0]
    print ball_vel
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2,veloc  # these are ints
    #ball_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_pos = [0,HEIGHT/2]
    paddle2_pos = [WIDTH,HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    score1=0
    score2=0
    

    spawn_ball(True)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 2, "Yellow")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 2, "Yellow")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 2, "Yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos[1]-PAD_HEIGHT/2) >=0)  :
        paddle1_pos[1] += paddle1_vel
    else:
        paddle1_pos[1] = PAD_HEIGHT/2 +1
    if ((paddle1_pos[1]+PAD_HEIGHT/2) <= HEIGHT ) :
        paddle1_pos[1] += paddle1_vel
    else:
        paddle1_pos[1] =HEIGHT- PAD_HEIGHT/2
    if ((paddle2_pos[1]-PAD_HEIGHT/2) >=0)  :
        paddle2_pos[1] += paddle2_vel
    else:
        paddle2_pos[1] = PAD_HEIGHT/2 +1
    if ((paddle2_pos[1]+PAD_HEIGHT/2) <= HEIGHT ) :
        paddle2_pos[1] += paddle2_vel
    else:
        paddle2_pos[1] =HEIGHT- PAD_HEIGHT/2
        
    # paddle1 draw
    #paddle1_pos = [0,HEIGHT/2]
    paddle1_pos_side1 = [paddle1_pos[0],paddle1_pos[1]-PAD_HEIGHT/2]
    paddle1_pos_side2 =	[paddle1_pos[0],paddle1_pos[1]+PAD_HEIGHT/2]
    
    #canvas.draw_line([0,paddle1_pos_side1[1]],[PAD_WIDTH,paddle1_pos_side1[1]], 3, "White")
    #canvas.draw_line([0,paddle1_pos_side2[1]],[PAD_WIDTH,paddle1_pos_side2[1]], 3, "White")
    canvas.draw_polygon([(0,paddle1_pos_side1[1]), (PAD_WIDTH,paddle1_pos_side1[1]), (PAD_WIDTH,paddle1_pos_side2[1]),(0,paddle1_pos_side2[1])], 5, 'Red', 'Red')
    #paddle2 draw
    #paddle2_pos = [WIDTH,HEIGHT/2]
    paddle2_pos_side1 = [paddle2_pos[0],paddle2_pos[1]-PAD_HEIGHT/2]
    paddle2_pos_side2 =	[paddle2_pos[0],paddle2_pos[1]+PAD_HEIGHT/2]
    
    #canvas.draw_line([WIDTH-PAD_WIDTH,paddle2_pos_side1[1]],[WIDTH,paddle2_pos_side1[1]], 3, "White")
    #canvas.draw_line([WIDTH-PAD_WIDTH,paddle2_pos_side2[1]],[WIDTH,paddle2_pos_side2[1]], 3, "White")
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,paddle2_pos_side1[1]), (WIDTH,paddle2_pos_side1[1]), (WIDTH,paddle2_pos_side2[1]),(WIDTH-PAD_WIDTH,paddle2_pos_side2[1])], 5, 'Blue', 'Blue')
       
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] <= (BALL_RADIUS+PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos_side1[1]) and (ball_pos[1] <= paddle1_pos_side2[1]) :
            ball_vel[0] = - ball_vel[0]
            print ball_vel[0]
        else:
            score2 += 1
            spawn_ball(True)
    if ball_pos[0] >= (WIDTH-PAD_WIDTH-BALL_RADIUS):
        if (ball_pos[1] >= paddle2_pos_side1[1]) and (ball_pos[1] <= paddle2_pos_side2[1]) :
            
            if ball_vel[0] <=20 and ball_vel[0]>= -20:
                ball_vel[0] = - 1.2*ball_vel[0]
            print ball_vel[0]
        else:
            score1 +=1
            spawn_ball(False)

    
    # upper and lower wall    
    if ball_pos[1] <= (BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]        
    
    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
   
    # draw scores
    canvas.draw_text(str(score1),[100,150],50,'Red')
    canvas.draw_text(str(score2),[450,150],50,'Blue')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 4
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel= 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel =0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

        
def reset():
    #global paddle1_vel, paddle2_vel
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('New Game',new_game,100)
frame.add_button('Reset',reset,100)

# start frame
new_game()
frame.start()
