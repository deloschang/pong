# an Atari pong game in Python with cool features

from graphics import *
from sys import exit
from random import uniform

# Player Scores
p1score = 0
p2score = 0

# Paddle 1 Coordinates
y1 = 100   # changes with Paddle 1's movement
X1 = -15     
W1 = 30    
H1 = 90  

# Paddle 2 Coordinates
y2 = 100   # changes with Paddle 2's movement
X2 = 385   
W2 = 30    
H2 = 90  

# Starting Paddle Y coordinates
ORIGY1 = y1
ORIGY2 = y2

# Starting Paddle speed
ORIG_PADDLE_SPEED = 15

# In-game Paddle Speed
paddle_speed = ORIG_PADDLE_SPEED

# Ball Coordinates
y3 = 200
x3 = 200
R3 = 10

# Starting Ball coordinates
ORIGX3 = x3
ORIGY3 = y3

# Starting Ball Velocity
BALL_X = 6
BALL_Y = 2.5

# Ball Velocity 
ball_x = BALL_X
ball_y = BALL_Y

# Expands ball erasing radius
ERASE_CONSTANT = 0.7

# random accelerating obstacle coordinates
rand_obstacle_accelerate_x = uniform(50, 350)
rand_obstacle_accelerate_y = uniform(50, 350)

# random teleportation obstacle coordinates
rand_obstacle_teleport_x = uniform(50, 350)
rand_obstacle_teleport_y = uniform(50, 350)

# random obstacle coordinates that reverse the paddle hotkeys
rand_obstacle_reverse_x = uniform(50, 350)
rand_obstacle_reverse_y = uniform(50, 350)

# random obstacle that makes the ball superman (very high y)
rand_obstacle_superman_x = uniform(50, 350)
rand_obstacle_superman_y = uniform(50, 350)

# Initializes reversed paddle hotkeys
reverse_switch = False

# Initializes game
set_game = False

# Initializes ball movement
set_ball_go = False

# switch to add score when player wins
add_p1_score = False
add_p2_score = False

disable_stroke()
set_clear_color(1, 1, 1) # white
set_fill_color(0, 0, 0) # black

def left_paddle_move_down():
    global y1, ball_y, ball_x
    if(is_key_pressed("z")):
        if reverse_switch == False:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X1, y1, W1, H1) # erases paddles
        
            y1 += paddle_speed
        
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X1, y1, W1, H1) # redraws new paddle
            
            if bounce_zone(x3, y3, X1, y1, W1, H1):
                ball_y += 1
                ball_x += 0.5
        
        # reversed paddle direction because of obstacle
        if reverse_switch == True:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X1, y1, W1, H1) # erases paddles
            
            y1 -= paddle_speed
            
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X1, y1, W1, H1) # redraws new paddle
                
            if bounce_zone(x3, y3, X1, y1, W1, H1):
                ball_y -= 1
                ball_x += 0.5

def left_paddle_move_up():
    global y1, ball_y, ball_x
    if(is_key_pressed("a")):
        if reverse_switch == False:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X1, y1, W1, H1) # erases paddles
            
            y1 -= paddle_speed
            
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X1, y1, W1, H1) # redraws new paddle
            
            if bounce_zone(x3, y3, X1, y1, W1, H1):
                ball_y -= 1
                ball_x += 0.5
        
        # reversed paddle direction because of obstacle
        if reverse_switch == True:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X1, y1, W1, H1) # erases paddles
        
            y1 += paddle_speed
        
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X1, y1, W1, H1) # redraws new paddle

def right_paddle_move_down():
    global y2, ball_y, ball_x
    if(is_key_pressed("m")):
        if reverse_switch == False:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X2, y2, W2, H2) # erases paddle
        
            y2 += paddle_speed
        
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X2, y2, W2, H2) # redraws new paddle
            
            if bounce_zone(x3, y3, X2, y2, W2, H2):
                ball_y += 1
                ball_x -= 0.5
        
        # reversed paddle dir. because of obstacle
        if reverse_switch == True:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X2, y2, W2, H2) # erases paddle
            
            y2 -= paddle_speed 
            
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X2, y2, W2, H2) # redraws new paddle
            
