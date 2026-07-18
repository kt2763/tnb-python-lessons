def add(a: float, b: float) -> float:
    """2つの数を足す"""
    return a + b


def divide(a: float, b: float) -> float:
    """割り算を行う。bがゼロの場合はValueErrorを発生させる"""
    if b == 0:
        raise ValueError("ゼロで割ることはできません")
    return a / b
