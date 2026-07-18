# #23 例外処理

動画: https://youtu.be/6bg7Ts0ZLYs

`try` / `except` / `else` / `finally` による例外処理、複数の例外の使い分け、`with` 文によるリソース管理、独自例外クラスの定義を扱います。

- `lesson23_1.py` — `try` / `except` の基本（`ValueError` の捕捉）
- `lesson23_2.py` — 複数の `except` でエラー種別ごとに処理を分ける
- `lesson23_3.py` — 例外オブジェクトからメッセージを取得する（`as e`）
- `lesson23_4.py` — `else` 節（例外が起きなかった場合の処理）
- `lesson23_5.py` — `finally` 節を使った後片付け（ファイルのクローズ）
- `lesson23_6.py` — `with` 文で `finally` を省略する書き方
- `lesson23_7.py` — 独自例外クラス（`InsufficientFundsError`）の定義と送出
