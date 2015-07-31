""" 
This code will help you understand the workings of TicTacTongue. 
You'll write your own strategy (algorithm), and play against it. 

REMEMBER: Your strategy is implemented by your computer. Therefore.. 
if you lose to your computer, you had a good strategy. Well done.
But if you win, well done again! You had a good strategy. But, you.. 
.. should try to let your computer win once in a while too.

Also remember: The instructions - your team - is called Earth's Mightiest Zeros! 
It will be important later (when you realize just how awesome Marvel is. 
"""    

#We're setting up an empty 3x3 grid.
Grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  
#Basically, we                    
    
def isThreat(Grid):  
    """This function will detect if there is a threat present or not."""
    x = False;
    
