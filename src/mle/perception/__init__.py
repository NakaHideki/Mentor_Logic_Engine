"""
Layer 1: Perception (Vision OCR)

手書き数式をLaTeXに変換するVLMエンジン
使用モデル: Qwen3-VL-8B
"""

from .vlm import VLMEngine

__all__ = ["VLMEngine"]
