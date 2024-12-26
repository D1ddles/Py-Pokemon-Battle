from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from random import randint

from models.models_helper import get_type_relationships

@dataclass
class Poke_type:

    name: str
    strong: List[Poke_type] = field(default_factory=list) # list of types where self is strong against
    weak: List[Poke_type] = field(default_factory=list) # list of types where self is weak against
    not_affect: List[Poke_type] = field(default_factory=list) # list of types that self cannot affect

    def __post_init__(self):
        # Automatically set relationships just after initialising
        self.set_relationships()

    def set_relationships(self):
        # Defines relationships between types as specified in helper
        relationships = get_type_relationships(self.name)
        self.strong = relationships["strong"]
        self.weak = relationships["weak"]
        self.not_affect = relationships["not_affect"]

    def __str__(self):
        return self.name
    
    def type_effectiveness(self, move_type: Poke_type) -> int:
        """
        Returns damage multiplier based on the type of an attack
        """
        mult = 1

        if self.name in move_type.strong:
            mult *= 2
        elif self.name in move_type.weak:
            mult *= 0.5
        elif self.name in move_type.not_affect:
            mult *= 0

        return mult

@dataclass
class Pokemon:

    poke: int
    name: str
    type1: Poke_type
    type2: Poke_type
    hp: int 
    atk: int
    dfs: int
    spd: int
    spec: int
    
    def __str__(self):
        return self.name
    
    # Poke_type function "type_effectiveness" is more in line with damage formula
    # def attack_effectiveness(self, move_type: Poke_type):
    #     """
    #     Returns damage multiplier based on the type of the attack and the types of the defending pokemon
    #     """
    #     mult = 1
    #     for type in [self.type1, self.type2]:
    #         if not type:
    #             break

    #         elif type.name in move_type.strong:
    #             mult *= 2
    #         elif type.name in move_type.weak:
    #             mult *= 0.5
    #         elif type.name in move_type.not_affect:
    #             mult *= 0

    #     return mult

@dataclass
class Move:

    name: str
    type: Poke_type
    category: str
    power: int
    accuracy: int
    pp: int
    effect: str

    def __str__(self):
        return self.name
    
    def damage_calc(self, attacking: Pokemon, defending: Pokemon):

        # calculating damage multipliers
        if self.category == "Special":
            atk = attacking.atk
            dfs = defending.dfs
        else:
            atk = attacking.spec
            dfs = defending.spec
        
        type1 = attacking.type1
        type2 = attacking.type2

        if randint(0, 255) > randint(0, 255):
            crit = 2
        else:
            crit = 1

        if self.type in [type1, type2]:
            stab = 1.5
        else:
            stab = 1

        # damage calculation
        damage = ((2*crit+2)*self.power*atk/dfs)/50
        damage += 2*stab*type1.type_effectiveness(self.type)*type2.type_effectiveness(self.type)
        if damage != 1:
            damage *= (randint(217,255)/255) # "random"