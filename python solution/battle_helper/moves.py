import math
import csv
from random import randint
from pathlib import Path

import pickle

from models.models import Pokemon, Move

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
            # Grabs move data, saving numbers as integers
            data = [int(data) if data.isdigit() else data for data in row]

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

def moves_select(pokemon: Pokemon, moves_dict: dict) -> Pokemon:
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

# Executes effect
def effect(effect: str, dmg: int, attacking: Pokemon, defending: Pokemon):

    if effect == "User recovers 50% of the damage dealt.":
        attacking.hp += math.floor(dmg / 2)

    elif effect == "33% chance to lower the target's Defense by 1.":
        if randint(1,250) > 83:
            defending.dfs.stage += 1

    elif effect == "Raises the user's Defense by 2.":
        attacking.dfs.stage += 2

    elif effect == "Raises the user's Speed by 2.":
        attacking.spd.stage += 2

    elif effect == "Raises the user's Special by 2.":
        attacking.spec.stage += 2

    elif effect == "33% chance to lower the target's Attack by 1.":
        if randint(1,250) > 83:
            defending.atk.stage += 1
    
    elif effect == "Hits 2-5 times in one turn.":
        random = randint(1,8)
        if random in (1,2,3):
            dmg *= 2
        elif random in (4,5,6):
            dmg *= 3
        elif random == 7:
            dmg *= 4
        elif random == 8:
            dmg *= 5

    elif effect == "Waits 2-3 turns; deals double the damage taken.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
    
    elif effect == "Prevents the target from moving for 2-5 turns.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "10% chance to make the target flinch.":
        ### NEEDS DOING ###
        if randint(1, 10) == 10:
            pass
        print("UNFINISHED MOVE")

    elif effect == "10% chance to freeze the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    return dmg

moves_dict = get_moves()

