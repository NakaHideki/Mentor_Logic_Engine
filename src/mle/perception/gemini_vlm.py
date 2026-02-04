import os
from dotenv import load_dotenv
import google.generativeai as genai 
from PIL import Image   
from .vlm import VLM

# .envファイルを読み込む
load_dotenv()

class GeminiVLM(VLM):
    """
    Google Gemini Vision APIを使用したVLM実装
    """
    def __init__(self):
        """
        初期化
        """
        #APIキーの設定
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEYが設定されていません")
        
        #APIキーの設定
        genai.configure(api_key=api_key)

        #モデル選択
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        pass

    def predict(self, image_path: str) -> str:
        """
        画像を解析し、Latexなどを返す
        """
        #1.画像を取り込む
        image = Image.open(image_path)

        #2.プロンプトの準備
        prompt = """
        以下の画像を解析し、Latex形式で数式を出力してください。
        """

        #3.APIを叩く
        response = self.model.generate_content([prompt, image])

        #4.結果を返す
        return response.text

