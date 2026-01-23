from functools import lru_cache


# キャッシュなしの再帰(遅い)
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


# キャッシュありの再帰(速い!)
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


# 速度比較
import time

start = time.time()
result = fibonacci_slow(30)
print(f"キャッシュなし: {time.time() - start:.3f}秒")

start = time.time()
result = fibonacci_fast(30)
print(f"キャッシュあり: {time.time() - start:.6f}秒")
