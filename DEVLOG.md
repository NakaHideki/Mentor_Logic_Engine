# MLE 開発ログ

このファイルは、MLEプロジェクトの開発過程で発生した問題、解決方法、学習内容を記録するログです。

---

## 2026-02-02 - プロジェクト初期セットアップ

### 📋 目標
- プロジェクト構造の設計と作成
- 開発環境のセットアップ
- 依存関係のインストール

---

### 🎯 完了したこと

#### 1. プロジェクト構造設計（src/レイアウト）
- **決定事項**: 3つの選択肢（src/、フラット、モノリポ）から、src/レイアウトを選択
- **理由**: 長期プロジェクトに適した構造、テストとコードの明確な分離

**作成したディレクトリ構造:**
```
Mentor_Logic_Engine/
├── src/mle/
│   ├── perception/      # Layer 1: Vision OCR (Qwen3-VL-8B)
│   ├── reasoning/       # Layer 2: Thinking Logic
│   ├── verification/    # Layer 3: Formal Math (SymPy)
│   └── orchestration/   # Layer 4: State Management (LangGraph)
├── tests/
├── data/
├── models/
├── pyproject.toml
├── .gitignore
├── .env.example
└── README.md
```

#### 2. 設定ファイルの作成

**pyproject.toml:**
- ビルドシステム: setuptools
- 依存関係管理: pyproject.toml形式（モダンな選択）
- 基本パッケージ: sympy, numpy, python-dotenv
- 開発ツール: pytest, black, ruff, mypy

**学習ポイント:**
- `pyproject.toml` vs `requirements.txt` の違い
- `pyproject.toml` は2026年現在の標準（新規プロジェクトでは60%が採用）
- optional-dependencies で開発用・本番用を分離できる

**.gitignore:**
- Python標準の除外設定
- 仮想環境（venv/）
- 大きなモデルファイル
- 環境変数ファイル（.env）

#### 3. スケルトンコードの作成

各レイヤーに以下を含むスケルトンコードを作成：
- 詳細な日本語docstring
- 型ヒント（type hints）
- TODO マーカー（実装箇所）
- 使用例（Example）

**作成したファイル:**
- `src/mle/perception/vlm.py` - VLMEngine (Qwen3-VL-8B)
- `src/mle/reasoning/thinking.py` - ThinkingEngine
- `src/mle/verification/sympy_engine.py` - SymPyVerifier
- `src/mle/orchestration/graph.py` - StateMachine
- `tests/test_verification/test_sympy_engine.py` - テストスケルトン

---

### ⚠️ 発生した問題と解決方法

#### 問題1: `python` コマンドが見つからない
**エラー:**
```bash
$ which python
python not found
```

**原因:**
- MacOSでは `python` コマンドは存在しない
- Python 3 は `python3` コマンドで実行する

**解決:**
- `python3` を使用する
- システムに Python 3.9.6 がインストール済みであることを確認

**学習:**
- MacOSでは常に `python3` と明示的に書く
- `which python3` で場所を確認: `/usr/bin/python3`

---

#### 問題2: 仮想環境の有効化スクリプトが見つからない
**エラー:**
```bash
$ source venv/activate
source: no such file or directory: venv/activate
```

**原因:**
- 正しいパスは `venv/bin/activate`（`bin/` ディレクトリが必要）

**解決:**
```bash
$ source venv/bin/activate
```

**学習:**
- 仮想環境のactivateスクリプトは `venv/bin/` 内にある
- Windowsでは `venv\Scripts\activate.bat`、Unix系では `venv/bin/activate`

---

#### 問題3: pip の editable install がエラー
**エラー:**
```bash
ERROR: File "setup.py" or "setup.cfg" not found. Directory cannot be installed in editable mode
```

**原因:**
- pip 21.2.4 が古く、pyproject.toml のみでの editable install に対応していない
- pip 21.3 以上が必要

