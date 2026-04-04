class Character:
    pass


class Player(Character):
    pass


class Enemy(Character):
    pass


class Boss(Enemy):
    pass


# インスタンスの型チェック
player = Player()
enemy = Enemy()
boss = Boss()

print(isinstance(player, Player))  # True
print(isinstance(player, Character))  # True(親クラスも)
print(isinstance(player, Enemy))  # False

print(isinstance(boss, Boss))  # True
print(isinstance(boss, Enemy))  # True(親クラス)
print(isinstance(boss, Character))  # True(祖先クラス)

# クラスの継承関係チェック
print(issubclass(Player, Character))  # True
print(issubclass(Boss, Enemy))  # True
print(issubclass(Boss, Character))  # True
print(issubclass(Player, Enemy))  # False
