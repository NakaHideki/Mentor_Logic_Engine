#!/usr/bin/env python3
"""
GeminiVLM のテストスクリプト
実際の画像を使って Gemini API が正しく動くか確認する
"""

from mle.perception.gemini_vlm import GeminiVLM

def main():
    print("🔍 GeminiVLM テスト開始...")
    print()
    
    # GeminiVLM のインスタンス化
    print("1. GeminiVLM を初期化中...")
    vlm = GeminiVLM()
    print("✅ 初期化完了")
    print()
    
    # テスト画像のパス
    image_path = "data/test_equation.png"
    
    # 画像解析を実行
    print(f"2. 画像を解析中: {image_path}")
    result = vlm.predict(image_path)
    print("✅ 解析完了")
    print()
    
    # 結果を表示
    print("📊 結果:")
    print("=" * 50)
    print(result)
    print("=" * 50)
    print()
    print("🎉 テスト成功！")

if __name__ == "__main__":
    main()
