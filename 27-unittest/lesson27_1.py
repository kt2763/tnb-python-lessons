# unittest（標準ライブラリ）
import unittest


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 2, 3)


# pytest（シンプルで読みやすい）
def test_add():
    assert 1 + 2 == 3
