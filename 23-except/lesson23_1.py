try:
    x = int(input("数字を入力してください: "))
    print(f"入力した値: {x}")
except ValueError:
    print("数字ではありません！")
