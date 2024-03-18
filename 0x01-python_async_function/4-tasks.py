#!/usr/bin/env python3
"""Module takes the code from wait_n and alters it into a
    new function task_wait_n. The code is nearly identical
    to wait_n except task_wait_random is being called."""


import asyncio
from typing import List

wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function waiting for n."""
    spawned = []
    for _ in range(n):
        spawned.append(wait_random(max_delay))
    ret = []
    for res in asyncio.as_completed(spawned):
        compl = await res
        ret.append(compl)
    return ret
