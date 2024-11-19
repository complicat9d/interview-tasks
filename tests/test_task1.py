import pytest
from task1.solution import sum_two


def test_sum_two_valid_types():
    assert sum_two(1, 2) == 3
    assert sum_two(0, 0) == 0


def test_sum_two_invalid_types():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)

    with pytest.raises(TypeError):
        sum_two("1", 2)

    with pytest.raises(TypeError):
        sum_two(1, True)
