#!/usr/bin/env python3
""" Basic Async Syntax
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait random delay n times
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for task in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
