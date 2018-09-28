from add_three_numbers import add_three


def test_add_three_negative():
    result = add_three(-3, -2, -1)
    assert result == -6


def test_add_three_1():
    result = add_three(2, 2, 4)
    assert result == 8


from add_three_numbers import divide_by_three


def divide_by_three_zero():
    result = divide_by_three(0)
    assert result == 0


def divide_by_three_1():
    result = divide_by_three(3)
    assert result == 1
