from __future__ import annotations
from dataclasses import dataclass, field
import math
from typing import List

from models.models_helper import get_type_relationships

# Functions needed for creating pokemon types (due to circular nature)
def create_poke_types() -> dict:
    """
    Creates all Poke_type objects and returns all in a dict
    """
    types = {}
    type_names = ["Bug", "Dragon", "Electric", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Water"]
    
    for name in type_names:
        types[name] = Poke_type(name=name)

    for poke_type in types.values():
        poke_type.set_relationships()

    return types


# Models required for battle
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
        "Defines relationships between types"
        relationships = get_type_relationships(self.name)
        self.strong = relationships["strong"]
        self.weak = relationships["weak"]
        self.not_affect = relationships["not_affect"]

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

    def __str__(self):
        return self.name
    
    
@dataclass
class Stat:

    base: int # base stat value
    real: int  # real stat value based on level (100)
    final: int  # final stat value after stage
    _stage: int = 0 # stage increased/decreased by effects

    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
        self.set_final()
    
    def set_final(self):
        "Sets the final value based on the stage"

        # Checks stage is not over/under cap
        if self._stage < -6:
            print("Nothing happened!")
            self._stage = -6
        elif self._stage > 6:
            print("Nothing happened!")
            self._stage = 6

        # Sets final value
        if self._stage == -6:
            self.final = self.real * 0.25
        elif self._stage == -5:
            self.final = self.real * 0.28
        elif self._stage == -4:
            self.final = self.real * 0.33
        elif self._stage == -3:
            self.final = self.real * 0.4
        elif self._stage == -2:
            self.final = self.real * 0.5
        elif self._stage == -1:
            self.final = self.real * 0.66
        elif self._stage == 0:
            self.final = self.real * 1
        elif self._stage > 0:
            mult = self._stage * 0.5 + 1
            self.final = self.real * mult

        self.final = math.floor(self.final)
        
        # Checks final is not over/under cap
        if self.final < 1:
            self.final = 1
        elif self.final > 999:
            self.final = 999

    def __str__(self):
        return str(self.final)


@dataclass
class Pokemon:

    poke: int
    name: str
    type1: Poke_type
    type2: Poke_type
    hp: Stat
    atk: Stat
    dfs: Stat
    spd: Stat
    spec: Stat

    def __post_init__(self):
        self.acc = Stat(100, 100, 100)
        self.eva = Stat(100, 100, 100)
    
    def __str__(self):
        return self.name
    
    
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
    

@dataclass
class Player:

    name: str
    pokemon: list[Pokemon]

    def __post_init__(self):
        self.selected_poke = self.pokemon[0]

    def is_alive(self):
        "Checks if all player's pokemon are alive"
        for poke in self.pokemon:
            if poke.hp.final > 0:
                return True
        return False

    def __str__(self):
        return self.name