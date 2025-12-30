from mygame import Enemy, Player  # __init__.pyでまとめているので短く書ける

# from mygame.enemy import Enemy
# from mygame.player import Player

# プレイヤーと敵を作成
p = Player("勇者")
e = Enemy("スライム")

p.attack()  # 勇者の攻撃!
e.attack()  # スライムの攻撃!
