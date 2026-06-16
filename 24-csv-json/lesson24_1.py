# NG：closeを忘れるとリソースが解放されない
f = open("sample.txt", encoding="utf-8")
content = f.read()
f.close()

# OK：with文を使うと自動でcloseされる
with open("sample.txt", encoding="utf-8") as f:
    content = f.read()
