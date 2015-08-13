""" 
This file contains an program that implements the simple (and as we saw, defeatable)
algorithm to play TicTacToe. This is the last file for lesson one.

We'll see how almost with no new functions, the defensive strategy can be implemented.
You're playing as the TicTacMan/Woman. 
 
Next, I'll be putting up the code for the unbeatable Tic-Tac-Toe strategy, along with
a HUGE accompanying lesson on recursion, and graphs. I promise it'll be very interesting.
Stay tuned!

""" 

from random import randint; # randint(a, b) will return a random integer in the set {a, ... , b}

from ExtendedAPI import *; 

Grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  # Create empty grid.

ourTurn = True                   # We'll go first. 
while (not gameEnd(Grid)):      # While we can still play.
    if (ourTurn):
        i = int(raw_input("Enter X in row __ : "))
        j = int(raw_input("Enter X in column __: "))
        while (i < 0 or i > 2):
            i = int(raw_input("Row should be between 0 and 2: "))
        while (j < 0 or j > 2):
            j = int(raw_input("Col should be between 0 and 2: "))
        while (isCross(Grid, i, j) or isCross(Grid, i, j)):
            print "Please enter unoccupied coordinates"
            i = int(raw_input("Enter X in row __ : "))
            j = int(raw_input("Enter X in column __: "))
        Grid[i][j] = 'X'
        print("")
        print("You: ")
        printToConsole(Grid)        # Print the grid after every move
    else:
        if (boardFacesThreat(Grid)):     # If board is under threat from our perspective.
            i = 0                              # The first row we check will be row 0. This is asymmetric. Any suggestions?
            stopLooking = False                # We'll stop looking for rows when we find one under threat.      
            while (i < 3 and (not stopLooking)):
                print ("trapped in i")
                if (threatInRow(Grid, i)):             # Found the row under threat.
                    j = 0
                    while (j < 3 and (not stopLooking)):
                        print ("trapped in j1")
                        if (not isCross(Grid, i, j)):     # If this block in this row is empty
                            put(Grid, i, j)               # Block the threat by putting an X here.
                            stopLooking = True            # We can stop looking now.
                            break                         # Stop looking at any more blocks.
                        j += 1                            # Increment j to check the next block (if needed).
                if (threatInCol(Grid, i)):
                    j = 0
                    while (j < 3 and not stopLooking):
                        print ("trapped in j2")
                        if (not isCross(Grid, j, i)):
                            put(Grid, j, i)
                            stopLooking = True
                            break
                        j += 1
                i += 1                # Increment i to check next row.
            i = 0
            if (not stopLooking):
                if (threatInDiagonal1(Grid)):
                    for i in range(0, 3):
                        if (not isCross(Grid, i, i)):
                            put(Grid, i, i)
                            stopLooking = True
                            break
                elif (threatInDiagonal2(Grid)):
                    for i in range(0, 3):
                        if (not isCross(Grid, i, 2-i)):
                            put(Grid, i, i)
                            stopLooking = True
                            break

        else:                         # Else if the board is not under threat, play randomly
            i = randint(0, 2)         # Generate random coordinates to put a '0' on.
            j = randint(0, 2)         
            while (isCross(Grid, i, j) or isZero(Grid, i, j)):
                i = randint(0, 2)
                j = randint(0, 2)
            put(Grid, i, j)                # Put a 0 on the random coordinates.    
        print("")
        print("Earth's Mightiest Zeros: ")
        printToConsole(Grid)        # Print the grid after every move
    ourTurn = not ourTurn       # Give the other guy the move.
    
print("\n\nGame over: "),
if (ourTurn):
    print("The Earth's Mightiest Zeros win!")
else:
    print("TicTacMan/Woman wins!")
