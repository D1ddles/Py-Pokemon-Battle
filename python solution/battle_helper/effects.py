import math
from random import choice, randint

from models.models import Pokemon, Move

def before_attack(effect: str, dmg: int, attacking: Pokemon, defending: Pokemon):
    "Effects for moves that happen before the attack, or instead of the attack"

    # Applying status effects
    if effect == "Confuses the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Paralyzes the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Poisons the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Badly poisons the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Causes the target to fall asleep.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    # Raising stat effects
    elif effect == "Raises the user's evasiveness by 1.":
        print(f"{attacking.name}'s Evasiveness rose!")
        attacking.eva.stage += 1
    
    elif effect == "Raises the user's Defense by 1.":
        print(f"{attacking.name}'s Defense rose!")
        attacking.dfs.stage += 1

    elif effect == "Raises the user's Special by 1.":
        print(f"{attacking.name}'s Special rose!")
        attacking.spec.stage += 1

    elif effect == "Raises the user's Attack by 1.":
        print(f"{attacking.name}'s Attack rose!")
        attacking.atk.stage += 1
    
    elif effect == "Raises the user's Defense by 2.":
        print(f"{attacking.name}'s Defense rose greatly!")
        attacking.dfs.stage += 2

    elif effect == "Raises the user's Speed by 2.":
        print(f"{attacking.name}'s Speed rose greatly!")
        attacking.spd.stage += 2

    elif effect == "Raises the user's Special by 2.":
        print(f"{attacking.name}'s Special rose greatly!")
        attacking.spec.stage += 2

    elif effect == "Raises the user's Attack by 2.":
        print(f"{attacking.name}'s Attack rose greatly!")
        attacking.atk.stage += 2

    # Lowering stat effects
    elif effect == "Lowers the target's accuracy by 1.":
        print(f"{attacking.name}'s Accuracy fell!")
        defending.acc.stage += 1

    elif effect == "Lowers the target's Speed by 1.":
        print(f"{defending.name}'s Speed fell!")
        defending.spd.stage -= 1

    elif effect == "Lowers the target's Attack by 1.":
        print(f"{defending.name}'s Attack fell!")
        defending.atk.stage -= 1

    elif effect == "Lowers the target's Defense by 1.":
        print(f"{defending.name}'s Defense fell!")
        defending.dfs.stage -= 1
    
    elif effect == "Lowers the target's Defense by 2.":
        print(f"{defending.name}'s Defense fell greatly!")
        defending.dfs.stage -= 2

    # Set dmg effects
    elif effect == "Random damage from 1 to (user's level*1.5 - 1).":
        dmg = randint(1, 149)

    elif effect == "Damage = 1/2 target's current HP. Hits Ghosts.":
        dmg = math.floor(defending.hp.final / 2)
        if dmg < 1:
            dmg = 1

    elif effect == "Always does 20 HP of damage.":
        dmg = 20

    elif effect == "Deals 40 HP of damage to the target.":
        dmg = 40

    elif effect == "Damage = user's level. Can hit Ghost types.":
        dmg = 100 # all level 100 pokemon

    elif effect == "Damage = user's level. Can hit Normal types.":
        dmg = 100 # all level 100 pokemon

    # Insta-kill effects
    elif effect == "Deals 65535 damage. Fails if target is faster.":
        if attacking.spd.final > defending.spd.final:
            print(f"{attacking.name} is faster than {defending.name}!") # un-faithful
            dmg = 65535
        else:
            dmg = 0

    return dmg, attacking, defending


def during_attack(effect: str, dmg: int, attacking: Pokemon, defending: Pokemon):
    "Effects for moves that happen during the attack"

    if effect == "Target's Def halved during damage. User faints.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
        attacking.hp = 0


    return dmg, attacking, defending


