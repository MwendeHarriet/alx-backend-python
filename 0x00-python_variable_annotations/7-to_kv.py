#!/usr/bin/env python3
"""Module returns a tuple."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function returns tuple."""
    tup = (k, v*v)
    return tup
