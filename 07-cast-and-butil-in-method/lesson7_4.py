# ユーザー入力は文字列で入る
s = input("数字を入力: ")
if s.isdigit():  # 数字かどうかチェック
    n = int(s)  # 文字列→整数にキャスト
    print(n * 2)
else:
    print("数字を入力してください")
