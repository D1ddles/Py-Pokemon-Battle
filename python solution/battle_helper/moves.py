import csv
from pathlib import Path

import pickle

from models.models import Pokemon, Move, create_poke_types

def read_moves() -> dict:
    """
    Reads moves.csv to get all moves and returns a dictionary of "move name": "move object" 
    where the base Move object is extended to include its effect
    """
    # Creates empty dictionary for adding pokemon moves
    moves_dict = {}
    types = create_poke_types()

    with open('python solution/moves.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip headers

        for row in reader:
            # Grabs move data, saving numbers as integers
            data = [int(data) if data.isdigit() else data for data in row]
            data[1] = types.get(data[1])

            # Creates a new Move object based on the data and adds its effect as a new function
            move = Move(*data) 
            # Adds new move to the dictionary
            moves_dict[move.name] = move
    
    return moves_dict


def save_moves():
    """
    Saves all moves in a dictionary of "move name": "move object" for after moves are created
    """
    moves = read_moves()

    with open('python solution/models/moves.pkl', 'wb') as file:
        pickle.dump(moves, file)


def get_moves() -> dict:
    """
    Reads the moves pickle file and creates a dictionary of "move name": Move object" for all moves
    """
    file_path = Path("python solution/models/moves.pkl")

    if not file_path.exists():
        save_moves()
        file_path = Path("python solution/models/moves.pkl")

    with file_path.open('rb') as file:
        moves_dict = pickle.load(file)

    return moves_dict


def moves_select(pokemon: Pokemon) -> Pokemon:
    """
    Lets the user input the name of moves to create their pokemon's move list
    """
    # Create empty move list for 4 moves
    movelist = []

    while len(movelist) != 2: # Only two moves for testing for now
        print(f"Select a move to give to {pokemon}: ")
        selection = input()

        try:
            selection = selection.capitalize()
            # Selects Move object from dictionary
            print(selection)
            print(moves_dict["Pay Day"])
            move = moves_dict[selection]

            movelist.append(move)
        
        except(KeyError):
            if selection == '':
                print("You must write the name of a move")
            else:
                print("You must write the name of a move that existed in Generation 1")
        
        else:
            print(f"You selected {move}!")
    
    pokemon.moves = movelist

    return pokemon


moves_dict = get_moves()