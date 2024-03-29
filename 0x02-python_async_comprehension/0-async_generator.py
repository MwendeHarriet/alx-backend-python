#!/usr/bin/env python3
"""Module is a coroutine will loop 10 times, each time
    asynchronously wait 1 second, then yield a random
    number between 0 and 10 using the random module."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function looping asynchronously."""
    for i in range(10):
        delay = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield delay
