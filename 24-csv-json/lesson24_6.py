from pathlib import Path

data_dir = Path("data")

# ディレクトリ内の全ファイル
for file in data_dir.iterdir():
    print(file)

# 特定の拡張子のファイルだけ
for csv_file in data_dir.glob("*.csv"):
    print(csv_file)

# サブディレクトリを含む再帰的な検索
for txt_file in data_dir.rglob("*.txt"):
    print(txt_file)
