from Gamestate import Gamestate

Grid = [['X', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']]

state = Gamestate(Grid, True)

state.make_states()

state.calculate_value()

print("State value:"),
print(state.value)
