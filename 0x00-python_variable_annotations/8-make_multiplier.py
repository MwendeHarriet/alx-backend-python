#!/usr/bin/env python3
"""Module returns function that multiplies float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Fuction returns function thta multiplies float by multiplier."""
    return lambda x: x * multiplier
