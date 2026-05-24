def process_file(path: str) -> None:
    """ファイルを処理する"""
    f = None
    try:
        f = open(path, encoding="utf-8")
        content = f.read()
        print(f"内容: {content}")
    except FileNotFoundError:
        print("ファイルが見つかりません")
    finally:
        if f:
            f.close()
            print("ファイルを閉じました")
