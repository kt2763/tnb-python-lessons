from abc import ABC, abstractmethod


class Config(ABC):
    """設定の抽象クラス"""

    @property
    @abstractmethod
    def name(self) -> str:
        """設定の名前"""
        pass


class AppConfig(Config):
    @property
    def name(self) -> str:
        return "AppConfig"


config = AppConfig()
print(config.name)  # AppConfig