def right_paddle_move_up():

    global y2, ball_y, ball_x
    if(is_key_pressed("k")):
        if reverse_switch == False:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X2, y2, W2, H2) # erases paddle
            
            y2 -= paddle_speed 
            
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X2, y2, W2, H2) # redraws new paddle
            
            if bounce_zone(x3, y3, X2, y2, W2, H2):
                ball_y -= 1
                ball_x -= 0.5
        
        # reversed paddle dir. because of obstacle
        if reverse_switch == True:
            set_fill_color(1, 1, 1) # white
            draw_rectangle(X2, y2, W2, H2) # erases paddle
        
            y2 += paddle_speed
        
            set_fill_color(0, 0, 0) # black
            draw_rectangle(X2, y2, W2, H2) # redraws new paddlea

def obstacle_accelerate():
    global ball_x, rand_obstacle_accelerate_x, rand_obstacle_accelerate_y

    # sets new random coord for respawning acceleration obstacle
    rand_obstacle_accelerate_new_x = uniform(50, 350)
    rand_obstacle_accelerate_new_y = uniform(50, 350) 

    # draws obstacle
    set_fill_color(1, 0, 0) # red
    draw_rectangle(rand_obstacle_accelerate_x, rand_obstacle_accelerate_y, 25, 25)
    
    set_fill_color(0, 0, 0) # white
    
    # accelerates ball if it touches the square
    if bounce_zone(x3, y3, rand_obstacle_accelerate_x, rand_obstacle_accelerate_y, 25, 25):
        ball_x *= 1.5
        
        # erases ball
        set_fill_color(1, 1, 1) # white
        draw_circle(rand_obstacle_accelerate_x + 12.5, rand_obstacle_accelerate_y + 12.5, 22.5)
        
        # sets new coordinates for obstacle respawn
        rand_obstacle_accelerate_x = rand_obstacle_accelerate_new_x
        rand_obstacle_accelerate_y = rand_obstacle_accelerate_new_y 

def obstacle_teleport():
    global x3, y3, rand_obstacle_teleport_x, rand_obstacle_teleport_y, ball_x, ball_y
    
    # new random coord for respawning teleport obstacle
    rand_obstacle_teleport_new_x = uniform(50, 350)
    rand_obstacle_teleport_new_y = uniform(50, 350)
    
    # ball teleports to these random destination coords
    rand_obstacle_dest_x = uniform(200, 200)
    rand_obstacle_dest_y = uniform(200, 200)
    
    set_fill_color(0, 0, 1) # blue
    draw_rectangle(rand_obstacle_teleport_x, rand_obstacle_teleport_y, 25, 25)
    
    set_fill_color(0, 0 ,0)
    
    # teleports ball if it touches the square
    if bounce_zone(x3, y3, rand_obstacle_teleport_x, rand_obstacle_teleport_y, 25, 25):
        
        # erases ball
        set_fill_color(1, 1, 1) # white
        draw_circle(rand_obstacle_teleport_x + 12.5, rand_obstacle_teleport_y + 12.5, 25)
        
        rand_obstacle_teleport_x = rand_obstacle_teleport_new_x
        rand_obstacle_teleport_y = rand_obstacle_teleport_new_y
        
        # changes ball direction 
        ball_x = -ball_x
        
        # teleports ball
        x3 = rand_obstacle_dest_x 
        y3 = rand_obstacle_dest_y

