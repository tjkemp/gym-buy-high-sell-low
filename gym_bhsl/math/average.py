import itertools
from typing import List, Sequence, Union

import numpy as np


def moving_average(
    values: Union[Sequence[float], Sequence[int]], window: int
) -> List[float]:
    """Calculate moving average.

    Args:
        values: a list of values for which to calculate average
        window: the length of window for which to calculate moving averages

    Returns:
        a list of floats of the size `values - windows + 1`

    Example:
        >>> moving_average([0, 0, 1, 2, 4, 5, 4], 3)
        [0.33333, 1.0, 2.33333, 3.66666, 4.33333]

    """
    if window > len(values):
        raise ValueError("Window length must be less or equal to length of values")
    average = np.convolve(values, np.ones(window), "valid") / window
    return average.tolist()


def right_average(values: Sequence[float], num_items: int) -> float:
    """Calculate average of `num_items` rightmost values in a sequence."""
    if not 0 < num_items <= len(values):
        raise ValueError(f"Invalid value for average: {num_items}")
    return (
        sum(itertools.islice(values, len(values) - num_items, len(values))) / num_items
    )
