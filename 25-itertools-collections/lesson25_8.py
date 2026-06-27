from collections import defaultdict

# 通常のdictだとKeyErrorが起きる
normal_dict = {}
# normal_dict["a"].append(1)  # KeyError

# defaultdictならキーがなくても自動で初期化される
dd = defaultdict(list)
dd["a"].append(1)
dd["a"].append(2)
dd["b"].append(3)
print(dict(dd))  # {'a': [1, 2], 'b': [3]}

# カウンターとして使う
word_count = defaultdict(int)
for word in ["hello", "world", "hello"]:
    word_count[word] += 1
print(dict(word_count))  # {'hello': 2, 'world': 1}