def obstacle_reverse():
    global rand_obstacle_reverse_x, rand_obstacle_reverse_y, reverse_switch
    
    # sets new random coord for respawning teleport obstacle
    rand_obstacle_reverse_new_x = uniform(50, 350)
    rand_obstacle_reverse_new_y = uniform(50, 350) 
    
    # draws obstacle
    set_fill_color(0, 1, 0) # green
    draw_rectangle(rand_obstacle_reverse_x, rand_obstacle_reverse_y, 25, 25)
    
    set_fill_color(0, 0, 0) # white
    
    # reverses paddle hotkeys if ball touches the square
    if bounce_zone(x3, y3, rand_obstacle_reverse_x, rand_obstacle_reverse_y, 25, 25):
        
        if reverse_switch == False:
            reverse_switch = True
        
        else:
            reverse_switch = False
        
        # erases ball
        set_fill_color(1, 1, 1) # white
        draw_circle(rand_obstacle_reverse_x + 12.5, rand_obstacle_reverse_y + 12.5, 22.5)
        
        rand_obstacle_reverse_x = rand_obstacle_reverse_new_x
        rand_obstacle_reverse_y = rand_obstacle_reverse_new_y

def obstacle_superman():
    global ball_x, ball_y, n, rand_obstacle_superman_x, rand_obstacle_superman_y
    
    # new random coord for respawning superman obstacle
    rand_obstacle_superman_new_x = uniform(50, 350)
    rand_obstacle_superman_new_y = uniform(50, 350)
    
    # random superman speed
    rand_obstacle_superman_speed_x = uniform(-5, 5)
    rand_obstacle_superman_speed_y = uniform(7, 12)
    
    # draws obstacle
    set_fill_color(1, 1, 0) # yellow
    draw_rectangle(rand_obstacle_superman_x, rand_obstacle_superman_y, 25, 25)
    
    set_fill_color(0, 0, 0)
     
    if bounce_zone(x3, y3, rand_obstacle_superman_x, rand_obstacle_superman_y, 25, 25):
    
        ball_x = rand_obstacle_superman_speed_x
        ball_y = rand_obstacle_superman_speed_y
                    
        # erases ball
        set_fill_color(1, 1, 1) # white
        draw_circle(rand_obstacle_superman_x + 12.5, rand_obstacle_superman_y + 12.5, 22.5)

        # blip of color
        set_fill_color(0, 1, 0)

        rand_obstacle_superman_x = rand_obstacle_superman_new_x
        rand_obstacle_superman_y = rand_obstacle_superman_new_y 

def bounce_zone(x, y, rx, ry, rw, rh):
    return x > rx and x < rx + rw and y > ry and y < ry + rh

