from typing import Protocol


class Printable(Protocol):
    """print_info()メソッドを持つ型"""

    def print_info(self) -> None: ...  # passでもOK


# 既存のクラス（Printableを継承していない）
class ExternalUser:
    def print_info(self) -> None:
        print("外部ユーザーの情報")


class Order:
    def print_info(self) -> None:
        print("注文の情報")


def show(item: Printable) -> None:
    """Printableを満たす任意のオブジェクトを受け取る"""
    item.print_info()


# どちらもProtocolを継承していないが、型チェックが通る
show(ExternalUser())  # 外部ユーザーの情報
show(Order())  # 注文の情報
