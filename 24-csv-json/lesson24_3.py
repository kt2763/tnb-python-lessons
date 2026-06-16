# 新規書き込み（既存ファイルは上書き）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("1行目\n")
    f.write("2行目\n")

# 複数行をまとめて書く
lines = ["りんご\n", "バナナ\n", "みかん\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 末尾に追記
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("追記した行\n")
