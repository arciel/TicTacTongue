"""
Firstly, implement ALL the functions from Functions.py using isCross 
(if they need it). After that, you can add pretty much any function you need
here, for Game.py.

"""

from Library import *; # Don't remove!

# You may need this method:

def printToConsole():
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

# After doing that, head to the showdown. Game.py.