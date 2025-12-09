import math
import pytest

from src.main import factorial, convert_rub_to_currency, average_grade


def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_raises_on_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_convert_rub_to_currency_usd():
    # 180 RUB при курсе 90 = 2 USD
    assert convert_rub_to_currency(180, "USD") == pytest.approx(2.0)


def test_convert_rub_to_currency_eur():
    # 300 RUB при курсе 100 = 3 EUR
    assert convert_rub_to_currency(300, "eur") == pytest.approx(3.0)


def test_convert_rub_to_currency_unsupported():
    with pytest.raises(ValueError):
        convert_rub_to_currency(1000, "GBP")


def test_convert_rub_to_currency_negative_amount():
    with pytest.raises(ValueError):
        convert_rub_to_currency(-100, "USD")


def test_average_grade_basic():
    grades = [4, 5, 3, 5]
    result = average_grade(grades)
    expected = sum(grades) / len(grades)
    assert math.isclose(result, expected)


def test_average_grade_raises_on_empty_list():
    with pytest.raises(ValueError):
        average_grade([])
