#!/usr/bin/env python3
"""Module with integers n and max_delay as arguments that measures
    the total execution time for wait_n(n, max_delay), and returns
    total_time / n and returns float (imports from task 1)."""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function calculates elapsed time."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
