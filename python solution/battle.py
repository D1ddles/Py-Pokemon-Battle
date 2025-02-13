from battle_helper.pokemon import pokemon_dict, pokemon_select
from battle_helper.moves import moves_dict, moves_select
from battle_helper.calculations import damage_calc

def setup():
    "Allows 2 users to select pokemon and their moves, then prints the moves"
    player1 = pokemon_select(pokemon_dict)
    player2 = pokemon_select(pokemon_dict)

    player1 = moves_select(player1)
    player2 = moves_select(player2)

    print(player1.moves)
    print(player2.moves)

    return player1, player2

def move_select(player):

    while True:

        print(f"Player's moves: ")
        for move in player.moves:
            print(move)

        selected = input("Select a move: ").capitalize()

        for move in player.moves:
            if selected == move.name:
                return move
        
        print("Must select an available move")

def battle(player1, player2):

    print(f"Player 1 {player1.name}'s health: {player1.hp}")
    print(f"Player 2 {player2.name}'s health: {player2.hp}")

    print("Player 1's turn!")
    move = move_select(player1)

    damage = damage_calc(move, player1, player2)
    print(f"Damage dealt: {damage}")

    print(f"Player 1 {player1.name}'s health: {player1.hp}")
    print(f"Player 2 {player2.name}'s health: {player2.hp}")

    print("Player 2's turn!")
    move = move_select(player2)

    damage = damage_calc(move, player2, player1)
    print(f"Damage dealt: {damage}")

    print(f"Player 1 {player1.name}'s health: {player1.hp}")
    print(f"Player 2 {player2.name}'s health: {player2.hp}")


while True:

    player1, player2 = setup()

    while player1.hp > 0 and player2.hp > 0:
        battle(player1, player2)

    if player1.hp > 0:
        print("Player 1 wins!")
        
    elif player2.hp > 0:
        print("Player 2 wins!")

    break