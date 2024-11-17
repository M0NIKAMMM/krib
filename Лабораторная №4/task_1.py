import json

INPUT_FILE = 'input.json'


def task() -> float:
    with open(INPUT_FILE, 'r') as f:
        json_data = json.load(f)
        vichislenie = 0
        for line in json_data:
            vichislenie += line['score'] * line['weight']
    return round(vichislenie, 3)


print(task())
