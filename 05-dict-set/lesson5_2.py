person = {"name": "たなべ", "age": 36}

print(person.keys())  # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['たなべ', 36])
print(person.items())  # dict_items([('name', 'たなべ'), ('age', 36)])

# 安全に取得（キーがなければNone）
print(person.get("city"))  # None
