fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # {'apple', 'banana', 'cherry'} ← 重複が自動で消える

a = {"apple", "banana", "cherry"}
b = {"banana", "melon", "cherry"}

print(a | b)  # {'apple', 'banana', 'cherry', 'melon'}
print(a & b)  # {'banana', 'cherry'}
print(a - b)  # {'apple'}
