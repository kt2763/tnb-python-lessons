import json
from pathlib import Path

config_path = Path("config.json")

# 書き込み
config = {
    "host": "localhost",
    "port": 5432,
    "debug": True,
}
with config_path.open("w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# 読み込み
with config_path.open(encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["host"])  # localhost
print(loaded["port"])  # 5432
