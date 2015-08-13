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

def playDefensive(Grid):
    """ This is the function we use to play the defensive game. Simply call it. """
    ourTurn = True                   # We'll go first. 
    while (not gameEnd()):          # While we can still play.
        if (ourTurn):
            i = int(raw_input("Enter X in row __ : "))
            j = int(raw_input("Enter X in column __: "))
            while (isCross(i, j) or isCross(i, j)):
                print "Please enter unoccupied coordinates"
                i = int(raw_input("Enter X in row __ : "))
                j = int(raw_input("Enter X in column __: "))
            Grid[i][j] = 'X'
        else:
            if (boardFacesThreat()):       # If board is under threat from our perspective.
                i = 0                              # The first row we check will be row 0. This is asymmetric. Any suggestions?
                stopLooking = False                # We'll stop looking for rows when we find one under threat.      
                while (i < 3 and not stopLooking):
                    if (crossesInRowk(i) == 2):             # Found the row under threat.
                        j = 0
                        while (j < 3 and not stopLooking):
                            if (not isCross(i, j)):           # If this block in this row is empty
                                put(i, j)                      # Block the threat by putting an X here.
                                stopLooking = True             # We can stop looking now.
                                break                         # Stop looking at any more blocks.
                        j += 1                           # Increment j to check the next block (if needed).
                i += 1                            # Increment i to check next row.
            else:                         # Else if the board is not under threat, play randomly
                i = randint(0, 2)         # Generate random coordinates to put a '0' on.
                j = randint(0, 2)         
                while (isCross(i, j) or isZero(i, j)):   # If (i, j) is full, again call random coordinates.
                     i = randint(0, 2)
                     j = randint(0, 2)
                put(i, j)                # Put a 0 on the random coordinates.
        ourTurn = not ourT   # Give the other guy the move.
        printToConsole()     # Print the grid after every move
    
    print "Game over."