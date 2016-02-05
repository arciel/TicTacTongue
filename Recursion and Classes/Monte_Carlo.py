from Gamestate import *
import random


  
NTRIALS = 100000    # Number of trials to run

def get_empty_squares(Grid):
    list=[]
    for i in range(3):
        for j in range(3):
            if(Grid[i][j]==''):
                list.append((i,j))
    return list
"""
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player
    by making random moves, alternating between players.
    The function should return when the game is over.
    The modified board will contain the state of the game,
    so the function does not return anything.
"""
def mc_trial(Grid,zero_move):
    
    if(ttp_lost(Grid) or zeros_lost(Grid)):
        return
    empty=get_empty_squares(Grid)
    count=len(empty)
    if(count==0):
        return 
    pos=random.randint(0,count-1)
    (a,b)=empty[pos]
    if(zeros_move):
        Grid[a][b]='0'
    else:
        Grid[a][b]='X'
    mc_trial(Grid, not zeros_move)

"""
    This function takes a grid of scores (a list of lists)
    with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game,
    and which player the machine player is.
    The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly,
    it does not return anything.
"""

def mc_update_scores(Grid,zeros_move,scores):
    
    if(ttp_lost(Grid)):
        for i in range(3):
            for j in range(3):
                if(Grid[i][j]=='0'):
                    scores[i][j]+=2
                if(Grid[i][j]=='X'):
                    scores[i][j]-=1
    if(zeros_lost(Grid)):
        for i in range(3):
            for j in range(3):
                if(Grid[i][j]=='0'):
                    scores[i][j]-=1
                if(Grid[i][j]=='X'):
                    scores[i][j]+=2
    return
"""
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple.
"""
def get_best_move(Grid,scores):

    
    max=scores[0][0]
    list=[]
    
    for i in range(3):
        for j in range(3):
            
            if(scores[i][j]>=max):
                list.append((i,j))
                max=scores[i][j]
    
    return list[random.randrange(len(list))]
"""
    This function takes a current board,
    which player the machine player is,
    and the number of trials to run.
    The function should return a move for the machine player
    in the form of a (row, column) tuple.
"""
def mc_move(Grid, zeros_move, trials):
    
    
    scores = [[0 for dummy in range(3)] 
        for dummy in range(3)]
    temp=state.grid
    for dummy in range(trials):
        mc_trial(Grid, zeros_move)
        mc_update_scores(Grid, zeros_move, scores)
        state.grid=temp
    return get_best_move(Grid, scores)
    


Grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

x_moves = raw_input("Welcome, TicTacMan/Woman! >:( Do you want to go first? (Y or N): ")

zeros_move = True if (x_moves == 'N' or x_moves == 'n') else False



first_move = True
while (first_move or (not game_end(state.grid))):
    if (first_move):
        if (not zeros_move):
            i = int(raw_input("Enter X in row __: "))
            j = int(raw_input("Enter X in col __: "))
            while (i < 0 or i > 2):
                i = int(raw_input("Row should be between 0 and 2: "))
            while (j < 0 or j > 2):
                j = int(raw_input("Col should be between 0 and 2: "))
            Grid[i][j] = 'X'
            print("\nYou: ")
        else:
            Grid[0][0] = '0'
            print("\nEarth's Mightiest Zeros: ")
        
        first_move = False
    else:     
        if (not zeros_move):
            i = int(raw_input("Enter X in row __: "))
            j = int(raw_input("Enter X in col __: "))
            while (i < 0 or i > 2):
                i = int(raw_input("Row should be between 0 and 2: "))
            while (j < 0 or j > 2):
                j = int(raw_input("Col should be between 0 and 2: "))
            Grid[i][j]='X'
            print("\nYou: ")
        else:
            (a,b)=mc_move(Grid, True, NTRIALS)
            while(Grid[a][b]!=' '):
                (a,b)=mc_move(Grid, True, NTRIALS)
                
            Grid[a][b]='0'
            print("\nEarth's Mightiest Zeros: ")
    state = Gamestate(Grid, not zeros_move, 1)
    printToConsole(state.grid)
    zeros_move = not zeros_move
    
print("\n\nGame over:"),
if (ttp_lost(state.grid)):
    print("The Earth's Mightiest Zeros win!")
elif (zeros_lost(state.grid)):
    print("TicTacMan/Woman wins!")
else:
    print("Draw.")
