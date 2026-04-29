from abc import ABC, abstractmethod


class Animal(ABC):
    """動物の抽象基底クラス"""

    @abstractmethod
    def speak(self) -> str:
        """鳴き声を返す（サブクラスで必ず実装すること）"""
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "ワン！"


class Cat(Animal):
    pass  # speakを実装し忘れた


dog = Dog()
print(dog.speak())  # ワン！

# cat = Cat()  # TypeError: Can't instantiate abstract class Cat
#              # without an implementation for abstract method 'speak'
