"""
These implementations of put and isCross look a bit different from those in 
Functions.py; but, they will help when you finally get to completing Game.py

"""

# Surely try to look for things you don't know about. But you'll do fine 
# without that too. The thing (maybe good, maybe bad) about many things in the
# world is, you don't have to know what something is - only what it does.

from Functions.py import Grid; # Don't remove! 

def put(x, y):
    """This function puts a '0' at position (x, y)."""
    assert (type(x) == type(y) == int);
    assert (x >= 0 and x <= 2 and y >= 0 and y <= 2);
    Grid[x][y] = '0'
    

def isCross(x, y):
    """This function returns True if there is an X at position (x, y)."""
    assert (type(x) == type(y) == int);
    assert (x >= 0 and x <= 2 and y >= 0 and y <= 2);
    return Grid[x][y] == 'X'
    
    
