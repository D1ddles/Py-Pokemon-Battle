import pickle

from models.models import Poke_type, Pokemon

def get_pokemon():
    with open(r"python solution\models\pokemon.pkl", 'rb') as file:
        data = pickle.load(file)

        pokemon_dict = {}
        for pokemon in data:
            pokemon_dict[pokemon["Name"]] = pokemon

        return pokemon_dict

def pokemon_select(pokemon_dict):
    print("Select a pokemon: ")
    selection = input()
    if selection:
        pokemon = pokemon_dict[selection]

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