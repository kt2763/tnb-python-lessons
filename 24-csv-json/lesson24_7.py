import csv

# 基本的な読み込み
with open("users.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダー行をスキップ
    for row in reader:
        print(row)
