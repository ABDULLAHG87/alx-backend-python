#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A function that loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
