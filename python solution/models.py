from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from models_helper import get_type_relationships

@dataclass
class Poke_type:

    name: str
    strong: List[Poke_type] = field(default_factory=list) # all types where self is strong against
    weak: List[Poke_type] = field(default_factory=list) # all types where self is weak against
    not_affect: List[Poke_type] = field(default_factory=list) # all types that self cannot affect

    def __post_init__(self):
        # Automatically set relationships using helper
        self.set_relationships()

    def set_relationships(self):
        relationships = get_type_relationships(self.name)
        self.strong = relationships["strong"]
        self.weak = relationships["weak"]
        self.not_affect = relationships["not_affect"]

    def __str__(self):
        return self.name

@dataclass
class Pokemon:

    poke: int
    name: str
    type1: Poke_type
    type2: Poke_type
    hp: int
    atk: int
    dfs: int
    spatk: int
    spdfs: int
    spd: int
    
    def __str__(self):
        return self.name

    def attack_effectiveness(self, move_type: Poke_type):
        """
        Returns damage multiplier based on the type of the move and types of the defending pokemon
        """
        mult = 1
        for type in [self.type1, self.type2]:
            if not type:
                break

            elif type.name in move_type.strong:
                mult *= 2
            elif type.name in move_type.weak:
                mult *= 0.5
            elif type.name in move_type.not_affect:
                mult *= 0

        return mult