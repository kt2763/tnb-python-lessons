def read_file(path: str) -> str:
    """ファイルを読み込んで内容を返す"""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {path}")
        return ""
    except PermissionError:
        print(f"読み取り権限がありません: {path}")
        return ""
