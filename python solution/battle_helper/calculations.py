import math
from random import randint

from models.models import Pokemon
from models.moves import Move

# Move functions
def absorb(dmg, attacking, defending):
    "User recovers half the HP inflicted on opponent."
    attacking.hp += math.floor(dmg/2)

# Battle functions
def damage_calc(move: Move, attacking: Pokemon, defending: Pokemon):

        if hasattr(move, "effect"):
            print(move.effect) ### TEMP print() to be removed when functions created

        # calculating damage multipliers
        if move.category == "Special":
            atk = attacking.atk
            dfs = defending.dfs
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
        
        if move.effect == "User recovers half the HP inflicted on opponent.":
            absorb(damage, attacking, defending)

        return math.floor(damage)
