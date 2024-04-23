#!/usr/bin/env python3
"""Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.
"""

from typing import List
async_generator = __import___('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function that returns 10 random numbers"""
    results = [j async for j in async_generator()]
    return results
