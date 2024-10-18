#!/usr/bin/env python3
""" Basics Async Syntax
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the total runtime and return it.
    """
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return time.time() - start
