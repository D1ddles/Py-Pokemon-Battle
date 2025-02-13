from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import pickle
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

    for type in types.values():
        type.set_relationships()

    return types

### maybe move ###
def save_types():
    """
    Takes pokemon types dictionary and saves to a pickle file for external use
    """
    types = create_poke_types()

    with open("python solution/models/types.pkl", "wb") as file:
        pickle.dump(types, file)

### MOVE ###
def get_types() -> dict:
    """
    Reads the types pickle file getting a dictionary of "type name": "type object" for all types
    """
    file_path = Path("python solution/models/types.pkl")

    # Creates pickle file if it does not already exist
    if not file_path.exists():
        save_types()
        file_path = Path("python solution/models/types.pkl")

    with file_path.open('rb') as file:
        data = pickle.load(file)

        return data


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
    stage: int = 0 # stage increased/decreased by effects
    
    def set_final(self):
        "Sets the final value based on the stage"
        if self.stage == -6:
            self.real = self.base * 0.25
        elif self.stage == -5:
            self.real = self.base * 0.28
        elif self.stage == -4:
            self.real = self.base * 0.33
        elif self.stage == -3:
            self.real = self.base * 0.4
        elif self.stage == -2:
            self.real = self.base * 0.5
        elif self.stage == -1:
            self.real = self.base * 0.66
        elif self.stage == 0:
            self.real = self.base * 1
        elif self.stage > 0:
            mult = self.stage * 0.5 + 1
            self.real = self.base * mult

    def __str__(self):
        return self.real


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
    