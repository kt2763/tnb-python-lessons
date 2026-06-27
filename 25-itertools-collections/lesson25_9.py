from collections import deque

dq = deque([1, 2, 3])

# 先頭に追加・末尾に追加
dq.appendleft(0)  # deque([0, 1, 2, 3])
dq.append(4)  # deque([0, 1, 2, 3, 4])

# 先頭から取り出し・末尾から取り出し
print(dq.popleft())  # 0
print(dq.pop())  # 4

# 最大サイズを指定したスライディングウィンドウ
log_buffer = deque(maxlen=3)
for i in range(6):
    log_buffer.append(i)
    print(list(log_buffer))
# [0]
# [0, 1]
# [0, 1, 2]
# [1, 2, 3]  ← 古いものが自動で消える
# [2, 3, 4]
# [3, 4, 5]
