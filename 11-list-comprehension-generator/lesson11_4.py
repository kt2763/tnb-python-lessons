import sys

big_list = [i for i in range(1_000_000)]
big_gen = (i for i in range(1_000_000))
print(sys.getsizeof(big_list))  # 大きい
print(sys.getsizeof(big_gen))  # 小さい
