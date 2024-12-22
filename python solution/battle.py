import pickle
from pathlib import Path

from models.models import Poke_type, Pokemon
from models.models_helper import write_pickle

def get_pokemon() -> dict:

    file_path = Path("models/pokemon.pkl")

    if not file_path.exists():
        write_pickle()
        file_path = Path("models/pokemon.pkl")

    with file_path.open('rb') as file:
        data = pickle.load(file)

        pokemon_dict = {}
        for pokemon in data:
            pokemon_dict[pokemon["Name"]] = pokemon

        return pokemon_dict

def pokemon_select(pokemon_dict: dict) -> dict:
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

    print(player1.get('Type 1'))
    
    break