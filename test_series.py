import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_one():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(15)
    expected = 610
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(19)
    expected = 4181
    assert actual == expected


def test_lucas_one():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_two():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_lucas_three():
    actual = lucas(16)
    expected = 2207
    assert actual == expected


def test_sum_series_one():
    actual = sum_series(8, 0, 1)
    expected = 21
    assert actual == expected


def test_sum_series_two():
    actual = sum_series(7, 2, 1)
    expected = 29
    assert actual == expected


def test_sum_series_three():
    actual = sum_series(6, 10, 5)
    expected = 90
    assert actual == expected


