import re

# \d+ : 1桁以上の数字
re.findall(r"\d+", "電話番号: 090-1234-5678")
# ['090', '1234', '5678']

# \d{4} : ちょうど4桁の数字
re.findall(r"\d{4}", "電話番号: 090-1234-5678")
# ['1234', '5678']

# colou?r : colour または color
re.findall(r"colou?r", "I like color and colour")
# ['color', 'colour']
