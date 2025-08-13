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

    ###📊 使い方の例

    - データ分析: Marimoを使用して、データフレームを操作し、インタラクティブなビジュアライゼーションを作成できます。

    - 機械学習: モデルのトレーニングや評価を行い、結果をリアルタイムで確認できます。

    ---
    """
    )
    return


if __name__ == "__main__":
    app.run()
