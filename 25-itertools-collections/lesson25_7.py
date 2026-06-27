from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counter = Counter(words)
print(counter)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# 最も多い上位N件
print(counter.most_common(2))
# [('apple', 3), ('banana', 2)]

# 文字の頻度を数える
char_count = Counter("programming")
print(char_count)
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
