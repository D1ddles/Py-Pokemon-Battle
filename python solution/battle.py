from battle_helper.pokemon import pokemon_dict, pokemon_select
from battle_helper.moves import moves_dict, moves_select
from battle_helper.calculations import damage_calc


while True:

    player1 = pokemon_select(pokemon_dict)
    player2 = pokemon_select(pokemon_dict)

    player1 = moves_select(player1)
    player2 = moves_select(player2)

    print(player1.moves)
    print(player2.moves)

    print(damage_calc(player1.moves[0], player1, player2))
    
    break