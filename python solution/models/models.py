from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import pickle
from typing import List
from random import randint

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