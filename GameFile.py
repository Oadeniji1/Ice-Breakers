# ------------------------------------------------------------------------------
# Program Name:    Project(squares).py
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
# Function purpose: Draws one of the squares
# Syntax          : draw_square (start)
# Parameter       : start - Point fuction that determins where the hexagon will be drawn
# Return value    : None
# ------------------------------------------------------------------------------

def draw_square (start):
    global win
    

    square = Rectangle (start, Point (start.x+50, start.y+50))
    square.setFill(color_rgb(204, 255, 255))
    square.draw(win)
    
    
# ------------------------------------------------------------------------------
# Function purpose: draws the game board using my draw_square function
# Syntax          : game_board()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
    
def game_board():
    global win

#   Sets the window dimentions and the name of the window    
    win = GraphWin ( 'Ice Breakers', 500, 400 )

    rec = Rectangle(Point(0,0), Point (500,400))
    rec.setFill('blue')
    rec.draw(win) 

#   the game starts at position 0,0 of the window    
    xstart = 0 
    ystart = 0
    for y in range(7):
        for x in range(10):
            draw_square (Point(xstart,ystart))
            xstart +=50
        xstart = 0
        ystart +=50
        
        
                
# ------------------------------------------------------------------------------
# Function purpose: Draws the player one circle
# Syntax          : player_1()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
                   

def player_1():
    global player_1
    
    
    player_1 = Circle(Point(25, 175),15)
    player_1.setFill('white')
    player_1.draw(win)
    

# ------------------------------------------------------------------------------
# Function purpose: Draws the player two circle
# Syntax          : player_2()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------


def player_2():
    global player_2 
    
    
    player_2 = Circle(Point(475, 175),15)
    player_2.setFill('red')
    player_2.draw(win)
    
    
# ------------------------------------------------------------------------------
# Function purpose: Controls the movements of player one. Checks to see if a player clicking on the game
#                   board is making a legal move before moving the players piece.
# Syntax          : P1_move()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
    
def P1_move():
    
    global player_1, p_text, game_running

#   Check to see if player one has lost the game   
    if check_win() == True:   
        p_col = player_1.getCenter().x // 50  # getting current position of a player before they click
        p_row = player_1.getCenter().y // 50  
        where = win.getMouse()
        col = where.x // 50                   #new position that the player wishes to move to
        row = where.y // 50  
    
#   Check to see if move is valid        
        if valid_p_move(where.x, where.y, col, row, p_col, p_row) == True:      
            player_1.undraw()
            x_pos = (col+ 0.5) * 50
            y_pos = (row + 0.5) * 50
#   Undraws the current circle for the player and replaces it with a new circle when the player moves        
            player_1 = Circle(Point(x_pos, y_pos),15)
            player_1.setFill('white')
            player_1.draw(win)
        
            restore_board('P1')      # restores / opens up the users old position when they move to a new position
            move_rep(col, row, 'P1') # marks down the players position in a list of positions 
        else:
            P1_move()
#   If player is unable to make anymore legal moves then they lose   
    else:
        p_text.setText("Player Two Wins! Click to exit")
        p_text.setFill('red') 
        p_text.setSize(25)
        game_running = False
        
           
# ------------------------------------------------------------------------------
# Function purpose: Controls the movements of player Two. Checks to see if a player clicking on the game
#                   board is making a legal move before moving the players piece.
# Syntax          : P2_move()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
def P2_move():
    
    global player_2, p_text, game_running
#   Check to see if player one has lost the game       
    if check_win() == True:
        p_col = player_2.getCenter().x // 50   # getting current position of a player before they click
        p_row = player_2.getCenter().y // 50       
        where = win.getMouse()
        col = where.x // 50    #new position that the player wishes to move to
        row = where.y // 50  
 #   Check to see if move is valid     
        if valid_p_move(where.x,where.y, col, row, p_col, p_row) == True:        
            player_2.undraw()
            x_pos = (col+ 0.5) * 50
            y_pos = (row + 0.5) * 50
