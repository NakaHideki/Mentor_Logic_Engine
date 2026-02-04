from mle.perception.vlm import MockVLM

def test_mock_vlm():
    """
    MockVLMが正しく固定のLatexを返すかテスト
    """
    #1.インスタンス化
    vlm = MockVLM()

    #2.実行(ダミーなのでパスはなんでも OK)
    result = vlm.predict("dummy_image.jpg")

    #3.検証 (期待通り答えが返ってきたか？)
    expected = r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}"

    assert result == expected