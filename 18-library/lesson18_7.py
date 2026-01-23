import time

# 現在のUnixタイムスタンプ
timestamp = time.time()
print(f"タイムスタンプ: {timestamp}")

# プログラムを一時停止(秒単位)
print("3秒待ちます...")
time.sleep(3)
print("再開!")

# 処理時間の測定
start = time.time()

# 何か重い処理
total = 0
for i in range(1000000):
    total += i

end = time.time()
elapsed = end - start
print(f"処理時間: {elapsed:.3f}秒")
