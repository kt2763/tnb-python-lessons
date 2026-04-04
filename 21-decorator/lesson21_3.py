import time


def timer(func):
    """実行時間を計測するデコレータ"""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__}: {elapsed:.4f}秒")
        return result

    return wrapper


@timer
def heavy_calc():
    total = 0
    for i in range(1_000_000):
        total += i
    return total


heavy_calc()
