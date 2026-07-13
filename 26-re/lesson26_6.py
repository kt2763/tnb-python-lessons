import re

# 日付パターン: YYYY-MM-DD
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"

m = re.search(date_pattern, "今日は 2026-04-08 です")
if m:
    print(m.group(0))  # 2026-04-08（マッチ全体）
    print(m.group(1))  # 2026（年）
    print(m.group(2))  # 04（月）
    print(m.group(3))  # 08（日）
