import sys

# Pythonのバージョン
print(f"Pythonバージョン: {sys.version}")

# プラットフォーム情報
print(f"OS: {sys.platform}")


# プログラムを終了
def game_over():
    print("ゲームオーバー")
    sys.exit()  # プログラム終了


# コマンドライン引数
# python game.py player1 hard
if len(sys.argv) > 1:
    player_name = sys.argv[1]
    difficulty = sys.argv[2] if len(sys.argv) > 2 else "normal"
    print(f"プレイヤー: {player_name}, 難易度: {difficulty}")
