"""
Firstly, implement ALL the functions from Functions.py using isCross 
(if they need it). After that, you can add pretty much any function you need
here, for Game.py.

"""

from Library import *; # Don't remove!

# You may need this method:

def printToConsole(Grid):
    """ This method prints the Grid onto the screen."""
    for i in range(0, 3):
        print("   |   |   ")
        for j in range(0, 3):
            print "\b " + str(Grid[i][j]) + " ",
            if (j != 2):
                print "\b|",
            else:
                print ""
        if (i != 2):
            print "___|___|___"
        else:
            print "   |   |   "
            
            
# Methods for playing against the computer.

def zerosInRowK(k):
    """This function returns the number of Xs in row 'k'."""
    # k is an integer in the set {0, 1, 2}. So, depending on k, we can get
    # the number of 0s in rows 0, 1, and 2. Here's how.
    
    while (k > 2):      # To keep trouble-makers at bay. Not important for now.
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (Grid[k][index] == '0'): # We're looking at row 'k', which can be ..
            count = count + 1       # .. any row, really. We chose the 'k'.   
        else:
            pass
        index = index + 1          
    return count         
        

def zerosInColK(k):
    """This function will return the number of Xs in column k."""
    while (k > 2):      
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (Grid[index][k] == '0'): 
            count = count + 1      
        else:
            pass
        index = index + 1          
    return count 
    

def zerosInDiag1():   
    """This function will return the number of 0s in the main diagonal."""
    count = 0
    index = 0
    while (index < 3):
        if (Grid[index][index] == '0'):
            count = count + 1
        else:
            pass
        index = index + 1
    return count
    
def zerosInDiag2():   
    """This function will return the number of 0s in the other diagonal."""
    count = 0
    i = 0
    while (i < 3):
        if (Grid[i][2-i] == '0'): 
            count = count + 1
        else:
            pass
        i = i + 1
    return count
    

def weLost():
    """This function will return True if we have lost the game."""
    i = 0
    while (i < 3):
        if (zerosInRowK(i) == 3):
            return True
        elif (zerosInColK(i) == 3):                          # Else, If {...}
            return True
        else:
            pass
    if (zerosInDiag1 == 3 or zerosInDiag2 == 3):
        return True
    else:
        return False
        

def isZero(x, y):
    """This function returns True if there is an X at (x, y)."""
    while (x > 2): 
        x = int(raw_input("Please enter an 'x' in {0, 1, 2}: "))
    while (y > 2):    
        y = int(raw_input("Please enter a 'y' in {0, 1, 2}: "))
    return (Grid[x][y] == '0')

def gameEnd():
    """ This function returns True if the game has ended """
    return weLost() or lost()    # The game ends when someone loses (or wins).


# After doing that, head to the showdown. Game.py.