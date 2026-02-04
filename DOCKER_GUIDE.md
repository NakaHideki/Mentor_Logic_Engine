# 🐳 Docker 開発ガイド

このプロジェクトは Docker を使用して開発を行います。
以下に、よく使うコマンドをまとめました。

## 1. 🚀 起動と終了

### 開発を始める（起動）
バックグラウンドで環境を立ち上げます。
```bash
docker compose up -d
```

### 開発を終える（終了）
コンテナを停止・削除します。
```bash
docker compose down
```

---

## 2. 🛠 開発中の操作

**注意:** すべてのコマンドは `docker compose exec app <コマンド>` の形になります。
「コンテナ(`app`)の中で `<コマンド>` をやってね」という意味です。

### テストを実行する
```bash
docker compose exec app pytest
```

### Pythonスクリプトを実行する
（例：`src/main.py` を実行したい場合）
```bash
docker compose exec app python src/main.py
```

### シェルに入る（コンテナの中に入る）
毎回 `docker compose exec` と打つのが面倒な場合、コンテナの中に入って作業できます。
```bash
docker compose exec app bash
```
（出るときは `exit` と入力）

---

## 3. 🧹 その他

### 環境を再構築する（ビルドし直す）
`Dockerfile` や `pyproject.toml` を変更した場合は実行してください。
```bash
docker compose up -d --build
```

### ログを見る
実行中のコンテナのログ（print出力など）を確認します。
```bash
# ログを表示し続ける（Ctrl+Cで停止）
docker compose logs -f
```
