# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "fizzbuzz-tdd-kata-jousset==0.1.0",
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    from collections import Counter

    import marimo as mo
    import matplotlib.pyplot as plt

    from fizzbuzz_tdd_kata_jousset import fizzbuzz


@app.cell
def _():
    mo.md(r"""
    # FizzBuzz Explorer

    Pick a range below and see how fizzbuzz classifies each number
    in it, both as a list and as a chart of the distribution of
    outputs. This notebook consumes the published fizzbuzz package —
    it does not reimplement the function.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    results = [fizzbuzz(n) for n in range(lo, hi + 1)]
    results
    return (results,)


@app.cell
def _(results):
    counts = Counter("Number" if r.isdigit() else r for r in results)

    fig, ax = plt.subplots()
    ax.bar(
        counts.keys(),
        counts.values(),
        color=["#4c72b0", "#dd8452", "#55a868", "#c44e52"],
    )
    ax.set_ylabel("Count")
    ax.set_title("Distribution of FizzBuzz outputs over the selected range")
    fig
    return


if __name__ == "__main__":
    app.run()
