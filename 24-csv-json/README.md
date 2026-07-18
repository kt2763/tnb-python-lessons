# #24 ファイル操作 CSV, JSON

動画: https://youtu.be/5BQ1FloNMw8

`with` 文によるファイルの読み書き、`pathlib.Path` を使ったパス操作、`csv` / `json` モジュールによる構造化データの読み書きを扱います。

- `lesson24_1.py` — `with` 文の必要性（`close()`忘れとの比較）
- `lesson24_2.py` — テキストファイルの読み込み（`read()` / 1行ずつ / `readlines()`）
- `lesson24_3.py` — テキストファイルの書き込み（上書き・複数行・追記）
- `lesson24_4.py` — `pathlib.Path` によるパスの作成と情報取得
- `lesson24_5.py` — `Path.write_text()` / `read_text()` と `mkdir()`
- `lesson24_6.py` — `Path.iterdir()` / `glob()` / `rglob()` によるファイル検索
- `lesson24_7.py` — `csv.reader` によるCSVの読み込み
- `lesson24_8.py` — `csv.DictReader` による辞書形式でのCSV読み込み
- `lesson24_9.py` — `csv.DictWriter` によるCSVの書き込み
- `lesson24_10.py` — `json.dumps()` / `json.loads()` によるJSON文字列との相互変換
- `lesson24_11.py` — `json.dump()` / `json.load()` によるJSONファイルの読み書き
- `data/` — 読み込みサンプル用のCSV/テキストファイル
