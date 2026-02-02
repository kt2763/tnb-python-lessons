class Monster:
    """モンスタークラス"""

    def __init__(self, name):
        self.name = name
        print(f"{self.name}が出現!")

    def __del__(self):
        """オブジェクトが削除されるときに呼ばれる"""
        print(f"{self.name}が消滅...")


# 使用例
monster = Monster("スライム")
# スライムが出現!

del monster  # 明示的に削除
# スライムが消滅...


# スコープを抜けるときも呼ばれる
def battle():
    boss = Monster("ドラゴン")
    # ドラゴンが出現!
    print("戦闘中...")


battle()
# 戦闘中...
# ドラゴンが消滅...(関数を抜けるときに自動削除)
