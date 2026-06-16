# 全体を1つの文字列として読む
with open("sample.txt", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 1行ずつ読む（大きいファイルでもメモリを節約できる）
with open("sample.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())  # 末尾の改行を取り除く

# 全行をリストとして読む
with open("sample.txt", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)  # ['行1\n', '行2\n', '行3\n']
