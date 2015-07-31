"""
This code will help you understand the workings of TicTacTongue. 
You'll write your own strategy (algorithm), and play against it. 

Make sure you read the syntax in the readme file before starting here.

Remember: The instructions - your team - is called Earth's Mightiest Zeros! 
It will be important later (when you realize just how awesome Marvel is). 

"""

# We're setting up an empty 3x3 grid. The game shall be played here.

Grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  

# Basically, we created 3 rows, each row containing 3 empty boxes. And then,
# we stacked those rows upon one-another. Remember, numbering of rows as well as
# columns starts from 0. 

def crossesInRowZero():
    """This function returns the number of Xs in row zero (0).""" 
    count = 0  #                   This will count the number of X's in the row.
    index = 0  #                              This is the column index in row 0. 
    while (index < 3):  # <------<---    While loop starts. See the condition?
        if (Grid[0][index] == 'X'):# ^        If there's an X at (0, index) ...  
            count = count + 1      # ^        ... increase count by 1.
        else:                     # ^     If there isn't an X at (0, index) ...
            pass                 # ^      ... do nothing.              
        index = index + 1       # ^        Either way, now look at the next box.
    # ---->----------->---------^      Follow this arrow for the next iteration.
 
    #  We've looked at all boxes in row0. Now index = 3. We're out of the loop. 
    if (count >= 2):                # Count = 2 implies two X's in row0. Threat.
        return True
              
    
def threatPresent():  
    """This function will detect if there is a threat present or not."""
    
    
