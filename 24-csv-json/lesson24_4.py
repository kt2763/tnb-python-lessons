from pathlib import Path

# パスの作成
p = Path("data") / "users" / "user.txt"
print(p)  # data/users/user.txt（Windowsでは data\users\user.txt）

# ファイル操作
print(p.exists())  # ファイルが存在するか
print(p.is_file())  # ファイルか
print(p.is_dir())  # ディレクトリか
print(p.suffix)  # 拡張子: .txt
print(p.stem)  # 拡張子なしのファイル名: user
print(p.parent)  # 親ディレクトリ: data/users
