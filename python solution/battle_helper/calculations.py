import math
from random import randint

from models.models import Pokemon, Move

from .effects import effect, before_attack, after_attack

# Battle functions
def damage_calc(move: Move, attacking: Pokemon, defending: Pokemon):
    damage = 0

    if move.accuracy:
        # Accuracy check
        accuracy = (move.accuracy*2.55) * attacking.acc.final * defending.eva.final
        # limits accuracy to 255
        if accuracy > 255:
            accuracy = 255

        if randint(0,255) < accuracy:
            pass  
        else:
            print("Attack missed!")
            return 0, attacking, defending
        
    damage, attacking, defending = before_attack(move.effect, damage, attacking, defending)

    if move.power:

        # calculating damage multipliers
        if move.category == "Special":
            atk = attacking.spec.final
            dfs = defending.spec.final
        else:
            atk = attacking.atk.final
            dfs = defending.dfs.final

        # setting attack types
        atk_type1 = attacking.type1
        atk_type2 = attacking.type2

        # setting defence types
        def_type1 = defending.type1
        def_type2 = defending.type2

        

        # Critical hits use the attacker and defender's original stats with no modifications
        crit = 1
        if move.effect == "High critical hit ratio.":
            if randint(0,255) < min(8 * defending.spd.base / 2, 255):
                atk = attacking.atk.real
                dfs = defending.dfs.real
                crit = 2
                print("Critical hit!")

        elif move.effect == "Quarters the user's chance for a critical hit.":
            # Bugged effect in Gen 1
            if randint(0,255) < (defending.spd.base / 8):
                atk = attacking.atk.real
                dfs = defending.dfs.real
                crit = 2
                print("Critical hit!")

        else:
            if randint(0,255) < (defending.spd.base / 2):
                atk = attacking.atk.real
                dfs = defending.dfs.real
                crit = 2
                print("Critical hit!")

        # STAB (Same Type Attack Bonus) if attack is made by same type of the pokemon
        if move.type in [atk_type1, atk_type2]:
            stab = 1.5
        else:
            stab = 1

        # type effectiveness multipliers
        type1_mult = def_type1.type_effectiveness(move.type)
        if def_type2:
            type2_mult = def_type2.type_effectiveness(move.type)
        else:
            type2_mult = 1

        # damage calculation
        damage = (((2*100*crit)/5+2)*move.power*atk/dfs)/50+2
        damage *= stab*type1_mult*type2_mult
        if damage != 1:
            damage *= (randint(217,255)/255) # adds "random"-ness to the damage
        damage = math.floor(damage)

    print(f"{attacking} dealt: {damage} damage!")
    defending.hp.final -= damage

    damage, attacking, defending = after_attack(move.effect, damage, attacking, defending)
    
    ### OLD ###
    if move.effect:
        damage, attacking, defending = effect(move.effect, damage, attacking, defending)

    return attacking, defending
