fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
fruits[1] = "orange"  # 要素の変更
fruits.append("melon")  # 末尾に追加
print(fruits)  # ['apple', 'orange', 'cherry', 'melon']

fruits.remove("apple")  # 要素を削除
print(fruits)  # ['orange', 'cherry', 'melon']
