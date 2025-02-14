from battle_helper.pokemon import pokemon_dict, pokemon_select
from battle_helper.moves import moves_dict, moves_select
from battle_helper.calculations import damage_calc

def setup():
    "Allows 2 players to select pokemon and their moves"
    player1 = pokemon_select(pokemon_dict)
    player2 = pokemon_select(pokemon_dict)

    for pokemon in player1:
        pokemon = moves_select(pokemon, moves_dict)
        
    for pokemon in player2:
        pokemon = moves_select(player2, moves_dict)

    return player1, player2

def attack_select(pokemon):
    "Displays a player's pokemon's available moves, allows them to select one"
    while True:

        print(f"Player 1 {pokemon.name}'s moves: ")
        for move in pokemon.moves:
            print(move)

        selected = input("Select a move: ").capitalize()

        for move in pokemon.moves:
            if selected == move.name:
                return move
        
        print("Must select an available move")

def battle(player1, player2):

    print(f"Player 1 {player1.name}'s health: {player1.hp.final}")
    print(f"Player 2 {player2.name}'s health: {player2.hp.final}")

    print("Player 1's turn!")
    move = attack_select(player1)

    damage, player1, player2 = damage_calc(move, player1, player2)
    print(f"Damage dealt: {damage}")

    print(f"Player 1 {player1.name}'s health: {player1.hp.final}")
    print(f"Player 2 {player2.name}'s health: {player2.hp.final}")

    print("Player 2's turn!")
    move = attack_select(player2)

    damage, player2, player1 = damage_calc(move, player2, player1)
    print(f"Damage dealt: {damage}")

    print(f"Player 1 {player1.name}'s health: {player1.hp.final}")
    print(f"Player 2 {player2.name}'s health: {player2.hp.final}")


while True:

    player1, player2 = setup()

    while player1[0].hp.final > 0 and player2[0].hp.final > 0:
        battle(player1[0], player2[0])

    if player1[0].hp.final > 0:
        print("Player 1 wins!")

    elif player2[0].hp.final > 0:
        print("Player 2 wins!")

    break