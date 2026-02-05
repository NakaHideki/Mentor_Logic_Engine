import streamlit as st
import tempfile
import os
import time
from PIL import Image
from streamlit_drawable_canvas import st_canvas

#VLMクラスのインポート
from mle.perception.gemini_vlm import GeminiVLM
from mle.perception.qwen_vlm import QwenVLM

#Streamlitアプリの設定
st.set_page_config(
    page_title = "Mentor Distillation Engine Playground",
    page_icon = "✏️",
    layout = "centered"
)

def main():
    st.title("✏️ Mentor Distillation Engine Playground")
    st.markdown("""
    ## 目的
    iPad/Apple Pencilで数式を書いて、VLMでLaTeX認識します。
    """)

    """
    1. サイドバー:ユーザーがモデル（QwenかGemini）を選べるようにする
    2. ペン設定:ペンの太さ、色を設定できるようにする
    3. キャンバス: 実際に書く部分
    4. ボタン: 推論開始
    5. 結果表示: LaTeXを表示する(経過時間も表示)
    """

    #サイドバー
    st.sidebar.header("⚙️ Configuration")
    model_choice = st.sidebar.radio(
        "VLM Model",
        ["Qwen3-VL (Local)", "Qwen2.5-VL 7B (Local)", "Gemini 2.5 Flash (Cloud)"]
    )
    
    # ペンの設定
    st.sidebar.subheader("Pen Settings")
    stroke_width = st.sidebar.slider("Stroke width", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Stroke color", "#000000")
    
    # フォントサイズ設定
    st.sidebar.subheader("Display Settings")
    math_font_size = st.sidebar.select_slider(
        "Math Font Size",
        options=["tiny", "scriptsize", "footnotesize", "small", "normalsize", "large", "Large", "LARGE", "huge", "Huge"],
        value="large"
    )

    #キャンバス
    canvas_result = st_canvas(
        fill_color = "rgba(255, 255, 255, 0)", # 塗りつぶし色（透明）
        stroke_width = stroke_width, # ペンの太さ
        stroke_color = stroke_color, # ペンの色
        background_color = "#ffffff",  # ← これを追加（白背景）
        height = 400, # キャンバスの高さ
        width = 700,  # ← これを追加（キャンバスの幅）
        drawing_mode = "freedraw", # 自由描画モード
        key = "canvas" # キャンバスのキー
    )

    # 何か描かれたら処理可能にする
    if canvas_result.image_data is not None:
        
        if st.button("🔍 Analyze Logic", type="primary"):
            # キャンバスのデータを画像に変換
            img_data = canvas_result.image_data
            image = Image.fromarray(img_data.astype("uint8"), mode="RGBA")
            
            # 白背景で合成（透明部分を白くする）
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3]) # 3 is alpha channel
            final_image = background

            with st.spinner(f"Analyzing with {model_choice}..."):
                try:
                    # 一時ファイルへ保存
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                        final_image.save(tmp, format="JPEG")
                        tmp_path = tmp.name

                    # 推論
                    start_time = time.time()
                    if model_choice == "Qwen3-VL (Local)":
                         vlm = QwenVLM(model_name="qwen3-vl")
                    elif model_choice == "Qwen2.5-VL 7B (Local)":
                        vlm = QwenVLM(model_name="qwen2.5vl:7b") # 正しいタグを使用
                    else:
                        vlm = GeminiVLM()

                    raw_result = vlm.predict(tmp_path)
                    elapsed_time = time.time() - start_time
                    
                    # LaTeXの整形（余計なテキストを除去）
                    import re
                    def clean_latex(text):
                        # 1. \documentclass などのプレアンブルを除去してdocumentの中身だけ抽出
                        doc_match = re.search(r'\\begin{document}(.*?)\\end{document}', text, re.DOTALL)
                        if doc_match:
                            text = doc_match.group(1)
                        
                        # 2. コードブロック ```latex ... ``` の抽出
                        code_match = re.search(r'```(?:latex)?\s*(.*?)\s*```', text, re.DOTALL)
                        if code_match:
                            return code_match.group(1).strip()
                            
                        # 3. ブロック数式 \[ ... \] の抽出
                        block_match = re.search(r'\\\[(.*?)\\\]', text, re.DOTALL)
                        if block_match:
                            return block_match.group(1).strip()
                            
                        # 4. ドルマーク $$ ... $$ の抽出
                        dollar_match = re.search(r'\$\$(.*?)\$\$', text, re.DOTALL)
                        if dollar_match:
                            return dollar_match.group(1).strip()
                            
                        # 5. インライン数式 $ ... $ の抽出
                        inline_match = re.search(r'\$(.*?)\$', text, re.DOTALL)
                        if inline_match:
                            return inline_match.group(1).strip()
                            
                        # 6. それでもまだ \documentclass が残っていたら強制削除
                        text = re.sub(r'\\documentclass(?:\[.*?\])?\{.*?\}', '', text)
                        text = re.sub(r'\\usepackage(?:\[.*?\])?\{.*?\}', '', text)
                        
                        return text.strip()

                    latex_result = clean_latex(raw_result)
                    
                    # 後始末
                    os.unlink(tmp_path)

                    # 結果表示
                    st.success(f"✅ 解析完了 ( {elapsed_time:.2f} 秒 )")
                    
                    st.subheader("1. LaTeX Output")
                    st.code(latex_result, language="latex")
                    
                    st.subheader("2. Rendered Math")
                    try:
                        # フォントサイズを適用してレンダリング
                        sized_latex = f"\\{math_font_size} {latex_result}"
                        st.latex(sized_latex)
                    except Exception as e:
                        st.warning("⚠️ Could not render LaTeX")
                        st.error(str(e))

                # ターミナルに詳細エラーを表示
                except Exception as e:
                    import traceback
                    traceback.print_exc()  
                    st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
