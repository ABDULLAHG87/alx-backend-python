#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float
"""


import time
import asyncio
wait_n = __import__('1-current_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that returns total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time / n)
