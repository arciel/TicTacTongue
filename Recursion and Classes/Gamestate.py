"""Contains the class to represent a gamestate of TicTacToe."""

from ExtendedAPI import *

class Gamestate:
    """The class implementing a state of the game."""
    def __init__(self, grid, whos_turn):
        """Constructor, especially useful for generating states recursively."""
        self.grid = grid
        self.zeros = whos_turn
        self.states = []
        self.value = 0.0

    def make_states(self):
        """Makes child states of self."""
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] == ' '):
                    new_grid = [row[:] for row in self.grid]
                    new_grid[i][j] = '0' if (self.zeros) else 'X'
                    new_state = Gamestate(new_grid, not self.zeros)
                    self.states.append(new_state)
                    new_state.make_states()

    def calculate_value(self):
        """Calculates the value of self."""
        if (not self.states):                                        # If self doesn't have any child states (is a leaf) ...
            self.value = 10.0 if (not lost(self.grid)) else 0.0      # ... then assign a value depending upon the winner.
        else:
            for state in self.states:
                state.calculate_value()
                self.value += state.value
            self.value //= len(self.states)
                
                    
