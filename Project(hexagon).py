# ------------------------------------------------------------------------------
# Program Name:    L5Q1.py
# Student Name:	   Olamide Adeniji 
# Question number: 1
# ------------------------------------------------------------------------------
# Program Purpose: The game Ice Breakers. Allows a player to play a round of ice breakers
#                  With either a friend or vs the cpu.
# ------------------------------------------------------------------------------

#   imports functions and methods from graphics file
from graphics import* 

win = None



# ------------------------------------------------------------------------------
# Function purpose: Draws one of the hexagons
# Syntax          : draw_hexa (start)
# Parameter       : start - Point fuction that determins where the hexagon will be drawn
# Return value    : None
# ------------------------------------------------------------------------------

def draw_hexa (start):
    global win
    

    hexa = Polygon (start, Point (start.x+10, start.y-15), Point (start.x+30, start.y-15), Point (start.x+40, start.y), Point (start.x+30, start.y+ 15), Point (start.x+10, start.y+15) )
    hexa.setFill(color_rgb(204, 255, 255))
    hexa.draw(win)
    
    
    


# ------------------------------------------------------------------------------
# Function purpose: Draws the first two columns of the game board using my draw hexa function
# Syntax          : draw_column(start_x, start_y)
# Parameter       : start_x - location of x value of the point where the first hexagon will be drawn
#                   start_y - location of y value of the point where the first hexagon will be drawn
# Return value    : None
# ------------------------------------------------------------------------------


def draw_column(start_x, start_y):
    global win
    
    original_start_xnew = start_x        #start_x is stored in  original_start_x so that it can be used after the loop
    for y in range (7):
        for x in range (2):
            draw_hexa (Point( start_x, start_y))
            start_x += 30
            start_y += 15
        start_x = original_start_xnew 
        

# ------------------------------------------------------------------------------
# Function purpose: draws the game board using my draw_column function
# Syntax          : game_board()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
    


def game_board():
    global win

#   Sets the window dimentions and the name of the window    
    win = GraphWin ( 'Ice Breakers', 350, 350 )
    
    x_value = 10            # x_value is set to a variable so that it can be updated
    for x in range (5):
        draw_column(x_value, 20)
        x_value +=60
   
    
# ------------------------------------------------------------------------------
# Function purpose: None
# Syntax          : game_board()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
                   

def player_1():
    global win
    
    
    player = Circle(Point(30, 110),6)
    player.setFill('red')
    player.draw(win)

# ------------------------------------------------------------------------------
# Function purpose: None
# Syntax          : game_board()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------


def player_2():
    global win
    
    
    player = Circle(Point(300, 125),6)
    player.setFill('green')
    player.draw(win)

















             
game_board() 
player_1()    
player_2()
        
win.getMouse()
win.close()

