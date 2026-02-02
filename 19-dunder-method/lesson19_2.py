class Singleton:
    """シングルトンパターン(インスタンスを1つだけに制限)"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("新しいインスタンスを作成")
            cls._instance = super().__new__(cls)
        else:
            print("既存のインスタンスを返す")
        return cls._instance


# 何度作っても同じインスタンス
obj1 = Singleton()  # 新しいインスタンスを作成
obj2 = Singleton()  # 既存のインスタンスを返す
print(obj1 is obj2)  # True
