#!/usr/bin/env python3
"""Module is an async routine called wait_n (imports wait_random
    from task 0)that takes in 2 int arguments (in this order):
    n and max_delay. You will spawn wait_random n times with the
    specified max_delaywaiting n times."""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function waiting for n."""
    spawned = []
    for _ in range(n):
        spawned.append(wait_random(max_delay))
    ret = []
    for res in asyncio.as_completed(spawned):
        compl = await res
        ret.append(compl)
    return ret
