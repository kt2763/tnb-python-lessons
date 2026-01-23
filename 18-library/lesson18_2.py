import datetime

# 現在の日時
now = datetime.datetime.now()
print(f"現在時刻: {now}")

# 特定の日時を作成
game_release = datetime.datetime(2025, 12, 25, 10, 0, 0)
print(f"発売日: {game_release}")

# 日付だけ
today = datetime.date.today()
print(f"今日の日付: {today}")

# 時刻だけ
current_time = datetime.datetime.now().time()
print(f"現在時刻(時間のみ): {current_time}")


now = datetime.datetime.now()

# 読みやすい形式に変換
formatted = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(formatted)  # 2025年01月11日 14:30:45

# よく使うフォーマット
print(now.strftime("%Y-%m-%d"))  # 2025-01-11
print(now.strftime("%H:%M"))  # 14:30
print(now.strftime("%Y/%m/%d %H:%M:%S"))  # 2025/01/11 14:30:45

# 現在時刻
now = datetime.datetime.now()

# 7日後
future = now + datetime.timedelta(days=7)
print(f"7日後: {future}")

# 3時間前
past = now - datetime.timedelta(hours=3)
print(f"3時間前: {past}")

# 日数の差を計算
event_date = datetime.datetime(2025, 12, 25)
days_until = (event_date - now).days
print(f"イベントまであと{days_until}日")
