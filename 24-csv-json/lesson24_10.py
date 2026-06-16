import json

# Pythonオブジェクト → JSON文字列
data = {"name": "太郎", "age": 30, "skills": ["Python", "SQL"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON文字列 → Pythonオブジェクト
parsed = json.loads(json_str)
print(parsed["name"])
