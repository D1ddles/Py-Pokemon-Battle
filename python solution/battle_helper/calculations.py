import math
from random import randint

from models.models import Pokemon, Move

from .effects import effect

# Battle functions
def damage_calc(move: Move, attacking: Pokemon, defending: Pokemon):
    damage = 0
    
    if move.power:

        # Accuracy check
        accuracy = (move.accuracy*2.55) * attacking.acc.final * defending.eva.final

        if randint(0,255) < accuracy:
            pass  
        else:
            print("Attack missed!")
            return 0, attacking, defending

        # calculating damage multipliers
        if move.category == "Special":
            atk = attacking.atk.final
            dfs = defending.dfs.final
        else:
            atk = attacking.spec.final
            dfs = defending.spec.final
        
        # setting attack types
        atk_type1 = attacking.type1
        atk_type2 = attacking.type2

        # setting defence types
        def_type1 = defending.type1
        def_type2 = defending.type2

        ### Critical hits use the attacker and defender's original stats with no modifications

        # Random crits
        if move.effect == "High critical hit ratio.":
            if randint(0,255) < (defending.spd.base * 100 / 64):
                crit = 2
                print("Critical hit!")

        elif move.effect == "Quarters the user's chance for a critical hit.":
            # Bugged move in Gen 1
            if randint(0,255) < (defending.spd.base * 100 / 2048):
                crit = 2
                print("Critical hit!")

        else:
            if randint(0,255) < (defending.spd.base * 100 / 512):
                crit = 2
                print("Critical hit!")
            else:
                crit = 1

        # STAB (Same Type Attack Bonus) if attack is made by type of the pokemon
        if move.type in [atk_type1, atk_type2]:
            stab = 1.5
        else:
            stab = 1

        # damage calculation
        damage = (((2*100*crit)/5+2)*move.power*atk/dfs)/50+2
        damage *= stab*def_type1.type_effectiveness(move.type)
        if def_type2:
            damage *= def_type2.type_effectiveness(move.type)
        if damage != 1:
            damage *= (randint(217,255)/255) # adds "random"-ness to the damage
        damage = math.floor(damage)

        defending.hp.final -= damage
    
    if move.effect:
        damage, attacking, defending = effect(move.effect, damage, attacking, defending)

    return math.floor(damage), attacking, defending
