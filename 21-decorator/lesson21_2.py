def my_decorator(func):
    """どんな関数にも使えるデコレータ"""

    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} を実行します")
        result = func(*args, **kwargs)  # 元の関数に引数をそのまま渡す
        print("[LOG] 完了")
        return result  # 戻り値も忘れずに返す

    return wrapper


@my_decorator
def add(a, b):
    return a + b


@my_decorator
def greet(name, greeting="こんにちは"):
    return f"{greeting}、{name}さん！"


print(add(3, 5))
print(greet("太郎", greeting="おはよう"))
