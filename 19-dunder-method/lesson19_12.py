class Countdown:
    """カウントダウンイテレータ"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """イテレータを返す(自分自身)"""
        return self

    def __next__(self):
        """次の値を返す"""
        if self.current <= 0:
            raise StopIteration  # 終了を通知

        self.current -= 1
        return self.current + 1


# 使用例
for num in Countdown(5):
    print(num)
# 5
# 4
# 3
# 2
# 1
