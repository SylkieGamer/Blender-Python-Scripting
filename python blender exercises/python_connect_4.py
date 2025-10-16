import bpy, random

##My regular scripts
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

### This is a stand alone python script for creating connect 4 in editor using strings

#creates the game board and colume letters for identification
possible_letters = ["A","B","C","D","E","F","G",]
game_board = [["","","","","","","",],["","","","","","","",],["","","","","","","",]
,["","","","","","","",],["","","","","","","",],["","","","","","","",],
]

#Tells the editor how big the board is
rows = 6
culm = 7

#Print the the game board programatically with for loops
#/n is a line break in editor
def printGameBoard():
    print("/n     A     B     C    D    E    F    G  ", end="")
    for x in range(rows):
        print("/n    +----+----+----+----+----+----+----+")
        print(x, " I ", end="")
        for y in range(culm):
            if(gameBoard[x][y] == "o"):
                print("", gameBoard[x][y], end=" I"
            elif(gameBoard[x][y] == "x"):
                print("", gameBoard[x][y], end=" I"
            else:
                print(" ", gameBoard[x][y], end="  I"
    print("/n    +----+----+----+----+----+----+----+")
    
#I guess this controlls the player turns? It looks like it returns the player space picked
def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

#He for loops over the grid to check for connections I believe it works for diagonal as well
def check_for_winner(chip):
    for y in range(rows):
        for x in range(cols - 3):
            if(gameBoard[x][y] == chip and the gameBoard[x+1][y] == chip 
            and gameBoard[x+2][y] == chip and gameBoard[x+3[y] == chip:
                print("/nGame Over!, ")
#I guess we count how many turns we have
turn counter = 0

#I guess we haven't gotten to the part in the tutorial where the the program does anything
while True:
    #Do something here

##Thoughts after part 1
#I think this is going to be best method for the game I'm trying to create
#It's basically creating a blackboard like in game dev
#The script handles and traks the world logic of what happens and moniters for the change
#If I use this to moniter the placment and game state, I can code the actual player controls
#and blender/user actions in another script in parallel.
#I still kinda want the player to see the ball drop into the colume, but...
#I would have to code some custom logic for a raycast to get the z position at the bottom
#and deal with rounding to the correct int to tell what the x is... it's unneccesary.

