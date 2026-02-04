# MLE 開発ログ

このファイルは、MLEプロジェクトの開発過程で発生した問題、解決方法、学習内容を記録するログです。

---

## 2026-02-04 - Docker開発環境への移行 🐳

### 📋 目標
- `venv` から `Docker` ベースの開発環境へ移行
- 環境の一貫性確保と将来のAWS展開への準備

### 🎉 今日の成果

#### ✅ 完了したこと
1.  **Docker環境の構築**
    - `Dockerfile`: Python 3.11-slim をベースに作成
    - `compose.yml`: ボリュームマウント（ファイル同期）の設定
    - `.dockerignore`: 不要ファイルの除外設定
2.  **動作検証**
    - `docker compose build`: ビルド成功（`src/`のコピー順序修正済み）
    - `docker compose up`: コンテナ起動確認
    - `docker compose exec app pytest`: コンテナ内でのテスト通過 ✅
    - ファイル同期の確認（Macで作成したファイルをDocker内で実行）

#### 📚 学んだこと
- **Dockerfile**: 環境の「レシピ」（OS, Python, ライブラリ）
- **compose.yml**: 環境の「指揮者」（起動設定、ボリュームマウント）
- **.dockerignore**: 不要なファイルをビルドに含めないための設定
- **docker compose exec**: コンテナ内でコマンドを実行する方法
- **ボリュームマウント**: ホスト（Mac）とコンテナ間のファイル同期の仕組み

---

## 2026-02-02 - プロジェクト初期セットアップ完了 ✅

### 📋 目標
- プロジェクト構造の設計と作成
- 開発環境のセットアップ
- GitHubとの連携

### 🎉 今日の成果

#### ✅ 完了したこと
1. プロジェクト構造の設計と作成（src/レイアウト）
2. 設定ファイルの作成（pyproject.toml, .gitignore, .env.example）
3. 全4層のスケルトンコード作成
4. 仮想環境のセットアップと依存関係インストール
5. Gitリポjトリの初期化
6. **GitHubとの接続成功（SSH鍵認証）** 🎉
7. 初回プッシュ完了

#### 📚 学んだこと
- プロジェクト構造設計（src/レイアウトの選択理由）
- pyproject.toml vs requirements.txt
- 仮想環境（venv）の仕組みと必要性
- Gitの基本（init, add, commit, push, stash, pull）
- GitHubとの連携（SSH vs HTTPS の違い）
- SSH鍵認証のセットアップ
- 複数PCでの開発フロー
- トラブルシューティング（認証エラー、競合解決）

---

## 🖥️ 他のPC（Mac）での作業開始手順

### **初回セットアップ（新しいMac用）**

#### 1. SSH鍵の生成と登録
```bash
# SSH鍵を生成
ssh-keygen -t ed25519 -C "hidenaka82@gmail.com"
# 全てEnterだけ押す（パスフレーズなし）

# 公開鍵をコピー
cat ~/.ssh/id_ed25519.pub
```

**GitHubに公開鍵を登録:**
1. https://github.com/settings/ssh/new にアクセス
2. **Title**: `MLE Work Mac` または `MLE Laptop` など
3. **Key**: コピーした公開鍵を貼り付け
4. **Add SSH key** をクリック

---

#### 2. リポジトリのクローン
```bash
# プロジェクトフォルダへ移動
mkdir -p ~/Projects
cd ~/Projects

# クローン
git clone git@github.com:NakaHideki/Mentor_Logic_Engine.git

# 初回のみ SSH確認が出たら "yes" と入力

# プロジェクトに移動
cd Mentor_Logic_Engine
```

---

#### 3. 開発環境のセットアップ
```bash
# 仮想環境を作成
python3 -m venv venv

# 有効化
source venv/bin/activate

# 依存関係をインストール
pip install -e ".[dev]"

# 環境変数を設定（必要に応じて）
cp .env.example .env
# .env を編集
```

---

### **日常の作業フロー（2台のMacを行き来）**

#### Mac Studio で作業終了時：
```bash
cd /Users/hideki.nakazawa/sandbox/Indivisual\ Project/Mentor_Logic_Engine
source venv/bin/activate

# 作業内容をコミット
git add .
git commit -m "作業内容"
git push
```

#### 他のMacで作業開始時：
```bash
cd ~/Projects/Mentor_Logic_Engine
source venv/bin/activate

# ⚠️ 必ず最初に pull！
git pull

# 作業...
```

#### 他のMacで作業終了時：
```bash
git add .
git commit -m "作業内容"
git push
```

#### Mac Studio で再作業時：
```bash
cd /Users/hideki.nakazawa/sandbox/Indivisual\ Project/Mentor_Logic_Engine
source venv/bin/activate

# ⚠️ 必ず最初に pull！
git pull

# 作業...
```

---

### **⚠️ 重要な注意点**

1. **作業開始時は必ず `git pull`**
   - これを忘れるとコンフリクト（競合）発生
   - 他のPCでの変更を取り込む

2. **作業終了時は必ず `git push`**
   - これを忘れると他のPCで最新版が見れない

3. **`venv/` は各PCで再作成**
   - Gitにコミットされない（`.gitignore`に入っている）
   - 各PCで `python3 -m venv venv` を実行

4. **`.env` も各PCで設定**
   - Gitにコミットされない（秘密情報のため）
   - 各PCで `.env.example` をコピーして編集

---

## 🎯 次回のタスク

1. **他のMacでリポジトリをクローン**（明日予定）
2. **pytest で動作確認**
3. **Layer 3（SymPy検証エンジン）の実装開始**
4. **基本的な数式検証機能の実装**

---

**記録日時**: 2026-02-02
**作業時間**: 約3時間
**次回作業**: 他のMacでのclone + Layer 3実装
