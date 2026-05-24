try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"エラーが発生しました: {e}")
    # エラーが発生しました: division by zero
