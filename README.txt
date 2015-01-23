
ICE BREAKERS: STREET FIGHTER EDITION
BY: Olamide Adeniji

	This is my version of ice breakers. I implemented my game by creating a game board representation of the game using a list. 
This list keeps track of all the things going on in the game,and can be used with if statements to check if the player is making a legal move. 
I then created a visual representation the the game using graphics.py.

	To run the game all a person would have to do is run the GameFile then select which game mode they would like to play. 
I did not implement a 1p game mode so clicking anywhere on the splash screen will load up the 2 player game. the start game function calls the game_exe() function,
which contains all of the most important key functions for my game. the game board function, the board_rep function, and the play_game function.
The game_board function handles the drawing of the game board, the board_rep function controls the marking down of important information that is needed by
my program to calculate legal moves (such as current position of players, and ice break locations), and the play_game function controls the main game loop.

	My global variables were, my win, player_1, player_2, p_text, game_running,  and board. the win variable controls the game window, the player_1 and player_2 
variables control where the circle representation of a player is drawn, the P_text variable controls what text is shown at the bottom of the game board, and 
my last variable game_running contrls the main loop of the game.

	It might also be worthwhile to mention that i attempted to start making the game using the hexagons for the bonus marks, but i was unable to figure out how to change my mouse clicks from a
player into hexagon positions on my game board. i put my attempt into my project folder (project(hexagon)).
