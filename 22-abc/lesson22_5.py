from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self) -> None:
        pass


# 既存のサードパーティ製クラス（変更できない）
class ExternalUser:
    def print_info(self) -> None:
        print("外部ユーザーの情報")


# ExternalUserはPrintableを継承していないので型エラーになる
def show(item: Printable) -> None:
    item.print_info()


user = ExternalUser()
# show(user)  # mypyだと型エラーになる
