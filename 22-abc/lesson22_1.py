class Animal:
    def speak(self):
        pass  # 何もしない


class Dog(Animal):
    def speak(self):
        print("ワン！")


class Cat(Animal):
    pass  # speakを実装し忘れた


dog = Dog()
cat = Cat()

dog.speak()  # ワン！
cat.speak()  # 何も出力されない（エラーにならない！）
