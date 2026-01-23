import os

# 現在の作業ディレクトリ
current_dir = os.getcwd()
print(f"現在のディレクトリ: {current_dir}")

# ファイルが存在するかチェック
if os.path.exists("savegame.json"):
    print("セーブデータが見つかりました")
else:
    print("セーブデータがありません")

# ディレクトリが存在するかチェック
if os.path.isdir("data"):
    print("dataフォルダが存在します")

# ディレクトリを作成
if not os.path.exists("saves"):
    os.makedirs("saves")
    print("savesフォルダを作成しました")

# ファイル一覧を取得
files = os.listdir(".")
print(f"ファイル一覧: {files}")
