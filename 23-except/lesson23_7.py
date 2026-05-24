class InsufficientFundsError(Exception):
    """残高不足を表す例外"""

    def __init__(self, balance: float, amount: float) -> None:
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"残高不足: 残高 {balance}円 に対して {amount}円 の引き出しが要求されました"
        )


class BankAccount:
    """銀行口座"""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        """引き出しを行う"""
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"{amount}円を引き出しました。残高: {self.balance}円")


account = BankAccount(1000)

try:
    account.withdraw(500)  # 500円を引き出しました。残高: 500円
    account.withdraw(800)  # InsufficientFundsError が発生
except InsufficientFundsError as e:
    print(f"エラー: {e}")
