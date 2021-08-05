import pytest

from gym_bhsl.math import average


def test_moving_average():
    values, window_size = [0, 0, 1, 2, 4, 5, 4], 3
    expected = [0.33333333, 1.0, 2.33333333, 3.66666667, 4.33333333]

    result = average.moving_average(values, window_size)

    assert len(expected) == len(result)
    for i, j in zip(result, expected):
        assert i == pytest.approx(j, 0.01)


def test_right_average():
    values, num = [0, 0, 1, 2, 4, 5, 4], 3
    expected = 4.333

    result = average.right_average(values, num)

    assert isinstance(result, float)
    assert result == pytest.approx(expected, 0.01)
