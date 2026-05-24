def process_file(path: str) -> None:
    """with文を使ったファイル処理"""
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
            print(f"内容: {content}")
    except FileNotFoundError:
        print("ファイルが見つかりません")
