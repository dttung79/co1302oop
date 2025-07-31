from fraction import Fraction

def test_str_01():
    f = Fraction(1, 2)
    expected = "1/2"
    result = str(f)
    assert result == expected

def test_str_02():
    f = Fraction(-1, 2)
    expected = "-1/2"
    result = str(f)
    assert result == expected

def test_str_03():
    f = Fraction(1, -2)
    expected = "-1/2"
    result = str(f)
    assert result == expected

def test_str_04():
    f = Fraction(-1, -2)
    expected = "-1/-2"
    result = str(f)
    assert result == expected

def test_init_01():
    try:
        f = Fraction(1, 0)
        assert False  # If no exception is raised, the test fails
    except ZeroDivisionError as e:
        assert str(e) == "Denominator cannot be zero"


def test_get_01():
    f = Fraction(1, 2)
    expected_numerator = 1
    expected_denominator = 2
    assert f.numerator == expected_numerator
    assert f.denominator == expected_denominator