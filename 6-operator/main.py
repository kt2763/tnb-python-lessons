# 論理演算の例

# 論理演算子 not, and, or

a, b, c = True, False, True
print(a and b or c)
print(a and (b or c))
print((a and b) or c)

# ()系は先に書く -> 優先順位が高いものを先に書く
