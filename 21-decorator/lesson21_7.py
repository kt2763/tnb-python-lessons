from dataclasses import dataclass


@dataclass
class Player:
    name: str
    level: int
    hp: int
    mp: int


# __init__ / __repr__ / __eq__ が自動生成される

player1 = Player("勇者", 10, 100, 50)
player2 = Player("勇者", 10, 100, 50)

print(player1)  # Player(name='勇者', level=10, hp=100, mp=50)
print(player1 == player2)  # True（__eq__ が自動生成）
