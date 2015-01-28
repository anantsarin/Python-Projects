# template for "Stopwatch: The Game"
import simplegui
# define global variables
minute = 0
sec = 0
milisec = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    

def reset():
    global minute , sec , milisec
    minute = 0
    sec = 0
    milisec = 0
    timer.stop()

    

# define event handler for timer with 0.1 sec interval
def handle_timer():
    global minute , sec , milisec
    if milisec == 9:
        milisec = 0
        if sec == 59:
            sec = 0
            minute += 1 
        else:
            sec += 1
    else:
        milisec += 1

# define draw handler
#
def draw(canvas):
    global minute , sec , milisec
    str_min = str(minute/10)+str(minute%10)
    str_sec = str(sec/10)+str(sec%10)
    str_milisec = str(milisec)
    time = str_min + ':'+str_sec+'.'+str_milisec
    #print time
    canvas.draw_text(time, (50,100), 36, "Red")
    
    
    
# create frame
f = simplegui.create_frame('stopwatch',200,200)
f.add_button('start',start,200)
f.add_button('stop',stop,200)
f.add_button('Reset',reset,200)
timer = simplegui.create_timer(100,handle_timer)
f.set_draw_handler(draw)
# register event handlers


# start frame
f.start()

# Please remember to review the grading rubric
