import copy
import random

# We want to create some constants or fixed values to help with the game
# This makes the code easier to read, and avoid spelling mistakes
white = "white"
black = "black"
totalChips = 15
home = {white:25, black:0}
start = {white:0, black:25}
middle = {white:26,black:27} # We need to record white/black chips moved off the board

# Create initial setup board
# We have a fixed number of columns that can either be white or black
# A data strucutre to store the board could be a list
# For each element we need to store the colour and number of chips
initialBoard = [[None,0],
                [white,2],[None,0],[None,0],[None,0],[None,0],[black,5],
                [None,0],[black,3],[None,0],[None,0],[None,0],[white,5],
                [black,5],[None,0],[None,0],[None,0],[white,3],[None,0],
                [white,5],[None,0],[None,0],[None,0],[None,0],[black,2],
                [None,0],
                [None,0],
                [None,0]
               ]

def displayBoard(board):
    for counter, point in enumerate(board):
        # Create a new line if on the second half
        # We also add any chips in the middle
        if counter == 13:
            print()
            print()
            if board[middle[white]][1] > 0 or board[middle[black]][1] > 0:
                print("Middle has ", board[middle[white]][1]," white chips in the middle please type",middle[white])
                print("Middle has ", board[middle[black]][1]," black chips in the middle please type",middle[black])
                print()
            for counter in range(13,25):
                if counter == 19:
                    print("  ",end="")
                print("    " + str(counter) + "  ",end="")
            print()

        # We create a divide for the mid part of the game
        if counter == 7 or counter == 19:
            print("||",end =" ")

        if counter == 0:
            print("Black Home has", point[1])
            for counter in range(1,13):
                if counter == 7:
                    print("    ",end="")
                if counter < 7:
                    print("   " + str(counter) + "    ",end="")
                elif counter >= 10:
                    print("    " + str(counter) + "  ",end="")
                else:
                    print("   " + str(counter) + "   ",end="")
            print()
        elif counter == 25:
            print()
            print("White Home has",point[1])
            print()
        elif counter < 25:
            # To make the length of colour so the counter matches up we add a space to None
            if point[0] == None:
                colour = "None "
            else:
                colour = point[0]
            print(colour,point[1],end=" ")
            
def throwADie():
    return random.randint(1,6)

def throwDice():
    dice = []
    dice.append(throwADie())
    dice.append(throwADie())
    # If we roll the same dice the player gets four moves
    if dice[0] == dice[1]:
        dice.append(dice[0])
        dice.append(dice[0])

    return dice

def displayDice(dice, colour):
    print(colour + " rolled:")
    for die in dice:
        print(die)

def getPlayerInt(request):
    #Initialise the answer we wil get from the user to a string so we enter the while loop
    answer = " "
    #A while loop that will continue
    #not answer.isdigit() is not (is answer a digit) so while a strong like "s" is entered the while will continue
    #As soon as the player enters an integer the while loop stops
    while not (answer.isdigit() or (len(answer) > 1 and answer[0] == "-" and answer[1:].isdigit())):
        #The request string provided is prompted to the user for them to input there answer
        #We store the value entered by the player in the variable answer
        answer = input(request)

    #Return the answer after it is converted to an intger int()
    return int(answer)

def requestIntegerFromPlayer(request):
    valid = False
    while not valid:
        try:
            answerAsString = input(request)
            answerAsInteger = int(answerAsString)
            valid = True
        except ValueError:
            print("Please enter an integer")
    return answerAsInteger

def getPlayerDieToMove(colour,dice):
    numberOfMoves = requestIntegerFromPlayer("Please enter number of spaces to move for " + colour)
    # We want to check the player enters one of the die
    while numberOfMoves not in dice:
        print("Please select from",dice)
        numberOfMoves = requestIntegerFromPlayer("Please enter number of spaces to move for " + colour)
    return numberOfMoves

def requestPlayerMove(colour, dice):
    numberOfMoves = 0
    pointToMoveFrom = requestIntegerFromPlayer("Please enter position to move for " + colour)
    # A negative pointToMoveFrom indicates the players wants to stop
    if pointToMoveFrom >= 0:
        numberOfMoves = getPlayerDieToMove(colour,dice)
    return pointToMoveFrom, numberOfMoves

# Determine the direction of the move
# White moves forward
# Balck moves back so we subtract
def determineNewPosition(colour,pointToMoveFrom, numberOfMoves):
    # Determine the direction of the move
    # White moves forward
    # Balck moves back so we subtract
    
    #If we are in the middle we need to reset
    if pointToMoveFrom == middle[colour]:
        pointToMoveFrom = start[colour]

    # If the move is beyond, further, than home we make it home
    if colour == white:
        newPosition = pointToMoveFrom + numberOfMoves
        if newPosition > home[colour]:
            newPosition = home[colour]
    else: 
        newPosition = pointToMoveFrom - numberOfMoves
        if newPosition < home[colour]:
            newPosition = home[colour]

    return newPosition

def dieExists(dice,numberOfMoves):
    return numberOfMoves in dice

def validatePointToMoveFrom(currentBoard,colour,point,silent ):
    valid = True
    if not point <= middle[colour]:
        if not silent:
            print("Point is too large")
        valid = False
    elif not currentBoard[point][0] == colour:
        if not silent:
            print("Position to move from not your colour")
        valid = False
    elif not currentBoard[point][1] > 0:
        if not silent:
            print("Position to mover from does not have sufficient chips")
        valid = False
    elif currentBoard[middle[colour]][1]> 0 and not point == middle[colour]:
        if not silent:
            print("You have chips in the middle, please play these first")
        valid = False

    return valid

