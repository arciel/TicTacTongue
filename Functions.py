"""
This code will help you understand the workings of TicTacTongue. 
You'll write your own strategy (algorithm), and play against it. 

Make sure you read the syntax and the readme file before starting here.

Remember: The instructions - your team - is called Earth's Mightiest Zeros! 
It will be important later (when you realize just how awesome Marvel is).

Reading code can be a little dry - but don't give up! Read this file, please. 

"""

# NOTE: The words 'line' and 'instruction' have been used interchangeably, as,
# mostly, in a program, there is one instruction per line (roughly). 
# May or may not be true for individual lines. Sometimes, two or even three 
# instructions can be on one line. But we'll assume there's just one per line.

# A function is a set of instructions. Now, why do we use functions? A very 
# common example is this - say you want to do something that takes a couple of
# instructions (say 10). And you want to do it many times, at different places 
# in your code. 

# Now, if you make a function of those instructions, instead of 
# writing those same (or similar) 10 lines everywhere in your code, you can 
# write the 10 lines once, and CALL the FUNCTION of those 10 lines everywhere.

# Calling a function takes only one line, so, if you needed that code in 20 
# places, instead of 200 lines, you use only 21. This makes reading and 
# maintaining code much easier and better.  


# We're setting up an empty 3x3 grid. The game shall be played here.

Grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  


# Basically, we created 3 rows, each row containing 3 empty boxes. And then,
# we stacked those rows upon one-another. Remember, numbering of rows as well as
# columns starts from 0. 


def crossesInRowZero():
    """This function returns the number of Xs in row zero (0).""" 
    count = 0                          # This will count the number of X's in the row.
    index = 0                                # This is the column index in row 0. 
    while (index < 3):                           # While loop starts.   <------<---   
        if (Grid[0][index] == 'X'):             # If there's an X at (0, index) ... ^
            count = count + 1                   # ... increase count by 1.           ^
        else:                              # If there isn't an X at (0, index) ...   ^
            pass                           # ... do nothing.                         ^ 
        index = index + 1             # Either way, now look at the next box.        ^
             # Follow this arrow for the next iteration.  ---->----------->---------^ 
    
    # We've looked at all boxes in row 0. Now index = 3. We're out of the loop.
    return count                                                 # We are done!
    
    
def crossesInRowOne():
    """This function returns the number of Xs in row one (1)."""     
    # Everything is similar to the previous function (crossesInRowZero). 
    count = 0
    index = 0
    while (index < 3):
        if (Grid[1][index] == 'X'):
            count = count + 1
        else:
            pass
        index = index + 1          
    return count


def crossesInRowTwo():
    """This function returns the number of Xs in row two (2)."""     
    # Everything is similar to the crossesInRowZero and crossesInRowOne. 
    count = 0
    index = 0
    while (index < 3):
        if (Grid[2][index] == 'X'):
            count = count + 1
        else:
            pass
        index = index + 1          
    return count        

# The previous three functions (the only three so far, actually) simply gave us
# the number of Xs in their respective rows. To do such a simple task, we had 
# to write THREE nearly identical functions! Obviously, programming is not so 
# boring (if it was, nobody would be doing it). Can you think of a trick? 

# What if I can TELL the function which row it should look in? 
# This is a very important concept called PASSING AN ARGUMENT to a function.
# An argument is a piece of information, like an integer, that we give to an 
# entity, like a function, which helps the function perform. Here's an example.


def crossesInRowK(k):
    """This function returns the number of Xs in row 'k'."""
    # k is an integer in the set {0, 1, 2}. So, depending on k, we can get
    # the number of Xs in rows 0, 1, and 2. Here's how.
    
    while (k > 2):      # To keep trouble-makers at bay. Not important for now.
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (Grid[k][index] == 'X'): # We're looking at row 'k', which can be ..
            count = count + 1       # .. any row, really. We chose the 'k'.   
        else:
            pass
        index = index + 1          
    return count 
     
     
def threatPresent():  
    """This function will detect if there is a threat present or not."""
    
    
