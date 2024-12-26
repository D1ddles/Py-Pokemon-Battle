import pickle
import csv
from pathlib import Path

from models.models import Poke_type, Pokemon

def write_pickle():
    data = []
    with open('python solution/pokemon-stats.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip headers
        for row in reader:
            poke = Pokemon(*row)
            data.append(poke)

    with open("python solution/models/pokemon.pkl", "wb") as file:
        pickle.dump(data, file)

def get_pokemon() -> dict:

    file_path = Path("python solution/models/pokemon.pkl")

    if not file_path.exists():
        write_pickle()
        file_path = Path("python solution/models/pokemon.pkl")

    with file_path.open('rb') as file:
        data = pickle.load(file)
        print(data)

        pokemon_dict = {}
        for pokemon in data:
            pokemon_dict[pokemon.name] = pokemon

        return pokemon_dict

def pokemon_select(pokemon_dict: dict) -> Pokemon:
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

    print(player1.type1)
    
    break