def draw_frame():
    global set_game, set_ball_go, y1, y2, x3, y3, ball_x, ball_y, p1score, p2score, add_p1_score, add_p2_score, rand_obstacle_teleport_x, rand_obstacle_teleport_y, rand_obstacle_accelerate_x, rand_obstacle_accelerate_y, reverse_switch, paddle_speed

    # random ball velocity for Unpredictable Bouncing
    rand_ball_x = uniform (-0.5, 0.5)
    rand_ball_y = uniform (-0.5, 0.5)
    rand_paddle_x = uniform (-0.2, 0.2)
    rand_paddle_y = uniform (-0.2, 0.2)
    
    # draws starting message
    if set_game == False:
        draw_string("Press 'r' to start", 50, 50, scale = 1.0)
        draw_string("Red = Accelerate", 50, 75, scale = 0.8)
        draw_string("Blue = Teleport", 50, 90, scale = 0.8)
        draw_string("Green = Reverses Paddle Dir.", 50, 105, scale = 0.8)
        draw_string("Yellow = Superman", 50, 120, scale = 0.8)
        set_game = True
    
    # draws scoreboard
    draw_string("P1: " + str(p1score), 50, 350, scale = 1.0)
    draw_string("P2: " + str(p2score), 300, 350, scale = 1.0)
    
    # draws obstacle that accelerates the ball
    obstacle_accelerate()
        
    # draws obstacle that teleports the ball
    obstacle_teleport()
    
    # draws obstacle that reverses the paddle hotkeys
    obstacle_reverse()
    
    # draws obstacle that makes ball superman
    obstacle_superman()  
    
    # reset hotkey
    if(is_key_pressed("r")):
        clear()
    
        # resets original coordinates  
        y1 = ORIGY1
        y2 = ORIGY2
        x3 = ORIGX3
        y3 = ORIGY3
        
        # resets orig. ball velocity
        ball_x = BALL_X
        ball_y = BALL_Y
        
        # resets orig. paddle speed
        paddle_speed = ORIG_PADDLE_SPEED
       
        set_fill_color(0, 0, 0) # black

        draw_rectangle(X1, y1, W1, H1) # draws paddle 1
        draw_rectangle(X2, y2, W2, H2) # draws paddle 2
        
        draw_circle(x3, y3, R3) # draws ball
        
        set_ball_go = True
        
        # resets paddles to original direction
        reverse_switch = False
        
        # if P1 scores, add a point
        if add_p1_score == True:
            p1score += 1 
            add_p1_score = False
        
        # if P2 scores, add a point
        if add_p2_score == True:
            p2score += 1
            add_p2_score = False
        
        
    # left paddle movement  
    if y1 == 10 - paddle_speed: # paddle at top
        if reverse_switch == False:
            left_paddle_move_down()
        
        if reverse_switch == True:
            left_paddle_move_up() 
        
        draw_rectangle(X1, y1, W1, H1) # redraws paddle; shows where ball hits paddle
        
    if y1 == (400 - H1): # paddle at bottom
        if reverse_switch == False:
            left_paddle_move_up()

        if reverse_switch == True:
            left_paddle_move_down()

        draw_rectangle(X1, y1, W1, H1)
                
    if y1 < (400 - H1) and y1 > 0: # general movement
        left_paddle_move_down()
        left_paddle_move_up()
        draw_rectangle(X1, y1, W1, H1)
            
    # right paddle movement
    if y2 == 10 - paddle_speed: # paddle at top
        if reverse_switch == False:
            right_paddle_move_down()
            
        if reverse_switch == True:
            right_paddle_move_up()

        draw_rectangle(X2, y2, W2, H2)
        
    if y2 == (400 - H2): # paddle at bottom
        if reverse_switch == False:
            right_paddle_move_up()

        if reverse_switch == True:
            right_paddle_move_down()

        draw_rectangle(X2, y2, W2, H2)
    
    if y2 < (400 - H2) and y2 > 0: # general movement
        right_paddle_move_down()
        right_paddle_move_up()
        draw_rectangle(X2, y2, W2, H2)

    # draws ball movement
    if set_ball_go == True and x3 > 7 and x3 < 393: 
        set_fill_color(1, 1, 1) # white
        draw_circle(x3, y3, R3 + ERASE_CONSTANT) # erases ball
            
        # moves ball
        x3 += ball_x 
        y3 += ball_y
        
        set_fill_color(0, 0, 0) # black
        draw_circle(x3, y3, R3) # redraws ball

    # bounces off top wall
    if bounce_zone(x3, y3, 0, -20, 400, 30):
        ball_y = -ball_y - rand_ball_y
        ball_x += rand_ball_x + rand_ball_x

    # bounces off bottom wall
    if bounce_zone(x3, y3, 0, 390, 400, 30):
        ball_y = -ball_y - rand_ball_y
        ball_x += rand_ball_x + rand_ball_x
        
    # bounces off paddles
    if bounce_zone(x3, y3, X2, y2, W2, H2) or bounce_zone(x3, y3, X1, y1, W1, H1):
        ball_x = -ball_x + rand_paddle_x
        ball_y += rand_paddle_y
    
    # winning parameters
    if x3 < 7: 
        draw_string("Player 2 Wins!", 200, 200, scale = 1.5)
        draw_string("Press 'r' to reset", 200, 250, scale = 1.0)
        add_p2_score = True
        
    if x3 > 393:
        draw_string("Player 1 Wins!", 200, 200, scale = 1.5)
        draw_string("Press 'r' to reset", 200, 250, scale = 1.0)
        add_p1_score = True 
    
    # quit hotkey
    if(is_key_pressed("q")):
        exit()
            
set_frame_rate(50)   
graphics_window(draw_frame)
