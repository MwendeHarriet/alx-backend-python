#!/usr/bin/env python3
"""Module retuns sum of float and integers."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function returns sum of float and integers in list."""
    sum = 0
    for num in mxd_list:
        sum += num
    return sum
