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
    mo.md(r""" """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #PEACH.py（自由帳）

    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 自由帳""")
    return


app._unparsable_cell(
    r"""
     サイコロ実行
    """,
    name="_"
)


@app.cell
def _(mo):
    import random

    dice_roll_result = random.randint(1, 6)
    mo.md(f"サイコロの目: **{dice_roll_result}**")
    return (random,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""LOT６""")
    return


@app.cell
def _(mo, random):
    unique_lottery_numbers_set = set()
    while len(unique_lottery_numbers_set) < 6:
        unique_lottery_numbers_set.add(random.randint(1, 43))
    unique_lottery_numbers = sorted(list(unique_lottery_numbers_set))
    mo.md(f"LOT6の数字: **{', '.join(map(str, unique_lottery_numbers))}**")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""LOT7""")
    return


@app.cell
def _(mo, random):
    def _():
        unique_lottery_numbers_set = set()
        while len(unique_lottery_numbers_set) < 7:
            unique_lottery_numbers_set.add(random.randint(1, 37))
        unique_lottery_numbers = sorted(list(unique_lottery_numbers_set))
        return mo.md(f"LOT7の数字: **{', '.join(map(str, unique_lottery_numbers))}**")


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""> LO6とLOT７の場合ではコード構成が異なります。""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


if __name__ == "__main__":
    app.run()
