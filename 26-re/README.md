# #26 re 正規表現

動画: https://youtu.be/c8u8z9swroQ

標準ライブラリ `re` を使った正規表現によるパターンマッチングを扱います。基本的なメタ文字から、`search` / `match` / `fullmatch` の違い、置換・分割、グループ・名前付きグループ、フラグまでを扱います。

- `lesson26_1.py` — 正規表現を使う理由（`isdigit()` との比較）
- `lesson26_2.py` — 基本メタ文字（`\d` `{n}` `?` など）と `findall`
- `lesson26_3.py` — アンカー（`^` `$`）と単語境界（`\b`）
- `lesson26_4.py` — メタ文字のエスケープと raw文字列（`r"..."`）の使用
- `lesson26_5.py` — `search` / `match` / `fullmatch` の違い、`sub` による置換、`split` による分割
- `lesson26_6.py` — グループ化（`()`）による部分マッチの取得
- `lesson26_7.py` — 名前付きグループ（`(?P<name>...)`）
- `lesson26_8.py` — フラグ（`IGNORECASE` / `MULTILINE`）
- `meta.md` — 正規表現のメタ文字まとめ
