import re

date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

m = re.search(date_pattern, "今日は 2026-04-08 です")
if m:
    print(m.group("year"))  # 2026
    print(m.group("month"))  # 04
    print(m.group("day"))  # 08
    print(m.groupdict())  # {'year': '2026', 'month': '04', 'day': '08'}
