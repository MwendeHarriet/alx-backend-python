#!/usr/bin/env python3
"""Module returns sum of float."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function returns sum of list as float."""
    sum = 0.0
    for num in input_list:
        sum += num
    return sum
