def log_decorator(func):
    """実行前後にログを出すデコレータ"""

    def wrapper():
        print("--- 開始 ---")
        func()  # 元の関数を呼ぶ
        print("--- 終了 ---")

    return wrapper


@log_decorator
def greet():
    print("こんにちは！")


greet()
