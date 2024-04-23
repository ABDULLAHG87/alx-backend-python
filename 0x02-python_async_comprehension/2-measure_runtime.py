#!/usr/bin/env python3
"""Write a code that measures runtime coroutine and execute
async comprehension four times in paralle using asyncio.gather
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function that measures the total runtime"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for j in range(4)))

    end_time = time.time()
    return end_time - start_time
