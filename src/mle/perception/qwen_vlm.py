import ollama
from pathlib import Path
from PIL import Image
from .vlm import VLM


class QwenVLM(VLM):
    """
    Qwen3-VL Vision Language Modelをollamaで使用したVLM実装
    """

    def __init__(self, model_name: str = "qwen3-vl"):
        """
        初期化
        Args:
            model_name: 使用するQwenモデル名（デフォルト: qwen3-vl）
        """
        self.model_name = model_name
        
        # モデルの存在確認
        try:
            ollama.show(model_name)
        except Exception as e:
            raise ValueError(
                f"モデル '{model_name}' が見つかりません。"
                f"'ollama pull {model_name}' を実行してください。\n"
                f"エラー詳細: {e}"
            )

    def predict(self, image_path: str) -> str:
        """
        画像を解析し、LaTeX形式で数式を返す
        Args:
            image_path: 解析する画像のパス
        Returns:
            LaTeX形式の数式文字列
        """
        # 1. 画像パスの存在確認
        image_path_obj = Path(image_path)
        if not image_path_obj.exists():
            raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
        
        # 2. 画像の検証
        try:
            img = Image.open(image_path)
            img.verify()
        except Exception as e:
            raise ValueError(f"無効な画像ファイルです: {e}")
        
        # 3. 画像をバイナリで読み込む
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        
        # 4. Ollamaにリクエストを送信
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": "この画像に含まれる数式をLaTeX形式で出力してください。",
                        "images": [image_bytes]
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            raise RuntimeError(f"Ollamaの推論中にエラーが発生しました: {e}")