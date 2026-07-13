import re

# IGNORECASE
print(re.findall(r"hello", "Hello HELLO hello", re.IGNORECASE))
# ['Hello', 'HELLO', 'hello']

# MULTILINE
text = "apple\nbanana\napricot"
print(re.findall(r"^a\w+", text, re.MULTILINE))
# ['apple', 'apricot']（各行の先頭が対象）