#Undraws the current circle for the player and replaces it with a new circle when the player moves              
            player_2 = Circle(Point(x_pos, y_pos),15)
            player_2.setFill('red')
            player_2.draw(win)
        
            restore_board('P2')   # restores / opens up the users old position when they move to a new position
            move_rep(col, row, 'P2')   # marks down the players position in a list of positions    
        else:
            P2_move()
    #   If player is unable to make anymore legal moves then they lose        
    else:   
        p_text.setText("Player One Wins! Click to exit")
        p_text.setFill('white') 
        p_text.setSize(25)
        game_running = False
  


#-------------------------------------------------------------------------------
# Function purpose: Controls the breaking of ice for a player.
# Syntax          : break_ice()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------
def break_ice():
    where = win.getMouse()
    col = where.x // 50
    row = where.y // 50    
    
    #makes sure that the player is trying to make a legal ice break move
    if valid_w_move(where.x,where.y, col, row) == True:
        x_pos = col * 50
        y_pos = row * 50
        x_pos2 = (col + 1) * 50
        y_pos2 = (row + 1) * 50
    
        water = Rectangle(Point(x_pos, y_pos), Point(x_pos2, y_pos2))
        water.setOutline('blue')
        water.setFill('blue')
        water.draw(win)
        
        water_rep(col, row)
    else:
        break_ice()
    
        
#-------------------------------------------------------------------------------
# Function purpose: Checks to see if a player is attempmting to make an illegal move or not.
# Syntax          : move = valid_p_move(x, y, col, row, p_col, p_row)
# Parameter       : x - the x coordinate of where a player clicks.
#                   y - the y coordinate of where a player clicks.
#                   col - the column position of a click from the user, while attempting to move (0-9).
#                   row - the row position of a click from the user, while attempting to move (0-6).
#                   p_col - the current column position of a user.
#                   p_row - the current row position of a user.
# Return value    : False - if the user fails the tests, and the move is illegal
#                 : True if they pass the tests, and the move is legal
# ------------------------------------------------------------------------------


def valid_p_move(x, y, col, row, p_col, p_row): 
    
    if x > 500 or y > 350:  #  game board dimentions
        return False
    if [col, row] not in board:  #   if the position is available or empty
        return False  
    if p_col < (col - 1) or p_col > (col + 1): # if the players movement is within just one square 'x' portion
        return False
    if p_row <(row - 1) or p_row > (row + 1): # if the players movement is within just one square 'y' portion
        return False    
    else:
        return True # legal move

#-------------------------------------------------------------------------------
# Function purpose: checks to see if the player is making a legal ice break
# Syntax          : ice = valid_w_move(x, y, col, row)
# Parameter       : x - the x coordinate of where a player clicks.
#                   y - the y coordinate of where a player clicks.
#                   col - the column position of a click from the user, while attempting to move (0-9).
#                   row - the row position of a click from the user, while attempting to move (0-6).
# Return value    : False - if the user fails the tests, and the move is illegal
#                 : True if they pass the tests, and the move is legal
# ------------------------------------------------------------------------------


def valid_w_move(x, y, col, row):    
    if x > 500 or y > 350:
        return False
    if [col, row] not in board:
        return False  
    else:
        return True
    
# ------------------------------------------------------------------------------
# Function purpose: controls the main game loop. Keeps calls P1_move and P2_move till someone loses.
#                   also controls the text that is displayed at the bottom of the game board, and ice breaking
# Syntax          : play_game()
# Parameter       : None 
# Return value    : None
#------------------------------------------------------------------------------

def play_game():
    global win, p_text, game_running  
    game_running = True
    player_1()
    player_2()
    

    P_turn('One', 'white')
    
    while game_running:
        P1_move()
        if game_running == True:
            p_text.setText("Player One Break A Piece Of Ice")
            break_ice()
            p_text.setText("Player Two's Move")
            p_text.setFill('red')
            P2_move()
            if game_running == True:
                p_text.setText("Player Two Break A Piece Of Ice")       
                break_ice()
                p_text.setText("Player One's Move")
                p_text.setFill('white')
    win.getMouse()
    win.close()
    

# ------------------------------------------------------------------------------
# Function purpose: Creates the text at the bottom of the game board that helps to 
#                   direct a player on what to do, and whose turn it is
# Syntax          : P_turn(player, color)
# Parameter       : player - player  (One or Two)
#                   color - the color of the text
# Return value    : None
#------------------------------------------------------------------------------
    
    
def P_turn(player, color):
    global win, p_text
       
    p_text = Text(Point(250, 370), "Player "+ player +"'s Move")
    p_text.setFill(color)
    p_text.setSize(16)
    p_text.draw(win) 
    
    
