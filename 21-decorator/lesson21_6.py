class GameUtils:
    game_name = "RPGアドベンチャー"

    @staticmethod
    def calc_damage(attack, defense):
        """self もクラスも不要な処理"""
        return max(1, attack - defense)

    @classmethod
    def create_default_player(cls):
        """クラス変数にアクセスしたいとき"""
        print(f"{cls.game_name}のプレイヤーを作成")
        return {"name": "勇者", "hp": 100}


# インスタンス不要で呼び出せる
print(GameUtils.calc_damage(50, 20))  # 30
GameUtils.create_default_player()
