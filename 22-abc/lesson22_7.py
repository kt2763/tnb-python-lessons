from typing import Protocol


class Saveable(Protocol):
    """保存できるオブジェクトの型"""

    def save(self, path: str) -> None: ...


class JsonExporter:
    def save(self, path: str) -> None:
        print(f"JSONとして {path} に保存")


class CsvExporter:
    def save(self, path: str) -> None:
        print(f"CSVとして {path} に保存")


def export_data(exporter: Saveable, path: str) -> None:
    """Saveableを満たす任意のエクスポーターで保存する"""
    exporter.save(path)


export_data(JsonExporter(), "output.json")  # JSONとして output.json に保存
export_data(CsvExporter(), "output.csv")  # CSVとして output.csv に保存
