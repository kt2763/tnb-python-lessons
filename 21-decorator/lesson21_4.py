def repeat(times):
    """指定した回数だけ関数を繰り返すデコレータ"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"--- {i + 1} 回目 ---")
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def shout(message):
    print(message)


shout("行くぞ！")
