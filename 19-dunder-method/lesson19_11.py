class GameSession:
    """ゲームセッション管理"""

    def __init__(self, player_name):
        self.player_name = player_name

    def __enter__(self):
        """with文に入るときに呼ばれる"""
        print(f"=== {self.player_name}のゲーム開始 ===")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """with文を抜けるときに呼ばれる"""
        print(f"=== {self.player_name}のゲーム終了 ===")
        # Falseを返すと例外を再送出、Trueを返すと例外を握りつぶす
        return False


# 使用例
with GameSession("勇者") as session:
    print("冒険中...")
    print("モンスターと戦闘!")

# === 勇者のゲーム開始 ===
# 冒険中...
# モンスターと戦闘!
# === 勇者のゲーム終了 ===
