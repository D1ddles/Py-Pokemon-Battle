import pickle
from pathlib import Path

from models.models import Pokemon
from models.moves import read_moves

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

    move = None

    while not move:
        print(f"Select a move to give to {pokemon}: ")
        selection = input()

        try:
            selection = selection.capitalize()
            # Selects Move object from dictionary
            move = moves_dict[selection]
        
        except(KeyError):
            if selection == '':
                print("You must write the name of a move")
            else:
                print("You must write the name of a move that existed in Generation 1")
        
        else:
            print(f"You selected {move}!")
    
    movelist.append(move)

    pokemon.moves = movelist

    return pokemon

moves_dict = get_moves()