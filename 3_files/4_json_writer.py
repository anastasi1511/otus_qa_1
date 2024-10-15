import json

data = {
    "users": [
        {"Name": "Dominator", "skill": 100, "gold": 99999, "weapons": ['Sword', 'Atomic Laser'], "alive": True},
        {"Name": "Looser", "skill": 1, "gold": -100000, "weapons": [None, None, None], "alive": False},
    ]
}



with open("example.json", "a") as f:
    json.dump(data, f, indent=4)

