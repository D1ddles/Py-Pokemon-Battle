import csv

from models.models import Move, get_types

# TEMP Need to create functions for all move effects to add into Move definition
def add_effect(effect: str):
    if effect == "User recovers half the HP inflicted on opponent.":
        return "User recovers half the HP inflicted on opponent."
    else:
        return effect
    
types = get_types()

    
def read_moves() -> dict:
    """
    Reads moves.csv to get all moves and returns a dictionary of "move name": "move object" 
    where the base Move object is extended to include its effect
    """
    # Creates empty dictionary for adding pokemon moves
    moves_dict = {}

    with open('python solution/moves.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip headers

        for row in reader:
            # Grabs move data and effect
            name = row[0]
            type = types[row[1]]
            data = [int(data) if data.isdigit() else data for data in row[2:6]]
            effect = row[6]
            
            # Creates a new Move object based on the data and adds its effect as a new function
            move = Move(name, type, *data) 
            move.effect = add_effect(effect) # finds and adds correct effect to the move
            # Adds new move to the dictionary
            moves_dict[move.name] = move
    
    return moves_dict




