import pytest

from fizzbuzz_tdd_kata_jousset.cli import build_parser, main


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["15"])
    assert args.n == 15


def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "1", "--end", "5"])
    assert args.start == 1
    assert args.end == 5


def test_main_prints_single_value(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fizzbuzz-kata", "15"])
    main()
    assert capsys.readouterr().out.strip() == "FizzBuzz"


def test_main_prints_range(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["fizzbuzz-kata", "--start", "1", "--end", "5"],
    )
    main()
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["1", "2", "Fizz", "4", "Buzz"]


def test_main_requires_an_argument(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fizzbuzz-kata"])
    with pytest.raises(SystemExit):
        main()