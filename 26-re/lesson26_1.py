# 正規表現なし：数字だけの文字列かどうかを確認
def is_all_digits(s: str) -> bool:
    return all(c.isdigit() for c in s)


# 正規表現あり：1行で書ける
import re


def is_all_digits_re(s: str) -> bool:
    return bool(re.fullmatch(r"\d+", s))
