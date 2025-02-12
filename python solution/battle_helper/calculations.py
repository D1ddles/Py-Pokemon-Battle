from random import randint

from models.models import Pokemon
from models.moves import Move

# Battle functions
def damage_calc(move: Move, attacking: Pokemon, defending: Pokemon):

        if hasattr(move, "effect"):
            print(move.effect) #TEMP print() to be removed when functions created

        # calculating damage multipliers
        if move.category == "Special":
            atk = attacking.atk
            dfs = defending.dfs
        else:
            atk = attacking.spec
            dfs = defending.spec
        
        # setting attack types
        type1 = attacking.type1
        type2 = attacking.type2

        # Random crits
        if randint(0, 255) > randint(0, 255):
            crit = 2
        else:
            crit = 1

        # STAB (Same Type Attack Bonus) if attack is made by type of the pokemon
        if move.type in [type1, type2]:
            stab = 1.5
        else:
            stab = 1

        # damage calculation
        damage = ((2*crit+2)*move.power*atk/dfs)/50
        damage += 2*stab*type1.type_effectiveness(move.type)*type2.type_effectiveness(move.type)
        if damage != 1:
            damage *= (randint(217,255)/255) # adds "random"-ness to the damage

        return damage
