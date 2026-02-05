import pytest
from mle.perception.qwen_vlm import QwenVLM


def test_qwen_vlm_init():
    """
    QwenVLMが正しく初期化されるかテスト
    Note: このテストはqwen3-vlモデルがollamaにインストール済みの場合のみ成功します
    """
    try:
        vlm = QwenVLM()
        assert vlm.model_name == "qwen3-vl"
    except ValueError as e:
        pytest.skip(f"qwen3-vlモデルが未インストール: {e}")


def test_qwen_vlm_invalid_model():
    """
    存在しないモデル名でエラーが発生するかテスト
    """
    with pytest.raises(ValueError) as e:
        QwenVLM(model_name="invalid-model-xyz")
    assert "モデル" in str(e.value)


def test_qwen_vlm_predict_file_not_found():
    """
    存在しない画像ファイルでエラーが発生するかテスト
    """
    try:
        vlm = QwenVLM()
        with pytest.raises(FileNotFoundError) as e:
            vlm.predict("nonexistent_image.jpg")
        assert "画像ファイル" in str(e.value)
    except ValueError:
        pytest.skip("qwen3-vlモデルが未インストール")