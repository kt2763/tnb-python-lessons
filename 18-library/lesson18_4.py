import json

# JSON文字列からPythonオブジェクトへ
json_string = '{"name": "スライム", "hp": 50}'
enemy_data = json.loads(json_string)
print(enemy_data["name"])  # スライム

# Pythonオブジェクトから JSON文字列へ
data = {"score": 1000, "rank": "A"}
json_output = json.dumps(data)
print(json_output)  # {"score": 1000, "rank": "A"}
