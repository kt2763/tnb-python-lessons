import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    """一時ディレクトリを作成し、テスト後に削除するfixture"""
    with tempfile.TemporaryDirectory() as d:
        yield Path(d)  # yieldより前がsetup（テスト準備）、後がteardown（後片付け）


def test_write_file(temp_dir):
    file_path = temp_dir / "test.txt"
    file_path.write_text("hello", encoding="utf-8")
    assert file_path.read_text(encoding="utf-8") == "hello"


@pytest.fixture(scope="function")  # デフォルト。テスト関数ごとに作成・破棄
def per_function_fixture():
    return []


@pytest.fixture(scope="module")  # モジュール（ファイル）全体で共有
def per_module_fixture():
    return []


@pytest.fixture(scope="session")  # テストセッション全体で共有（重いセットアップに）
def per_session_fixture():
    return []
