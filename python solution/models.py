from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class poke_type:

    name: str
    strong: List[poke_type]
    weak: List[poke_type]
    not_effect: List[poke_type]

    def effective(self, poke_type: poke_type):

        for type in self.strong:
            if type == poke_type:
                return 2.0
            
        for type in self.weak:
            if type == poke_type:
                return 0.5
            
        for type in self.not_effect:
            if type == poke_type:
                return 0


@dataclass
class Pokemon:

    pk: int
    name: str
    type1: poke_type
    type2: poke_type
    hp: int
    atk: int
    dfs: int
    spatk: int
    spdfs: int
    spd: int
    
