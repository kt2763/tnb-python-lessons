from pathlib import Path

# 現在のディレクトリ
current = Path.cwd()
print(f"現在のディレクトリ: {current}")

# パスの結合(演算子で直感的に書ける)
save_dir = Path("game_data") / "saves" / "player1.json"
print(save_dir)  # game_data/saves/player1.json

# ホームディレクトリ
home = Path.home()
print(f"ホーム: {home}")

# ファイルの存在確認
if save_dir.exists():
    print("ファイルが存在します")

# ディレクトリかファイルか判定
if save_dir.is_file():
    print("ファイルです")
elif save_dir.is_dir():
    print("ディレクトリです")

# ファイル名・拡張子の取得
path = Path("data/config.json")
print(f"ファイル名: {path.name}")  # config.json
print(f"拡張子: {path.suffix}")  # .json
print(f"拡張子なし: {path.stem}")  # config
print(f"親ディレクトリ: {path.parent}")  # data
