# Mentor-Logic Engine (MLE)

**AI家庭教師エンジン：統計学の「思考をデバッグする」**

## 📖 概要

MLEは、統計学の学習における「論理の脱線」を特定し、自律的に指導を行うAI家庭教師エンジンです。

**コア・コンセプト：** 「答えを教えず、思考をデバッグする」

## 🏗️ プロジェクト構造

```
Mentor_Logic_Engine/
├── src/mle/                    # メインパッケージ
│   ├── perception/             # Layer 1: Vision OCR (手書き認識)
│   ├── reasoning/              # Layer 2: Thinking Logic (論理推論)
│   ├── verification/           # Layer 3: Formal Math (数理検証)
│   └── orchestration/          # Layer 4: State Management (状態管理)
├── tests/                      # テストコード
├── data/                       # 統計表データ、サンプル画像
├── models/                     # モデルファイル
├── pyproject.toml              # プロジェクト設定
└── .env.example                # 環境変数テンプレート
```

## 🚀 セットアップ

### 1. 仮想環境の作成

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

### 2. 依存関係のインストール

```bash
# 基本パッケージのみ
pip install -e .

# 開発ツールを含む
pip install -e ".[dev]"

# 全ての依存関係
pip install -e ".[all]"
```

### 3. 環境変数の設定

```bash
cp .env.example .env
# .env を編集してモデルパスなどを設定
```

## 🧪 テスト

```bash
pytest
```

## 📚 開発ロードマップ

| 週 | フェーズ | 内容 |
|---|---|---|
| W1-3 | Perception | Qwen2.5-VL構築、手書きLaTeX抽出 |
| W4-6 | Verification | SymPy等価性判定エンジン |
| W7-9 | Reasoning | LangGraph指導シナリオ |
| W10-12 | Integration | iPad UI、WebSocket通信 |

## 📝 ライセンス

MIT License

## 👤 作成者

Hideki Nakazawa