# ------------------------------------------------------------------------------
# Function purpose: Representation of the game board using a list. When a player performs 
#                   an action, it is recorded here
# Syntax          : game_board = board_rep()
# Parameter       : None 
# Return value    : List of the game board positions, player positions, and water positions
# ------------------------------------------------------------------------------

def board_rep():
    global board
    
    board = []
    for y in range (7):
        for x in range (10):
            board.append([x,y]) 
    move_rep(0, 3, 'P1')  
    move_rep(9, 3, 'P2')     
    return board

# ------------------------------------------------------------------------------
# Function purpose: records the players movement in the game board list representation
# Syntax          : move_rep(x_pos, y_pos, player)
# Parameter       : x_pos - x coordinate of the players move
#                   y_pos - y cordinate of the players move
#                   player - which player is making the move (P1 or P2)
# Return value    : None
# ------------------------------------------------------------------------------

temp_board = []

def move_rep(x_pos, y_pos, player):
    global board
    move = [x_pos, y_pos]
    for i in range(len(board)):
        if move == board[i]:
            temp_board.append(board.pop(i))  # puts the players current position into a temporary 
            #board so that it can be added back to the list after the player moves
            board.insert(i , player)
        
# ------------------------------------------------------------------------------
# Function purpose: records the players ice break in the game board list representation
# Syntax          : water_rep(x_pos, y_pos)
# Parameter       : x_pos - x coordinate of the players ice break
#                   y_pos - y cordinate of the players ice break
# Return value    : None
#-------------------------------------------------------------------------------

def water_rep(x_pos, y_pos):
    global board
    move = [x_pos, y_pos]
    for i in range(len(board)):
        if move == board[i]:
            board.pop(i)
            board.insert(i , 'W')        
            
# ------------------------------------------------------------------------------
# Function purpose: restores the list representation of the board, after a player moves from their current position
# Syntax          : restore_board(player)
# Parameter       : player - the player making the move 
# Return value    : None
#-------------------------------------------------------------------------------
        
def restore_board(player):
    global board
    for i in range(len(board)):
        if player == board[i]:
            board.pop(i)
            board.insert(i,temp_board.pop(0))
            
# ------------------------------------------------------------------------------
# Function purpose: Checks to see if a player has won or lost a game
# Syntax          : check_win():
# Parameter       : None
# Return value    : True if the player is unable to move to a legal  position
#                 : False if the player is able to move to legal position
#-------------------------------------------------------------------------------
def check_win():
    current_pos = temp_board[0]
    if [current_pos[0] - 1, current_pos[1] - 1] in board:
        return True 
    if [current_pos[0], current_pos[1] - 1] in board:
        return True     
    if [current_pos[0] + 1, current_pos[1] - 1] in board:
        return True 
    if [current_pos[0] - 1, current_pos[1] ] in board:
        return True  
    if [current_pos[0] + 1, current_pos[1] ] in board:
        return True 
    if [current_pos[0] - 1, current_pos[1] + 1] in board:
        return True 
    if [current_pos[0] , current_pos[1] + 1] in board:
        return True
    if [current_pos[0] + 1, current_pos[1] + 1] in board:
        return True   
    else:
        return False
    
        
#-------------------------------------------------------------------------------
# Function purpose: runs all of the main game functions
# Syntax          : game_exe()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------             
def game_exe():
    game_board() 
    board_rep() 
    play_game()

#-------------------------------------------------------------------------------
# Function purpose: Creates a splash screen for the game, and after the player clicks what type of game 
#                   mode they want to play, it load the game
# Syntax          : start_game()
# Parameter       : None 
# Return value    : None
# ------------------------------------------------------------------------------      
def start_game():
    win = GraphWin ( 'Ice Breakers', 1400, 800 )
    rec = Rectangle(Point(0,0), Point (1400,800))
    rec.setFill('cyan')
    
    screen = Image(Point(700, 400), 'RyuvsKen.gif')
    rec.draw(win)
    screen.draw(win)
    win.getMouse()
    win.close()
    game_exe()
    
start_game()