def allInHome(currentBoard,colour):
    total = 0
    # We need to create a direction for the range, since home is zero for black and 25 for white
    # So for white we go backwards
    direction = 1
    if colour == white:
        direction = -1

    for counter in range(home[colour],determineNewPosition(colour,home[colour],-7),direction):
        if currentBoard[counter][0] == colour:
            total += currentBoard[counter][1]
    return total == totalChips

# We need to validate the point to move to
def validatePointToMoveTo(currentBoard,colour,point,silent ):
    valid = True
    if currentBoard[point][0] != colour and currentBoard[point][0] != None and not currentBoard[point][1] == 1:
        if not silent:
            print("Position is not your colour and has more than one chip")
        valid = False
    elif not (currentBoard[point][0] == colour or currentBoard[point][0] == None or currentBoard[point][1] == 1):
        if not silent:
            print("Position to move to is not your colour or no colour")
        valid = False
    elif point%25 == 0 and not allInHome(currentBoard,colour):
        if not silent:
            print("Not able to move off the board till all chips are home")
        valid = False
    return valid

def validPlayerInstructions(currentBoard,colour,dice,pointToMoveFrom, numberOfMoves, silent=False):
    # Assume it is valid
    # We can then have a number of nots to check if valid and set not with feedback
    valid = True
    if not dieExists(dice,numberOfMoves):
        print("Die does not exist")
        valid = False
        
    if not validatePointToMoveTo(currentBoard,colour,determineNewPosition(colour,pointToMoveFrom, numberOfMoves),silent):
        valid = False
        
    if not validatePointToMoveFrom(currentBoard,colour,pointToMoveFrom,silent):
        valid = False
        
    return valid

def playerCanMove(currentBoard,colour,dice):
    canMove = False
    counter = 0
    # We use a while so we can exit once the player can move, this is faster than doing a for every move
    while counter < len(currentBoard):
        if currentBoard[counter][0] == colour:
            for die in dice:
                if validPlayerInstructions(currentBoard,colour,dice,counter,die,True):
                    canMove = True
        counter += 1
    return canMove

def validPlayerRound(currentBoard,colour,dice):
    valid = False
    pointToMoveFrom, numberOfMoves = requestPlayerMove(colour,dice)
    while pointToMoveFrom >= 0 and not valid and playerCanMove(currentBoard,colour,dice):
        if validPlayerInstructions(currentBoard,colour,dice,pointToMoveFrom, numberOfMoves):
            valid = True
        else:
            print("Please try again")
            pointToMoveFrom, numberOfMoves = requestPlayerMove(colour,dice)
    
    return pointToMoveFrom, numberOfMoves
    
def makePlayerMove(currentBoard,colour,pointToMoveFrom, numberOfMoves):
    #Decrement chip from position to move from
    positionFromCount = currentBoard[pointToMoveFrom][1]-1
    positionFromColour = colour
    if positionFromCount == 0:
        positionFromColour = None
    currentBoard[pointToMoveFrom] = [positionFromColour,positionFromCount]
    # Determine the direction of the move
    # White moves forward
    # Black moves back so we subtract
    newPosition = determineNewPosition(colour,pointToMoveFrom, numberOfMoves)
    originalColour = currentBoard[newPosition][0]
    if currentBoard[newPosition][0] != None and currentBoard[newPosition][0] != colour:
        currentBoard[middle[originalColour]] = [originalColour,currentBoard[middle[originalColour]][1] + 1]
        currentBoard[newPosition][1] = 0
    currentBoard[newPosition] = [colour,currentBoard[newPosition][1]+1]
    return currentBoard

def playerRound(currentBoard,colour,dice):
    pointToMoveFrom = 0
    # We don't know how many dice they have or if the try to exit with a negative pointToMoveFrom
    # So we need a conditional while to loop
    while len(dice) > 0 and pointToMoveFrom >= 0:
        pointToMoveFrom, numberOfMoves = validPlayerRound(currentBoard,colour,dice)
        currentBoard = makePlayerMove(currentBoard,colour,pointToMoveFrom, numberOfMoves)
        displayBoard(currentBoard)
        if pointToMoveFrom >= 0:
            dice.remove(numberOfMoves)
    return currentBoard, pointToMoveFrom
        
def playGame(currentBoard,colour):
    dice = throwDice()
    print("New turn for",colour)
    displayBoard(currentBoard)
    displayDice(dice,colour)
    if playerCanMove(currentBoard,colour,dice):
        currentBoard, pointsToMoveFrom = playerRound(currentBoard,colour,dice)
    else:
        print(colour + " has no moves")
        pointsToMoveFrom = 0
    return currentBoard, pointsToMoveFrom 
        
def main():
    # We need to make a deep copy or whe we change the currentBoard we will also change the initialBoard
    # It is a memory address to the same list
    currentBoard = copy.deepcopy(initialBoard)
    pointsToMoveFrom = 0
    print("To exit enter a negative position to move from")
    # We need to iterate to keep till one player has all chips home or someone tries to exit with a negative pointToMoveFrom
    # So we need to iterate with a while since it is conditional
    while (currentBoard[home[white]][1] != totalChips and currentBoard[home[black]][1] != totalChips) and pointsToMoveFrom >=0:
        currentBoard,pointsToMoveFrom = playGame(currentBoard,white)
        if pointsToMoveFrom >= 0:
            currentBoard,pointsToMoveFrom = playGame(currentBoard,black)
        
if __name__ == "__main__":
    main()
