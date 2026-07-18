# #27 pytest, 単体テスト

動画: https://youtu.be/_DlSzo10Kw0

`unittest` と `pytest` の比較、`assert` によるテストの書き方、例外のテスト、フィクスチャ（`fixture`）、パラメータ化テスト（`parametrize`）、正常系・異常系・境界値のテスト設計を扱います。

- `calculator.py` — テスト対象となる `add` / `divide` 関数
- `lesson27_1.py` — `unittest` と `pytest` の書き方の比較
- `lesson27_2.py` — `assert` の基本、`pytest.approx`、`pytest.raises` による例外テスト
- `lesson27_3.py` — `@pytest.fixture` によるテストデータの共有
- `lesson27_4.py` — `yield` を使ったフィクスチャのセットアップ／ティアダウンとスコープ
- `lesson27_5.py` — `@pytest.mark.parametrize` によるパラメータ化テスト
- `lesson27_6.py` — 正常系・異常系・境界値を意識したテスト設計
- `test_calculator.py` — `calculator.py` に対する実際のテストコード
