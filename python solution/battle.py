from battle_helper.calculations import damage_calc
from battle_helper.player_setup import setup


def attack_select(pokemon):
    "Displays a player's pokemon's available moves, allows them to select one"
    while True:

        print(f"{pokemon.name}'s moves: ")
        for move in pokemon.moves:
            print(move)

        selected = input("Select a move: ").capitalize()

        for move in pokemon.moves:
            if selected == move.name:
                return move
        
        print("Must select an available move")

def battle(attacking_poke, defending_poke):
    
    print(f"{attacking_poke.name} {attacking_poke.name}'s health: {attacking_poke.hp.final}")
    print(f"{defending_poke.name} {defending_poke.name}'s health: {defending_poke.hp.final}")

    move = attack_select(attacking_poke)

    damage, attacking_poke, defending_poke = damage_calc(move, attacking_poke, defending_poke)
    print(f"{attacking_poke} dealt: {damage} damage!")

    return attacking_poke, defending_poke


while True:

    player1, player2 = setup()

    while player1.is_alive() and player2.is_alive():
        
        print(f"{player1.name}'s Turn!")
        player1.selected_poke, player2.selected_poke = battle(player1.selected_poke, player2.selected_poke)

        if not player1.is_alive() or not player2.is_alive():
            break

        print(f"{player2.name}'s Turn!")
        player2.selected_poke, player1.selected_poke = battle(player2.selected_poke, player1.selected_poke)
            
        if not player1.is_alive() or not player2.is_alive():
            break

    if not player1.is_alive():
        print(f"{player2.name} wins!")

    elif not player2.is_alive():
        print(f"{player1.name} wins!")

    break