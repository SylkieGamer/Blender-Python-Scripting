import bpy, random

##My regular scripts
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

### This is a stand alone python script for creating connect 4 in editor using strings

#creates the game board and colume letters for identification
possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""],
["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

#Tells the editor how big the board is
rows = 6
cols = 7

#Print the the game board programatically with for loops
#/n is a line break in editor
def printGameBoard():
    print("\n    A     B     C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n    +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "o"):
                print("", gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "x"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n    +----+----+----+----+----+----+----+")
    
#I guess this controlls the player turns? It looks like it returns the player space picked
def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

#He for loops over the grid to check for connections I believe it works for diagonal as well
def checkForWinner(chip):
    #check Horizontal
    for y in range(rows):
        for x in range(cols - 3):
            if(gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip):
                print("\nGame Over!, "), chip, (" wins! Thank you for playing :)")
                return True
    #check the verticle
    for y in range(rows):
        for x in range(cols - 3):
            if(gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip):
                print("\nGame Over!, "), chip, (" wins! Thank you for playing :)")
                return True
    #check diagonal top right to bot left
    for y in range(rows - 3):
        for x in range(3, cols):
            if(gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip):
                print("\nGame Over!, "), chip, (" wins! Thank you for playing :)")
                return True
    #check top left to bot right
    for y in range(cols - 3):
        for x in range(3, cols):
            if(gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip):
                print("\nGame Over!, "), chip, (" wins! Thank you for playing :)")
                return True
    return False
    
def coordinateParser(inputString):
    coordinate = [None] * 2
    if(inputString[0] == "A"):
        coordinate[1] = 0 
    elif(inputString[0] == "B"):
        coordinate[1] = 1
    elif(inputString[0] == "C"):
        coordinate[1] = 2
    elif(inputString[0] == "D"):
        coordinate[1] = 3
    elif(inputString[0] == "E"):
        coordinate[1] = 4
    elif(inputString[0] == "F"):
        coordinate[1] = 5
    elif(inputString[0] == "G"):
        coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvaible(intendedCoordinate):
    if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == 'o'):
        return False
    elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == 'x'):
        return False
    else:
        return True
    
def gravityChecker(intendedCoordinate):
    #calculate space below
    
    spaceBelow= [None] * 2
    spaceBelow[0] = intendedCoordinate[0] + 1
    spaceBelow[1] = intendedCoordinate[1]
    #is coordinate at ground level
    if(spaceBelow[0] == 6):
        return True
    #is there a token below
    if(isSpaceAvaible(spaceBelow) == False):
        return True
    return False



#I guess we count how many turns we have
turnCounter = 0
while True:
    if(turnCounter % 2 == 0):
        printGameBoard()
        while True:
            spacePicked = input("\nChose a space: ")
            coordinate = coordinateParser(spacePicked)
            try:
                #check is space avaible
                if(isSpaceAvaible(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, 'o')
                    break
                else:
                    print("Not a valid coordinate.")
            except:
                print("Error occured. Please try again.")
        winner = checkForWinner('o')
        turnCounter += 1
    #it's computers turn
    else:
        while True:
            cpuChoice = [random.choice(possibleLetters), random.randint(0,5)]
            cpuCoordinate = coordinateParser(cpuChoice)
            if(isSpaceAvaible(cpuCoordinate) and gravityChecker(cpuCoordinate)):
                modifyArray(coordinate, 'x')
                break
        turnCounter += 1
        winner = checkForWinner('x')
    if(winner):
        printGameBoard()
        break

##Thoughts after part 1
#I think this is going to be best method for the game I'm trying to create
#It's basically creating a blackboard like in game dev
#The script handles and traks the world logic of what happens and moniters for the change
#If I use this to moniter the placment and game state, I can code the actual player controls
#and blender/user actions in another script in parallel.
#I still kinda want the player to see the ball drop into the colume, but...
#I would have to code some custom logic for a raycast to get the z position at the bottom
#and deal with rounding to the correct int to tell what the x is... it's unneccesary.