**解決:**
```bash
$ venv/bin/python3 -m pip install --upgrade pip
```

**学習:**
- `pip install -e .` の `-e` は editable mode（編集可能モード）
- コード変更が即座に反映される（開発中は便利）
- シンボリックリンクを作成して、再インストール不要に

---

#### 問題4: Python バージョンの不一致
**エラー:**
```bash
ERROR: Package 'mle' requires a different Python: 3.9.6 not in '>=3.10'
```

**原因:**
- システムの Python: 3.9.6
- pyproject.toml の要求: `>=3.10`

**解決:**
- `pyproject.toml` の `requires-python` を `">=3.9"` に変更
- Python 3.9 でも全ての依存関係は動作する

**学習:**
- プロジェクト要件は環境に合わせて調整可能
- Python 3.9 は 2025年10月にサポート終了（でも学習目的では問題なし）
- 将来的に Python 3.10+ に移行することも可能

---

### 📚 学習した知識

#### 1. pyproject.toml の構造
```toml
[project]
name = "mle"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = [...]  # 必須パッケージ

[project.optional-dependencies]
dev = [...]     # 開発ツール
perception = []  # Layer 1用
reasoning = []   # Layer 2用
all = ["mle[dev,perception,reasoning]"]  # 全部入り
```

**インストール方法:**
- `pip install -e .` - 基本パッケージのみ
- `pip install -e ".[dev]"` - 開発ツール込み
- `pip install -e ".[all]"` - 全部入り

#### 2. 仮想環境 (venv) の仕組み
**なぜ必要？**
- プロジェクトごとに独立したPython環境
- システムのPythonを汚さない
- チームで同じ環境を再現できる

**作成と使用:**
```bash
# 1. 作成（最初の1回）
python3 -m venv venv

# 2. 有効化（ターミナルを開くたびに）
source venv/bin/activate

# 3. プロンプトが (venv) になる
(venv) $ which python
/path/to/project/venv/bin/python

# 4. 無効化
deactivate
```

#### 3. パッケージとモジュール
**`__init__.py` の役割:**
- ディレクトリがPythonパッケージであることを示す
- パッケージレベルのインポートを定義

**例:**
```python
# src/mle/verification/__init__.py
from .sympy_engine import SymPyVerifier
__all__ = ["SymPyVerifier"]
```

これにより以下が可能に：
```python
from mle.verification import SymPyVerifier
```

#### 4. Docker vs venv の選択基準
**このプロジェクトでは venv を選んだ理由:**
1. Mac Studio の GPU (MPS) に直接アクセス必要
2. Dockerは macOS の GPU に対応していない
3. 1人開発なので環境の完全再現の恩恵が少ない
4. モデルファイルが巨大（Dockerイメージが肥大化）

**Dockerが有利なケース:**
- チーム開発
- 本番環境がLinuxサーバー
- 複数サービスの組み合わせ（DB, API, フロントエンド）

---

### ✅ 最終的にインストールされたパッケージ

**基本パッケージ:**
- sympy 1.14.0 - 数式処理（Layer 3で使用）
- numpy 2.0.2 - 数値計算
- python-dotenv 1.2.1 - 環境変数管理

**開発ツール:**
- pytest 8.4.2 - テストフレームワーク
- pytest-cov 7.0.0 - カバレッジ測定
- black 25.11.0 - コードフォーマッター
- ruff 0.14.14 - リンター（高速なコード品質チェック）
- mypy 1.19.1 - 型チェッカー

---

### 🎓 メンターからのアドバイス

#### AI協働ガイドラインの確立
`Guide.md` にAIの役割と作業方針を明記：
- 答えを勝手に出さない
- 必ず実行前に相談
- スケルトンコード提供（実装はユーザーが行う）
- フィードバック重視
- 積極的なブレストと疑問点の共有

#### 学習アプローチ
- 「実践 → 不足知識に気づく → 深掘り学習 → また実践」サイクル
- 電卓やTodoアプリなどのサンプルは作らず、MLEで直接学ぶ
- 必要になったタイミングで学ぶ（Just-in-Time Learning）

