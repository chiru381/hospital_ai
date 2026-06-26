import json


def read_json(path):

    with open(path, "r", encoding="utf-8") as f:

        data = json.load(f)

    return json.dumps(
        data,
        indent=2,
        ensure_ascii=False
    )