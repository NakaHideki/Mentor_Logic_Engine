from abc import ABC, abstractmethod

"""
Vision Language Model
"""

class VLM(ABC):
    """
    VLM(Vision Language Model)の抽象基底クラス
    全てのVLM(OpenAI, Qwenなど)はこのルールを守らなければならない。
    """

    @abstractmethod
    def predict(self, image_path: str) -> str:
        """
        画像を解析し、Latexなどを返す
        """
        pass

class MockVLM(VLM):
    """
    ダミーのVLM
    """
    def predict(self, image_path: str) -> str:
        #本来はここで画像を読み込んでAIに投げる
        #今回はダミーなので、適当な数式を返す
        return r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}"