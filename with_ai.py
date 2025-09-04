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
    # With AI　（自由帳）



    ```
    """
    )
    return


@app.cell
def _():
    def _():
        import marimo as mo
        return mo.md(
            """
        ## geminiを使う

        ![説明テキスト](/assets/IMGSS_gemini.png)

        これは、上記に表示されている画像の説明です。
        """
        )


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""![](/assets/imgss_gemini.png)""")
    return


@app.cell
def _():
    # 四則計算の例
    a = 10
    b = 5

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    print(f"足し算: {a} + {b} = {addition}")
    print(f"引き算: {a} - {b} = {subtraction}")
    print(f"掛け算: {a} * {b} = {multiplication}")
    print(f"割り算: {a} / {b} = {division}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 地図
    ### folium
    """
    )
    return


@app.cell
def _():
    import folium

    # Create a basic Folium map centered at a default location (e.g., [0, 0])
    # You can adjust the location and zoom level as needed
    blank_map = folium.Map(location=[0, 0], zoom_start=2)

    # Return the map object to display it in marimo
    blank_map
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    abc_example = """
    X:1
    T:きらきら星 (Twinkle, Twinkle Little Star)
    M:4/4
    L:1/8
    K:C
    "C"C2G2A2G2 | "F"F2E2D2C2 | "C"G2F2E2D2 | "G7"G2F2E2D2 |
    "C"C2G2A2G2 | "F"F2E2D2C2 ||
    """

    mo.md(f"""
    ## Music-ABC記法

    Music-ABCは、音楽をテキストベースで記述するための記法です。以下に例を示します。

    ```abc
    {abc_example}
    ```

    marimoはMusic-ABC記法を直接楽譜としてレンダリングする機能は持っていませんが、このテキストをコピーして、`abcjs`のような外部のABCレンダリングツールやJavaScriptライブラリを使用することで、楽譜として視覚化することができます。
    """)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## フロー図の例

    marimoはMermaid記法をサポートしており、テキストからフロー図を直接レンダリングできます。

    ```mermaid
    graph TD
        A[開始] --> B{条件A?};
        B -- はい --> C[処理X];
        B -- いいえ --> D[処理Y];
        C --> E[終了];
        D --> E;
    ```

    上記は、Mermaid記法で記述されたシンプルなフロー図の例です。
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # これは見出し1です

    ## これは見出し2です

    ### これは見出し3です

    これは通常の段落です。
    改行するには、行の終わりにスペースを2つ入れます。
    または、単に新しい行を開始します。

    **これは太字のテキストです**
    *これは斜体のテキストです*
    ***これは太字で斜体のテキストです***
    ~~これは取り消し線です~~

    - リストアイテム1
    - リストアイテム2
      - ネストされたリストアイテム
        - さらにネストされたアイテム

    1. 番号付きリストアイテム1
    2. 番号付きリストアイテム2
    3. 番号付きリストアイテム3

    これは[リンクの例](https://www.example.com)です。

    `これはインラインコードです`

    ```python
    # これはコードブロックです
    def hello_marimo():
        print("こんにちは、Marimo！")

    hello_marimo()
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    今日の天気は晴れです！☀️ 素晴らしい一日になりそうですね。😊
    気温は25℃で、風も穏やかです。🍃
    """
    )
    return


if __name__ == "__main__":
    app.run()
