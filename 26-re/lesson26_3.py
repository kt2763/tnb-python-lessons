import re

# ^ : 先頭から始まる
re.findall(r"^\d+", "123abc")  # ['123']
re.findall(r"^\d+", "abc123")  # []（先頭が数字でない）

# $ : 末尾で終わる
re.findall(r"\d+$", "abc123")  # ['123']

# \b : 単語の境界
re.findall(r"\bcat\b", "cat concatenate scatter")
# ['cat']（catだけ。concatenateやscatterの中のcatは除外）
