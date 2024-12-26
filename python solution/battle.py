import pickle
import csv
from pathlib import Path

from models.models import Poke_type, Pokemon

def create_poke_types() -> dict:
    """
    Creates all Poke_type objects and returns all in a dict
    """
    types = {}
    type_names = ["Bug", "Dragon", "Electric", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Water"]
    
    for name in type_names:
        types[name] = Poke_type(name=name)

    for type in types.values():
        type.set_relationships()

    return types

def write_pickle():
    """
    Takes data from pokemon-stats.csv to create Pokemon objects for all pokemon in the csv and write to a pickle file
    """
    data = []
    types = create_poke_types()

    with open('python solution/pokemon-stats.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip headers

        for row in reader:
            poke_data = row
            
            # replace types strings with type objects
            for i in [2,3]:
                if poke_data[i]:
                    poke_data[i] = types.get(poke_data[i])
            
            pokemon = Pokemon(*poke_data)

            data.append(pokemon)

    with open("python solution/models/pokemon.pkl", "wb") as file:
        pickle.dump(data, file)

def get_pokemon() -> dict:
    """
    Reads the pokemon pickle file and creates a dictionary of "pokemon name": "Pokemon object" for all pokemon
    """
    file_path = Path("python solution/models/pokemon.pkl")

    if not file_path.exists():
        write_pickle()
        file_path = Path("python solution/models/pokemon.pkl")

    with file_path.open('rb') as file:
        data = pickle.load(file)

        pokemon_dict = {}
        for pokemon in data:
            pokemon_dict[pokemon.name] = pokemon

        return pokemon_dict

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
            pokemon = pokemon_dict[selection]

        except (KeyError):
            if selection == '':
                print("You must write the name of a pokemon")
            else:
                print("You must write the name of a pokemon from Generation 1")

        else:
            print(f"You selected: {pokemon}!")

    return pokemon

pokemon_dict = get_pokemon()
while True:

    player1 = pokemon_select(pokemon_dict)
    player2 = pokemon_select(pokemon_dict)

    print(player1)
    print(player2)

    print(player1.type1.strong)
    
    break