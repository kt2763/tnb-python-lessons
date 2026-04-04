class A:
    def method(self):
        print("Aのメソッド")


class B:
    def method(self):
        print("Bのメソッド")


class C(A, B):  # AとBの両方を継承
    pass


# どちらのメソッドが呼ばれる?
c = C()
c.method()  # Aのメソッド(左側が優先される)

# MRO(メソッド解決順序)を確認
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
