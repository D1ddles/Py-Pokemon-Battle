def get_type_relationships(type_name: str) -> dict:
    return {
        "Normal": {
            "strong": [],
            "weak": ["Fighting"],
            "not_affect": []
        },
        "Fire": {
            "strong": ["Grass", "Bug", "Ice", "Steel"],
            "weak": ["Water", "Rock", "Fire"],
            "not_affect": []
        },
        "Water": {
            "strong": ["Fire", "Ground", "Rock"],
            "weak": ["Water", "Electric"],
            "not_affect": []
        },
        "Electric": {
            "strong": ["Water", "Flying"],
            "weak": ["Electric", "Ground"],
            "not_affect": []
        },
        "Grass": {
            "strong": ["Water", "Ground", "Rock"],
            "weak": ["Fire", "Grass", "Poison", "Flying", "Bug"],
            "not_affect": []
        },
        "Ice": {
            "strong": ["Grass", "Ground", "Flying", "Dragon"],
            "weak": ["Fire", "Water", "Ice", "Steel"],
            "not_affect": []
        },
        "Fighting": {
            "strong": ["Normal", "Ice", "Rock", "Bug", "Steel"],
            "weak": ["Flying", "Psychic", "Fairy"],
            "not_affect": ["Ghost"]
        },
        "Poison": {
            "strong": ["Grass", "Fairy"],
            "weak": ["Poison", "Ground", "Ghost"],
            "not_affect": []
        },
        "Ground": {
            "strong": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "weak": ["Grass", "Ice", "Water"],
            "not_affect": ["Flying"]
        },
        "Flying": {
            "strong": ["Grass", "Fighting", "Bug"],
            "weak": ["Electric", "Rock", "Steel"],
            "not_affect": []
        },
        "Psychic": {
            "strong": ["Fighting", "Poison"],
            "weak": ["Psychic"],
            "not_affect": ["Ghost"]
        },
        "Bug": {
            "strong": ["Grass", "Psychic", "Dark"],
            "weak": ["Fire", "Fighting", "Flying", "Ghost", "Steel"],
            "not_affect": []
        },
        "Rock": {
            "strong": ["Fire", "Ice", "Flying", "Bug"],
            "weak": ["Fighting", "Ground", "Steel", "Water"],
            "not_affect": []
        },
        "Ghost": {
            "strong": ["Psychic", "Ghost"],
            "weak": ["Ghost"],
            "not_affect": ["Normal"]
        },
        "Dragon": {
            "strong": ["Dragon"],
            "weak": ["Steel", "Fairy"],
            "not_affect": []
        },
        "Dark": {
            "strong": ["Psychic", "Ghost"],
            "weak": ["Fighting", "Fairy"],
            "not_affect": []
        },
        "Steel": {
            "strong": ["Ice", "Rock", "Fairy"],
            "weak": ["Fire", "Fighting", "Ground"],
            "not_affect": []
        },
        "Fairy": {
            "strong": ["Dragon", "Fighting", "Dark"],
            "weak": ["Fire", "Poison", "Steel"],
            "not_affect": []
        }
    }.get(type_name, {"strong": [], "weak": [], "not_affect": []})

def write_pickle():
    pass