---

---

## 2026-02-02 - GitHubリポジトリの接続（進行中）

### � 目標
- ローカルのGitリポジトリとGitHubを接続
- 初回プッシュを完了

---

### ✅ 完了したこと

#### 1. GitHubリポジトリの作成
- **リポジトリURL**: https://github.com/NakaHideki/Mentor_Logic_Engine
- **設定**: Public、README/ライセンス/gitignoreは追加せず（既にローカルにあるため）

#### 2. リモート接続の設定
```bash
git remote add origin https://github.com/NakaHideki/Mentor_Logic_Engine.git
git branch -M main
```

---

### ⚠️ 発生中の問題

#### 問題：GitHub認証エラー（403 Forbidden）
**エラー:**
```bash
$ git push -u origin main
remote: Permission to NakaHideki/Mentor_Logic_Engine.git denied to hidekinakazawa-collab.
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

**原因:**
- GitHubが2021年8月以降、パスワード認証を廃止
- Personal Access Token または SSH鍵が必要

---

### 🔧 解決方法（選択肢）

#### **方法1: Personal Access Token（推奨・簡単）**

**手順:**
1. GitHubでトークンを作成
   - アクセス先: https://github.com/settings/tokens
   - `Tokens (classic)` → `Generate new token (classic)`
   - Note: `MLE Development` など
   - Expiration: `90 days` または `No expiration`
   - スコープ: `repo` にチェック ✓
   - `Generate token` をクリック
   - **⚠️ トークンをコピー（後で見れない！）**

2. プッシュ時に使用
   ```bash
   git push -u origin main
   ```
   - Username: `NakaHideki`
   - Password: `<コピーしたトークン>`（パスワードではない）

3. トークンを保存（任意）
   ```bash
   # macOSのキーチェーンに保存
   git config --global credential.helper osxkeychain
   ```
   
   次回からトークン入力不要になる

**メリット:**
- 5分で完了
- すぐにプッシュできる

**デメリット:**
- トークンの有効期限管理が必要

---

#### **方法2: SSH鍵を設定**

**手順:**
1. SSH鍵を生成
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

2. 公開鍵をGitHubに登録
   - https://github.com/settings/ssh/new
   - `~/.ssh/id_ed25519.pub` の内容をコピー＆ペースト

3. リモートURLをSSHに変更
   ```bash
   git remote set-url origin git@github.com:NakaHideki/Mentor_Logic_Engine.git
   ```

4. プッシュ
   ```bash
   git push -u origin main
   ```

**メリット:**
- 一度設定すれば永続的
- トークン管理不要

**デメリット:**
- 初回セットアップが少し複雑

---

### 📚 学習した知識

#### Gitのリモート接続
```bash
# リモートを追加
git remote add origin <URL>

# リモート確認
git remote -v

# リモート削除
git remote remove origin

# ブランチ名を変更
git branch -M main

# プッシュ（初回）
git push -u origin main
```

#### GitHubの認証方法（2021年以降）
1. **Personal Access Token** - HTTPSで使用
2. **SSH鍵** - SSHプロトコルで使用
3. **GitHub CLI** - `gh auth login`

---

### 📌 次のステップ

1. **Personal Access Token を作成**
2. **git push を実行してGitHubにアップロード**
3. **ブラウザでリポジトリを確認**
4. **以降の開発フロー確立**

---

### 💡 今後のGit作業フロー

```bash
# 1. コード変更後
git add .

# 2. コミット
git commit -m "feat: add something"

# 3. GitHubにプッシュ
git push
```

---

### 💡 今後のログ記入ルール

- 日付ごとにセクションを分ける
- 完了したこと、問題、解決方法、学習内容を記録
- コマンドやエラーメッセージは具体的に記載
- 「なぜそうしたか」の理由も残す
