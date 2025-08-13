# marimo-sandbox

## 🐍 Marimo とは

Marimoは、PythonとSQLを統合したオープンソースのリアクティブノートブック環境です。
従来のノートブックの問題を解決し、データ分析や機械学習のプロジェクトにおいて再現性とインタラクティビティを重視しています。


## 🚀 主な機能

- リアクティブプログラミング: セルを実行すると、Marimoはそのセルに依存する他のセルを自動的に実行します。これにより、手動でセルを再実行する必要がなくなり、エラーを防ぎます。
- Gitフレンドリー: ノートブックはプレーンなPythonファイル（.py）として保存されるため、Gitによるバージョン管理が容易です。これにより、変更点の追跡や管理がしやすくなります。
- インタラクティブUI要素: スライダーやドロップダウンなどのUIコンポーネントを使用して、ユーザーインタラクションを可能にします。これらの要素は、関連するセルに値の変更を伝播し、結果を動的に更新します。
- AI支援コード補完: GeminiやOllamaなどの大規模言語モデルを利用したコード補完機能があり、開発者の生産性を向上させます。
- SQLとの統合: Pythonの変数に依存するSQLクエリを作成し、データフレームやデータベースに対して実行できます。

---

### 📦 通常のインストール方法

Marimoをインストールするには、以下のコマンドを使用します。
（仮想環境でインストールする：推奨）

```bash
pip install marimo
```
または、推奨される依存関係を含めてインストールするには：
```bash
pip install marimo[recommended]
```

---

### 📦 このリポジトリを利用する場合

- このリポジトリをクローンします。

当該プロジェクトのディレクトリで次を実行します
（uvが導入されていることを前提にしています）

```bash
uv sync
```

---

### 📦 marimo の起動（初回）

```bash
uv run marimo edit user_guide.py
```

### 📦 marimo の起動（初回以降）

```bash
uv run marimo edit *******.py
```

---

[Marimo README_Japanese](https://github.com/marimo-team/marimo/blob/main/README_Japanese.md)


[molab](https://molab.marimo.io/notebooks)

---
ライセンス

MIT License

貢献

プルリクエストやイシューの報告を歓迎?します！

更新履歴

v0.1.0

- 初期リリース
- marimo の紹介
- starter kit （user_guide.py）ほか

---

<svg xmlns="http://www.w3.org/2000/svg" width="200" height="50" viewBox="0 0 200 50">
  <a href="https://github.com/watanabe3tipapa/marimo-sandbox" target="_blank">
    <rect width="200" height="50" rx="10" fill="#24292e"/>
    <text x="50%" y="50%" alignment-baseline="middle" text-anchor="middle" fill="#ffffff" font-size="20" font-family="Arial">GitHub Repository</text>
  </a>
</svg>


