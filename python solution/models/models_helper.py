def get_type_relationships(type_name: str) -> dict:
    return {
       "Bug": {
            "strong": ["Grass", "Poison", "Psychic"],
            "weak": ["Fighting", "Fire", "Flying", "Ghost"],
            "not_affect": []
        },
        "Dragon": {
            "strong": ["Dragon"],
            "weak": [],
            "not_affect": []
        },
        "Electric": {
            "strong": ["Flying", "Water"],
            "weak": ["Dragon", "Electric", "Grass"],
            "not_affect": ["Ground"]
        },
        "Fighting": {
            "strong": ["Ice", "Normal", "Rock"],
            "weak": ["Bug", "Flying", "Poison", "Psychic"],
            "not_affect": ["Ghost"]
        },
        "Fire": {
            "strong": ["Bug", "Grass", "Ice"],
            "weak": ["Dragon", "Fire", "Rock", "Water"],
            "not_affect": []
        },
        "Flying": {
            "strong": ["Bug", "Fighting", "Grass"],
            "weak": ["Electric", "Rock"],
            "not_affect": []
        },
        "Ghost": {
            "strong": ["Ghost"],
            "weak": [],
            "not_affect": ["Normal", "Psychic"]
        },
        "Grass": {
            "strong": ["Ground", "Rock", "Water"],
            "weak": ["Bug", "Dragon", "Fire", "Flying", "Grass", "Poison"],
            "not_affect": []
        },
        "Ground": {
            "strong": ["Electric", "Fire", "Poison", "Rock"],
            "weak": ["Bug", "Grass"],
            "not_affect": ["Flying"]
        },
        "Ice": {
            "strong": ["Dragon", "Flying", "Grass", "Ground"],
            "weak": ["Ice", "Water"],
            "not_affect": []
        },
        "Normal": {
            "strong": [],
            "weak": ["Rock"],
            "not_affect": ["Ghost"]
        },
        "Poison": {
            "strong": ["Bug", "Grass"],
            "weak": ["Ghost", "Ground", "Poison", "Rock"],
            "not_affect": []
        },
        "Psychic": {
            "strong": ["Fighting", "Poison"],
            "weak": ["Psychic"],
            "not_affect": []
        },
        "Rock": {
            "strong": ["Bug", "Fire", "Flying", "Ice"],
            "weak": ["Fighting", "Ground"],
            "not_affect": []
        },
        "Water": {
            "strong": ["Fire", "Ground", "Rock"],
            "weak": ["Dragon", "Grass", "Water"],
            "not_affect": []
        }
    }.get(type_name, {"strong": [], "weak": [], "not_affect": []})
