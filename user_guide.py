import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # ユーザーガイド

    ## まずはチュートリアルから

    実行するには（uv環境） ...
    ```bash
    uv run marimo tutorial intro
    ```

    ---

    ## 🛠️ 基本的な使い方

    - ノートブックの作成: marimo edit {notebook}.pyを実行して新しいノートブックを作成します。
    - SQLセルの作成: SQLセルを作成するには、空のセルをSQLに変換するか、メニューからSQLセルを選択します。
    - UI要素の追加: スライダーやドロップダウンを追加し、Pythonコードにバインドします。

    ```python
    import marimo as mo

    ### スライダーの作成
    value = mo.ui.slider(label="Select a value", start=0, stop=100)
    ```

    - データのクエリ: SQLセルを使用してデータをクエリし、結果をPythonのデータフレームとして取得します。

    ```python
    df = mo.sql("SELECT * FROM my_table WHERE value > {value}")
    ```

    ###📊 おもな用途

    - データ分析: Marimoを使用して、データフレームを操作し、インタラクティブなビジュアライゼーションを作成できます。

    - 機械学習: モデルのトレーニングや評価を行い、結果をリアルタイムで確認できます。

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### ⚙️ 起動方法の例

    start_marimo.sh を作成しておくと便利です。

    **（事例:私のデバイスの場合）**

    ```PlainText
                            
    #!/bin/sh

    # ホームディレクトリを取得
    HOME_DIR=$HOME

    # marimo-sandbox ディレクトリのパスを作成
    MARIMO_DIR="$HOME_DIR/github/marimo-sandbox"

    # ディレクトリが存在するか確認
    if [ -d "$MARIMO_DIR" ]; then
        # 指定したディレクトリに移動
        cd "$MARIMO_DIR" || exit

        # 実行したいコマンドをここに書く
        # 例: git status を実行
        echo "現在のディレクトリ: $(pwd)"
        uv run marimo edit user_guide.py
    else
        echo "marimo-sandbox ディレクトリは存在しません。"
    fi

    ```

    このスクリプトをファイルに保存し、実行権限を与えてから実行することができます。
    例えば、ファイル名を start_marimo.sh とした場合、以下のコマンドで実行できます。

    **実行権限付与**

    ```PlainText
    chmod +x start_marimo.sh

    ```

    ターミナルでホームディレクトリ（当該shファイルがある）から

    **実行**

    ```bash
    ./start_marimo.sh

    ```

    ---






    """
    )
    return


if __name__ == "__main__":
    app.run()
