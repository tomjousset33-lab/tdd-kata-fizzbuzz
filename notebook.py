# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.24.2",
#     "pytest==9.1.1",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import pytest


@app.cell
def _():
    mo.md(r"""
    # TDD Demo: FizzBuzz with marimo

    This notebook illustrates the **Red → Green → Refactor** cycle of
    Test-Driven Development. Each section below corresponds to a
    development step where we **grow the contract** of the
    `fizzbuzz` function one test at a time.

    You can run the tests in two ways:

    1. **Inside marimo**: cells whose name starts with `test_`
       are automatically detected and run by pytest.
    2. **From the command line**:
       ```bash
       uv run pytest tdd_fizzbuzz_marimo_en.py
       ```
    """)
    return


@app.cell
def _():
    mo.md(r"""
    ## Step 1 — Red: first test, minimal contract

    Before writing a single line of `fizzbuzz`, we write the simplest
    possible test: for input `1`, we expect the output `"1"`.
    This test would fail if the function didn't exist yet
    (`NameError`) — that's the **Red** phase.

    We then write the **minimal** code that makes this test pass:
    simply return `str(n)`.
    """)
    return


@app.function
def fizzbuzz_v1(n):
    return str(n)


@app.cell
def test_v1_returns_number_as_string():
    assert fizzbuzz_v1(1) == "1"
    assert fizzbuzz_v1(2) == "2"
    return


@app.cell
def _():
    mo.md(r"""
    ## Step 2 — Grow the contract: multiples of 3

    We add a rule to the contract: *"if `n` is a multiple of 3,
    return `'Fizz'`"*. We first write the test (Red), then
    change the implementation to make it pass (Green), **without
    breaking the previous test** (regression).
    """)
    return


@app.function
def fizzbuzz_v2(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)


@app.cell
def test_v2_multiples_of_three_return_fizz():
    assert fizzbuzz_v2(3) == "Fizz"
    assert fizzbuzz_v2(6) == "Fizz"
    return


@app.cell
def test_v2_non_multiples_still_return_number():
    # Regression test inherited from step 1
    assert fizzbuzz_v2(1) == "1"
    assert fizzbuzz_v2(2) == "2"
    return


@app.cell
def _():
    mo.md(r"""
    ## Step 3 — New rule: multiples of 5

    Same approach: a new test describes the expected behavior for
    multiples of 5, then we adapt the implementation.
    """)
    return


@app.function
def fizzbuzz_v3(n):
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


@app.cell
def test_v3_multiples_of_five_return_buzz():
    assert fizzbuzz_v3(5) == "Buzz"
    assert fizzbuzz_v3(10) == "Buzz"
    return


@app.cell
def test_v3_multiples_of_three_still_return_fizz():
    assert fizzbuzz_v3(3) == "Fizz"
    return


@app.cell
def _():
    mo.md(r"""
    ## Step 4 — The trap case: multiples of 15

    This is the most pedagogically interesting test: it reveals a
    **bug** in the current implementation. With `fizzbuzz_v3`, the
    input `15` would return `"Fizz"` (the first matching `if`), while
    the expected contract is `"FizzBuzz"`.

    This test therefore fails first (**Red**), which forces us to
    revisit the order of conditions or the logic (**Green**).
    """)
    return


@app.function
def fizzbuzz_v4(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


@app.cell
def test_v4_multiples_of_fifteen_return_fizzbuzz():
    assert fizzbuzz_v4(15) == "FizzBuzz"
    assert fizzbuzz_v4(30) == "FizzBuzz"
    return


@app.cell
def test_v4_all_previous_rules_still_hold():
    assert fizzbuzz_v4(1) == "1"
    assert fizzbuzz_v4(3) == "Fizz"
    assert fizzbuzz_v4(5) == "Buzz"
    return


@app.cell
def _():
    mo.md(r"""
    ## Step 5 — Refactor: keep the behavior, improve the code

    The tests from the previous steps now form a **safety net**.
    We can rewrite the implementation (for example by building the
    string through concatenation rather than a cascade of `if`
    statements) without fear of regression, since the whole test
    suite must keep passing.

    This is the version we'd consider the final contract of the
    function in production code.
    """)
    return


@app.function
def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz representation of the integer n.

    Contract:
    - if n is a multiple of 3 AND 5: "FizzBuzz"
    - if n is a multiple of 3 only: "Fizz"
    - if n is a multiple of 5 only: "Buzz"
    - otherwise: str(n)

    Raises ValueError if n is not a strictly positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("fizzbuzz expects a strictly positive integer")

    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)


@app.cell
def _():
    mo.md(r"""
    ## Final test suite (parametrized)

    Once the contract is stable, we can group all the cases into a
    single parametrized test — more readable and easier to extend
    than separate tests.
    """)
    return


@app.function
@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (100, "Buzz"),
    ],
)
def test_cases(n, expected):
    assert fizzbuzz(n) == expected


@app.cell
def test_fizzbuzz_rejects_invalid_input():
    with pytest.raises(ValueError):
        fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz(-5)
    return


@app.cell
def _():
    mo.md(r"""
    ## Explore interactively

    Use the field below to call `fizzbuzz` on an integer of your
    choice and see the result live — handy for a classroom demo.
    """)
    return


@app.cell
def _():
    n_input = mo.ui.number(start=1, stop=1000, step=1, value=15, label="n")
    n_input
    return (n_input,)


@app.cell
def _(n_input):
    try:
        result = fizzbuzz(n_input.value)
        output = mo.md(f"`fizzbuzz({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    output
    return


if __name__ == "__main__":
    app.run()
