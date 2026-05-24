def divide(a: float, b: float) -> float | None:
    """割り算を行う。ゼロ除算の場合はNoneを返す"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("ゼロで割ることはできません")
        return None
    else:
        print("計算成功！")
        return result


print(divide(10, 2))  # 計算成功！ → 5.0
print(divide(10, 0))  # ゼロで割ることはできません → None
