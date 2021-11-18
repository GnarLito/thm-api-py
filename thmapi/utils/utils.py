import json



def to_json(obj):
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=True)