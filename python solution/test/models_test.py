import pytest
from models import Pokemon, Poke_type

@pytest.fixture
def type_objects():
    # define types
    grass = Poke_type("grass")
    fire = Poke_type("fire")
    water = Poke_type("water")
    ghost = Poke_type("ghost")

    # set relationships
    grass.set_relationships()
    fire.set_relationships()
    water.set_relationships()
    ghost.set_relationships()
    
    return {
        "grass": grass,
        "fire": fire,
        "water": water,
        "ghost": ghost,
    }

@pytest.fixture
def poke_objects(type_objects):
    return{
    "bulbasaur" : Pokemon(1, "Bulbasaur", type_objects["grass"],None,45,49,49,65,65,45),
    "charmander" : Pokemon(2, "Charmander", type_objects["fire"],None,39,52,43,60,50,65),
    "squirtle" : Pokemon(3, "Squirtle", type_objects["water"],None,44,48,65,50,64,43),
    "gastly" : Pokemon(4, "Gastly", type_objects["ghost"],None,30,35,30,100,35,80),
    }


def test_dmg_multiplier(type_objects, poke_objects):
    """
    Tests that when calculating the damage multiplier of a move on a pokemon based on types, the correct multiplier is given
    """
    attack_type = type_objects["fire"]
    attacked = poke_objects["bulbasaur"]

    assert attack_type.strong == [type_objects["grass"]]
    assert attacked.type1 == [type_objects["grass"]]

    assert attacked.attack_effectiveness(attack_type) == 2
