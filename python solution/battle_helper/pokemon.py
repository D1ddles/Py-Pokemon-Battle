import pickle
import csv
from pathlib import Path

from models.models import Player, Pokemon, Stat, create_poke_types

# Pickle file saving functions
def save_pokemon():
    """
    Takes data from pokemon-stats.csv to create Pokemon objects for all pokemon
    in the csv and write to a pickle file
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

            # create real stats based on base stats (based on level 100)
            # HP: 10 + L + (B * L / 50)
            hp = 10 + 100 + (poke_data[4] * 100 / 50)
            poke_data[4] = Stat(poke_data[4], hp, hp)
            # Others: 5 + (B * L / 50)
            for i in range(5,9):
                other = 5 + (poke_data[i] * 100 / 50)
                poke_data[i] = Stat(poke_data[i], other, other)
            
            pokemon = Pokemon(*poke_data)

            data.append(pokemon)

    with open("python solution/models/pokemon.pkl", "wb") as file:
        pickle.dump(data, file)

# Dictionary returning functions
def get_pokemon() -> dict:
    """
    Reads the pokemon pickle file and creates a dictionary of "pokemon name": "Pokemon object" for all pokemon
    """
    file_path = Path("python solution/models/pokemon.pkl")

    # Creates the pokemon pickle file if it does not exist
    if not file_path.exists():
        save_pokemon()
        file_path = Path("python solution/models/pokemon.pkl")

    with file_path.open('rb') as file:
        data = pickle.load(file)

        pokemon_dict = {}
        for pokemon in data:
            pokemon_dict[pokemon.name] = pokemon

        return pokemon_dict
    
# Selection functions
def pokemon_select() -> list[Pokemon]:
    """
    Lets the user input the name of pokemon to make their party and returns 
    those pokemon objects from the pokemon dict
    """
    pokemon = []

    pokemon_dict = get_pokemon()

    while len(pokemon) != 1: # Only 1 pokemon for testing for now
        print("Select a pokemon: ")
        selection = input()
        
        try:
            selection = selection.capitalize()
            # Selects Pokemon object from dictionary
            selected_pokemon = pokemon_dict[selection]
            pokemon.append(selected_pokemon)

        except (KeyError):
            if selection == '':
                print("You must write the name of a pokemon")
            else:
                print("You must write the name of a pokemon from Generation 1")

        else:
            print(f"You selected: {selected_pokemon}!")

    return pokemon