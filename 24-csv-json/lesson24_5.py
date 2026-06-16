from pathlib import Path

path = Path("output.txt")

# 書き込み（1行で書ける）
path.write_text("こんにちは\n世界\n", encoding="utf-8")

# 読み込み（1行で読める）
content = path.read_text(encoding="utf-8")
print(content)

# ディレクトリ作成（存在していてもエラーにしない）
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)
