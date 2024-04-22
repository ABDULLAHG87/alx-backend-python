#!/usr/bin/env python3
"""write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function that spawn wait_random in n times"""
    tasks = []
    delays = []

    for index in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
