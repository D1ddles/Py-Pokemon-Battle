import math
from random import randint

from models.models import Pokemon, Move

from moves import effect

# Battle functions
def damage_calc(move: Move, attacking: Pokemon, defending: Pokemon):
        
        damage = 0
        if move.power:

            # calculating damage multipliers
            if move.category == "Special":
                atk = attacking.atk.real
                dfs = defending.dfs.real
            else:
                atk = attacking.spec
                dfs = defending.spec
            
            # setting attack types
            atk_type1 = attacking.type1
            atk_type2 = attacking.type2

            # setting defence types
            def_type1 = defending.type1
            def_type2 = defending.type2

            # Random crits
            if randint(0, 255) > randint(0, 255):
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

            defending.hp = defending.hp - damage
        
        if move.effect:
            damage = effect(move.effect, damage, attacking, defending)

        return math.floor(damage)
