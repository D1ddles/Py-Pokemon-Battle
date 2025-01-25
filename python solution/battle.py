import pickle
import csv
from pathlib import Path
from random import randint

from models.models import Poke_type, Pokemon, Move, create_poke_types
from models.moves import read_moves

# Pickle file saving functions
def save_pokemon():
    """
    Takes data from pokemon-stats.csv to create Pokemon objects for all pokemon
    in a csv and write to a pickle file
    """
    data = []
    types = create_poke_types()

    with open('python solution/pokemon-stats.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip headers

        for row in reader:
            poke_data = [int(data) if data.isdigit() else data for data in row]
            
            # replace types strings with type objects
            for i in [2,3]:
                if poke_data[i]:
                    poke_data[i] = types.get(poke_data[i])
            
            pokemon = Pokemon(*poke_data)

            data.append(pokemon)

    with open("python solution/models/pokemon.pkl", "wb") as file:
        pickle.dump(data, file)

def save_moves():
    """
    Saves all moves in a dictionary of "move name": "move object" for after moves are created
    """
    moves = read_moves()

    with open('python solution/models/moves.pkl', 'wb') as file:
        pickle.dump(moves, file)


# Dictionary returning functions
def get_pokemon() -> dict:
    """
    Reads the pokemon pickle file and creates a dictionary of "pokemon name": "Pokemon object" for all pokemon
    """
    file_path = Path("python solution/models/pokemon.pkl")

    if not file_path.exists():
        save_pokemon()
        file_path = Path("python solution/models/pokemon.pkl")

    with file_path.open('rb') as file:
        data = pickle.load(file)

        pokemon_dict = {}
        for pokemon in data:
            pokemon_dict[pokemon.name] = pokemon

        return pokemon_dict
    
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

# Selection functions
def pokemon_select(pokemon_dict: dict) -> Pokemon:
    """
    Lets the user input the name of a pokemon and returns that pokemon object from the pokemon dict
    """
    pokemon = None

    while not pokemon:
        print("Select a pokemon: ")
        selection = input()
        
        try:
            selection = selection.capitalize()
            # Selects Pokemon object from dictionary
            pokemon = pokemon_dict[selection]

        except (KeyError):
            if selection == '':
                print("You must write the name of a pokemon")
            else:
                print("You must write the name of a pokemon from Generation 1")

        else:
            print(f"You selected: {pokemon}!")

    return pokemon

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

# Battle functions
def damage_calc(move: Move, attacking: Pokemon, defending: Pokemon):

        if hasattr(move, "effect"):
            print(move.effect) #TEMP print() to be removed when functions created

        # calculating damage multipliers
        if move.category == "Special":
            atk = attacking.atk
            dfs = defending.dfs
        else:
            atk = attacking.spec
            dfs = defending.spec
        
        # setting attack types
        type1 = attacking.type1
        type2 = attacking.type2

        # Random crits
        if randint(0, 255) > randint(0, 255):
            crit = 2
        else:
            crit = 1

        # STAB (Same Type Attack Bonus) if attack is made by type of the pokemon
        if move.type in [type1, type2]:
            stab = 1.5
        else:
            stab = 1

        # damage calculation
        damage = ((2*crit+2)*move.power*atk/dfs)/50
        damage += 2*stab*type1.type_effectiveness(move.type)*type2.type_effectiveness(move.type)
        if damage != 1:
            damage *= (randint(217,255)/255) # adds "random"-ness to the damage

        return damage

# Create dictionaries for grabbing objects from
pokemon_dict = get_pokemon()
moves_dict = get_moves()

while True:

    player1 = pokemon_select(pokemon_dict)
    player2 = pokemon_select(pokemon_dict)

    player1 = moves_select(player1)
    player2 = moves_select(player2)

    print(player1.moves)
    print(player2.moves)

    print(damage_calc(player1.moves[0], player1, player2))
    
    break