def after_attack(effect: str, dmg: int, attacking: Pokemon, defending: Pokemon):
    "Effects for moves that happen after the attack"

    # Healing effects

    if effect == "User recovers 50% of the damage dealt.":
        heal = math.floor(dmg / 2)
        print(f"{attacking.name} healed {heal} HP!")
        attacking.hp.final += heal
    
    elif effect == "User gains 1/2 HP inflicted. Sleeping target only.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    # Damaging-back effects

    elif effect == "Has 1/4 recoil.":
        ### NOT FAITHFUL IMPLEMENTATION
        recoil = math.floor(dmg / 4)
        print(f"{attacking.name} took {recoil} recoil damage!")
        attacking.hp.final -= recoil

    elif effect == "User takes 1 HP of damage if it misses.":
        if dmg == 0:
            print(f"{attacking.name} took 1 damage for missing!")
            attacking.hp.final -= 1

    elif effect == "User loses 1/2 the HP lost by the target.":
        lost = math.floor(dmg / 2)
        print(f"{attacking.name} lost {lost} HP!")
        attacking.hp.final -= lost

    # Applies status effects

    elif effect == "30% chance to make the target flinch.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
        
    elif effect == "10% chance to make the target flinch.":
        ### NEEDS DOING ###
        if randint(1, 10) == 10:
            pass
        print("UNFINISHED MOVE")

    elif effect == "10% chance to freeze the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "30% chance to burn the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "10% chance to burn the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "10% chance to confuse the target.":
        if randint(1,10) == 10:
            pass
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "10% chance to paralyze the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")
        # if randint(1,10) == 10:

    elif effect == "30% chance to paralyze the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "20% chance to poison the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "40% chance to poison the target.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")
        # if randint(1, 10) > 6:

    # + Multi-hit
    elif effect == "Hits 2 times. Last hit has 20% chance to poison.":
        print("Hit 2 times!")
        dmg *= 2
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")
        # if randint(1,5) == 5:

    # Lowering stat effects

    elif effect == "33% chance to lower the target's Defense by 1.":
        if randint(1,250) > 83:
            print(f"{defending.name}'s Defense fell!")
            defending.dfs.stage -= 1

    elif effect == "33% chance to lower the target's Attack by 1.":
        if randint(1,250) > 83:
            print(f"{defending.name}'s Attack fell!")
            defending.atk.stage -= 1

    elif effect == "33% chance to lower the target's Speed by 1.":
        if randint(1,250) > 83:
            print(f"{defending.name}'s Speed fell!")
            defending.spd.stage -= 1
        
    elif effect == "33% chance to lower the target's Special by 1.":
        if randint(1,250) > 83:
            print(f"{defending.name}'s Special fell!")
            defending.spec.stage -= 1
    
    # Multi-hit effects

    elif effect == "Hits 2 times in one turn.":
        print("Hit 2 times!")
        dmg *= 2
    
    elif effect == "Hits 2-5 times in one turn.":
        random = randint(1,8)
        if random in (1,2,3):
            print("Hit 2 times!")
            dmg *= 2
        elif random in (4,5,6):
            print("Hit 3 times!")
            dmg *= 3
        elif random == 7:
            print("Hit 4 times!")
            dmg *= 4
        elif random == 8:
            print("Hit 5 times!")
            dmg *= 5
    
    # Miscellaneous effects

    elif effect == "User becomes the same type as the target.":
        attacking.type1 = defending.type1
        attacking.type2 = defending.type2
        print(f"{attacking.name} became the types {defending.type1} and {defending.type2}!")

    elif effect == "Resets all stat changes. Removes foe's status.":
         ### STATUSES NEEDS DOING ###
        print("All stat changes reset!")
        attacking.dfs.stage = 0
        attacking.atk.stage = 0
        attacking.spd.stage = 0
        attacking.spec.stage = 0
        defending.dfs.stage = 0
        defending.atk.stage = 0
        defending.spd.stage = 0
        defending.spec.stage = 0
        print("UNFINISHED MOVE")

    elif effect == "User takes 1/4 its max HP to put in a Substitute.":
        ### NEEDS DOING ###
        lost = math.floor(attacking.hp.final / 4)
        print(f"{attacking.name} puts {lost} HP into its Substitute!")
        attacking.hp.final -= lost
        print("UNFINISHED MOVE")

    # Moves that do not have function in trainer battles

    elif effect == "No competitive use.":
        print("Does nothing.")

    elif effect == "Fails when used.":
        print("Move failed.")
        
    elif effect == "Scatters coins.":
        # Coins are not + will not be implemented
        print("Scattered coins!")

    return dmg, attacking, defending


def lasting_effect(effect: str, dmg: int, attacking: Pokemon, defending: Pokemon):
    "Effects that last multiple turns"

    if effect == "Waits 2-3 turns; deals double the damage taken.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
    
    elif effect == "Prevents the target from moving for 2-5 turns.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
        
    elif effect == "For 0-7 turns, disables one of the target's moves.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE") 

    elif effect == "Lasts 3-4 turns. Confuses the user afterwards.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    # Constant attack
    elif effect == "Lasts forever. Raises user's Attack by 1 when hit.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    return dmg, attacking, defending

### UNCATEGORISED MOVES - kept for effect checking ###
# Executes effect
def effect(effect: str, dmg: int, attacking: Pokemon, defending: Pokemon):
    """
    Executes the effect of a move
    """

    if effect == "If hit by Normal/Fighting move, deals 2x damage.":
        ### NEEDS DOING ###
        # requires last move's damage + type
        print("UNFINISHED MOVE")

    elif effect == "Digs underground turn 1, strikes turn 2.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
    
    elif effect == "Flies up on first turn, then strikes the next turn.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Can't move next turn if target or sub is not KOed.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "1/8 of target's HP is restored to user every turn.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")
    
    elif effect == "While active, user's Special is 2x when damaged.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Picks a random move.":
        ### NEEDS DOING ###
        # random_move = choice(list(moves_dict.keys()))
        print("UNFINISHED MOVE")

    elif effect == "Random move known by the target replaces this.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "User uses the target's last used move against it.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "While active, user is protected from stat drops.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Usually goes first.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Charges turn 1. Hits turn 2.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "While active, the user's Defense is doubled.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "User sleeps 2 turns and restores HP and status.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")
    
    elif effect == "Causes the target to become confused.":
        ### STATUSES NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Never misses, even against Dig and Fly.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    elif effect == "Copies target's stats, moves, types, and species.":
        ### NEEDS DOING ###
        print("UNFINISHED MOVE")

    return dmg, attacking, defending