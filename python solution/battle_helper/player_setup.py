from .pokemon import pokemon_select
from .moves import moves_select

from models.models import Player

def names_select() -> tuple[str, str]:
    "Allows 2 players to input their names"

    player1_name = input("Player 1, enter your name: ")
    if player1_name == "":
        player1_name = "Player 1"
    
    player2_name = input("Player 2, enter your name: ")
    if player2_name == "":
        player2_name = "Player 2"
        
    return player1_name, player2_name

def setup() -> tuple[Player, Player]:
    "Allows 2 players to select name, pokemon and their moves"

    player1_name, player2_name = names_select()

    player1_pokemon = pokemon_select()
    player2_pokemon = pokemon_select()

    player1 = Player(player1_name, player1_pokemon)
    player2 = Player(player2_name, player2_pokemon)

    for pokemon in player1.pokemon:
        pokemon = moves_select(pokemon)
        
    for pokemon in player2.pokemon:
        pokemon = moves_select(pokemon)

    return player1, player2