import pytest
from calculator import SimpleCalculator

@pytest.fixture
def calc():
    return SimpleCalculator()


# 1. Тесты сложения
@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (2.5, 2.5, 5.0), (-5, -5, -10)],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


# 2. Тесты вычитания
@pytest.mark.parametrize(
    "a, b, expected", [(5, 3, 2), (3, 5, -2), (0, 0, 0), (-5, -5, 0)]
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# 3. Тесты умножения
@pytest.mark.parametrize(
    "a, b, expected", [(4, 3, 12), (-2, 3, -6), (0, 10, 0), (2.5, 2, 5.0)]
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# 4. Тесты деления
@pytest.mark.parametrize(
    "a, b, expected", [(10, 2, 5.0), (7, 2, 3.5), (-9, 3, -3.0), (0, 5, 0.0)]
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


# 5. Тесты возведения в степень
@pytest.mark.parametrize(
    "base, exp, expected", [(2, 3, 8), (5, 0, 1), (2, -1, 0.5), (9, 0.5, 3.0)]
)
def test_power(calc, base, exp, expected):
    assert calc.power(base, exp) == expected


# 6. Тесты квадратного корня
@pytest.mark.parametrize(
    "a, expected", [(9, 3.0), (0, 0.0), (2.25, 1.5), (16, 4.0)]
)
def test_sqrt(calc, a, expected):
    assert calc.sqrt(a) == expected


def test_sqrt_negative(calc):
    with pytest.raises(ValueError):
        calc.sqrt(-4)


# 7. Тесты факториала
@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (6, 720)])
def test_factorial(calc, n, expected):
    assert calc.factorial(n) == expected


@pytest.mark.parametrize("n", [-1, 3.5])
def test_factorial_invalid(calc, n):
    with pytest.raises(ValueError):
        calc.factorial(n)


# 8. Тесты простых чисел
@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (13, True),
        (1, False),
        (0, False),
        (-7, False),
        (2.3, False),
    ],
)
def test_is_prime(calc, number, expected):
    assert calc.is_prime(number) == expected


# 9. Тесты расчёта процентов
@pytest.mark.parametrize(
    "part, whole, expected",
    [(50, 200, 25.0), (5, 1, 500.0), (0, 100, 0.0), (200, 200, 100.0)],
)
def test_percentage(calc, part, whole, expected):
    assert calc.percentage(part, whole) == expected


def test_percentage_division_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.percentage(50, 0)